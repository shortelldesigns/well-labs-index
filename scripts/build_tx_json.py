#!/usr/bin/env python3
"""Build data/labs-tx.json from TCEQ PWS Lab Map Table (Excel, updated 03/26/2026)."""
from __future__ import annotations

import json
import re
from pathlib import Path

import openpyxl

ROOT = Path("/workspace/well-lab-index")
XLSX = ROOT / "data/sources/tx-pws-lab-map-table-2026-03-26.xlsx"
OUT = ROOT / "data/labs-tx.json"

SOURCE_URL_PDF = "https://www.tceq.texas.gov/downloads/drinking-water/quality-assurance/pws-lab-map-table.pdf"
SOURCE_URL_XLSX = "https://www.tceq.texas.gov/downloads/drinking-water/quality-assurance/pws-lab-map-table.xlsx"
PWSS_PAGE = "https://www.tceq.texas.gov/drinkingwater/pwss.html"
STEPS_PAGE = "https://www.tceq.texas.gov/assistance/resources/steps-to-locate-an-accredited-laboratory"
TWDB_PAGE = "https://www.twdb.texas.gov/groundwater/data/privwwsamp.asp"
LCRA_PAGE = "https://www.lcra.org/services/els/residential-water-testing/"
NELAP_SEARCH = "https://www.tceq.texas.gov/agency/qa/env_lab_accreditation.html"

# Omit city water-plant / utility / river-authority / water-district labs from the
# homeowner directory (same approach as OH/WI). LCRA is an exception: its own
# public page offers residential / private water-supply testing.
OMIT_NAME_SUBSTRINGS = [
    "water supply corporation",
    "water supply",
    "water authority",
    "water district",
    "municipal water",
    "water utility",
    "water utilities",
    "water department",
    "water plant",
    "water works",
    "water resources",
    "river authority",
    "north water district",
    "water utility services",
]

# Keep these even if they match omit substrings
KEEP_NAMES = {
    "lower colorado river authority environmental laboratory services",
}

HEALTH_SUBSTRINGS = [
    "health department",
    "public health",
    "health district",
    "department of state health",
    "department of public health",
    "metropolitan health",
]


def slugify(name: str, city: str) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", f"{name}-{city}".lower()).strip("-")
    return "tx-" + (base[:80] or "lab")


def yn(val) -> bool:
    return str(val or "").strip().upper() == "Y"


def clean_phone(p) -> str:
    if p is None:
        return "unknown"
    s = str(p).strip()
    s = re.sub(r"\s+", " ", s)
    s = s.replace("Tx", "").strip()
    # normalize broken spacing like "956- 681-1720"
    s = re.sub(r"(\d)-\s+(\d)", r"\1-\2", s)
    return s or "unknown"


def category_for(name: str) -> str | None:
    n = name.lower()
    if any(h in n for h in HEALTH_SUBSTRINGS) or "health" in n and (
        "county" in n or "city of" in n or "district" in n or "bureau" in n
    ):
        return "health_department"
    if "university" in n or "texas state" in n or "tiaer" in n or "applied environmental research" in n:
        return "university"
    if "department of state health" in n:
        return "health_department"
    keep = n in KEEP_NAMES
    if any(s in n for s in OMIT_NAME_SUBSTRINGS) and not keep:
        return None  # omit
    if "city of" in n and "health" not in n:
        # city labs that are not health depts (water plants already caught; catch leftovers)
        if any(x in n for x in ("lab", "laboratory", "environmental")):
            return None
    if keep:
        return "river_authority_residential"  # LCRA special
    return "commercial"


def main() -> None:
    wb = openpyxl.load_workbook(XLSX, data_only=True)
    ws = wb["Public Labs"]
    rows = list(ws.iter_rows(values_only=True))
    header = rows[0]
    assert str(header[0]).strip() == "Map ID", header

    kept = []
    omitted = []
    for r in rows[1:]:
        if not r or r[0] is None:
            continue
        try:
            map_id = int(r[0])
        except Exception:
            continue
        name = str(r[1]).strip()
        phone = clean_phone(r[2])
        micro = yn(r[3])
        lcr = yn(r[4])
        wqp = yn(r[5])
        county = str(r[6] or "unknown").strip()
        address = str(r[7] or "unknown").strip()
        city = str(r[8] or "unknown").strip()
        state = str(r[9] or "TX").strip()
        zipc = r[10]
        zip_s = str(zipc).strip() if zipc is not None else "unknown"
        if zip_s.endswith(".0"):
            zip_s = zip_s[:-2]
        fri = r[11]
        sat = r[12]
        sun = r[13]

        cat = category_for(name)
        if cat is None:
            omitted.append({"map_id": map_id, "name": name, "city": city, "reason": "municipal_utility_or_pws_lab"})
            continue

        is_lcra = "lower colorado river authority" in name.lower()
        accepts = "yes" if is_lcra else "unknown"
        mail = "mail or drop-off (lab page: kit ship or pick up)" if is_lcra else "unknown"
        notes = (
            "Listed on TCEQ Public Water System Lab Map Table (updated 03/26/2026). "
            "That table is for NELAP-accredited drinking-water public laboratories offering "
            "microbial, lead-and-copper (LCR), and/or water-quality-parameter (WQP) testing. "
            "It is not a private-well-owner directory. Call before sending a private-well sample."
        )
        if is_lcra:
            notes = (
                "On the TCEQ PWS Lab Map Table (updated 03/26/2026). LCRA Environmental Laboratory "
                "Services’ residential water testing page (retrieved 2 September 2026) offers testing "
                "of residential / private drinking or domestic water sources, bottle kits by mail or "
                "pickup, and drop-off. Prices intentionally omitted."
            )

        weekend = {}
        if micro:
            weekend = {
                "friday": None if fri is None else str(fri).strip(),
                "saturday": None if sat is None else str(sat).strip(),
                "sunday": None if sun is None else str(sun).strip(),
            }

        lab = {
            "id": slugify(name, city),
            "map_id": map_id,
            "name": name,
            "city": city,
            "county": county,
            "state": state if state else "TX",
            "zip": zip_s,
            "address": f"{address}, {city}, {state} {zip_s}".replace("  ", " "),
            "street": address,
            "phone": phone,
            "category": cat,
            "accepts_private_well_samples": accepts,
            "sample_dropoff_or_mail": mail,
            "coliform_listed": micro,
            "lcr_listed": lcr,
            "wqp_listed": wqp,
            "nitrate_listed": False,  # not on this table
            "trace_metals_listed": lcr,  # LCR = lead and copper program; not a full metals claim
            "microbial_weekend": weekend or None,
            "notes": notes,
            "source_url": SOURCE_URL_PDF,
            "source_urls": [SOURCE_URL_PDF, SOURCE_URL_XLSX],
            "source_document": "Public Water System Lab Map Table, TCEQ Water Supply Division, updated 03/26/2026",
            "source_retrieved": "2026-09-02",
            "source_document_date": "2026-03-26",
        }
        if is_lcra:
            lab["verification_url"] = LCRA_PAGE
            lab["verification_note"] = (
                "LCRA residential water supply testing page describes private drinking/domestic "
                "water testing, kits, mail/drop-off. Retrieved 2026-09-02."
            )
        kept.append(lab)

    kept.sort(key=lambda x: (x["name"].lower(), x["city"].lower()))
    verified = [l for l in kept if l["accepts_private_well_samples"] == "yes"]

    payload = {
        "state": "Texas",
        "state_code": "TX",
        "last_updated": "2026-09-02",
        "source": {
            "title": "Public Water System Lab Map Table, TCEQ Water Supply Division, updated 03/26/2026",
            "url": SOURCE_URL_PDF,
            "excel_url": SOURCE_URL_XLSX,
            "document_date": "2026-03-26",
            "retrieved": "2026-09-02",
            "pwss_page": PWSS_PAGE,
            "steps_to_locate": STEPS_PAGE,
            "twdb_private_well": TWDB_PAGE,
            "lcra_residential": LCRA_PAGE,
            "nelap_accreditation": NELAP_SEARCH,
            "limitations": [
                "The PWS Lab Map Table lists NELAP-accredited drinking-water public laboratories that offer microbial total coliforms, lead and copper (LCR), and/or water quality parameters (WQP). It is aimed at public water systems; appearance on it is not an endorsement and is not, by itself, a statement that the lab takes homeowner / private-well samples.",
                "Municipal water-plant, city utility, river-authority (except LCRA, which publishes a residential testing program), water-district, and water-supply-corporation laboratories were omitted from this directory. That omission is a directory choice for private well owners, not a statement about their certification. They remain on the official TCEQ table.",
                "Except for Lower Colorado River Authority Environmental Laboratory Services, Well Labs Index has not independently verified that these laboratories currently accept private-well samples.",
                "Microbial / LCR / WQP columns follow the TCEQ table (Y/N). Nitrate and other chemistry are not listed on this table — contact the lab. Weekend acceptability columns apply only to microbial labs and change; always call.",
                "TCEQ and TWDB both say to always call laboratories to confirm address, sample drop-off hours, and prices. Prices are intentionally omitted from this site.",
                "For a full NELAP search by matrix/analyte, use TCEQ’s accredited-laboratory database or the steps at Steps to Locate an Accredited Environmental Laboratory.",
            ],
            "excel_rows_total": 80,
            "omitted_municipal_utility_count": len(omitted),
            "omitted_labs": omitted,
        },
        "lab_count": len(kept),
        "verified_private_well_count": len(verified),
        "labs": kept,
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {OUT} with {len(kept)} labs, {len(verified)} verified, {len(omitted)} omitted")


if __name__ == "__main__":
    main()
