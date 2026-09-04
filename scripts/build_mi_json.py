#!/usr/bin/env python3
"""Build data/labs-mi.json from EGLE SOM Microbiological Lab Certifications PDF text."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path("/workspace/well-lab-index")
TEXT = Path("/tmp/mi-micro.txt")
OUT = ROOT / "data/labs-mi.json"

SOURCE_PDF_URL = (
    "https://www.michigan.gov/egle/-/media/Project/Websites/egle/Documents/"
    "Programs/RRD/Lab/Microbiological-Laboratory-Certifications.pdf"
)
CERT_PAGE = (
    "https://www.michigan.gov/egle/about/organization/"
    "remediation-and-redevelopment/laboratory/certifications"
)
DW_TESTING = "https://www.michigan.gov/egle/public/services/drinking-water-testing"
DW_LAB = (
    "https://www.michigan.gov/egle/about/organization/"
    "remediation-and-redevelopment/laboratory/drinking-water"
)
EGLE_LAB_SITE = "https://www.michigan.gov/eglelab"

HEADER_RE = re.compile(r"^(\d{4})\s+(.+?):\s*$")
ADDR_RE = re.compile(
    r"^[·•\u2022\u00b7]\s*(.+?),\s*([A-Za-z .'-]+),\s*MI,?\s*(\d{5})(?:-(\d{0,4}))?\s*$"
)
# Some address lines miss comma before MI or have incomplete zip trailing dash
ADDR_LOOSE = re.compile(
    r"^[·•\u2022\u00b7]\s*(.+?),\s*([A-Za-z .'-]+),\s*MI,?\s*(\d{5})?-?\s*$"
)
CONTACT_RE = re.compile(
    r"^[·•\u2022\u00b7]\s*(.+?):\s*(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})\s*(\S+@\S+)?\s*$"
)
PHONE_ONLY = re.compile(r"(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})")
EMAIL_RE = re.compile(r"[\w.+-]+@[\w.-]+\.\w+")

# Strip footer / header noise
SKIP_LINE_PREFIXES = (
    "MICHIGAN DEPARTMENT",
    "Remediation & Redevelopment",
    "State of Michigan Certified",
    "The laboratories listed",
    "Laboratory Certification Officers",
    "Phone: (517) 335-9219",
    "Michigan.gov/EGLELab",
    "o Phone:",
)

OMIT_SUBSTRINGS = [
    "water treatment plant",
    "water treatment laboratory",
    "water filtration plant",
    "filtration plant",
    "filtration",  # e.g. Muskegon Heights Filtration
    "water plant",
    "wastewater",
    "wastwater",  # typo in PDF (Manistee)
    "wwtp",
    "wtp",
    "wfp",
    "water authority",
    "water auth",
    "water & sewer authority",
    "water and sewer authority",
    "sewer and water authority",
    "board of public utilities",
    "board of public works",
    "board of water",
    "brd. of water",
    "water utilities",
    "water utility",
    "water department",
    "water dept",
    "waterworks",
    "water works",
    "water system",
    "national park",
    "lake mich. filt",
    "public services laboratory",
    "community utilities authority",
    "charter township water",
    "township water plant",
    "township water system",
    "dkswtp",
    "glwa ",
    "gcdc-wws",
    "treatment plant",
    "water analysis lab",
]

# City-style short names that are utility plant labs (not commercial "…Water Laboratory")
OMIT_EXACT = {
    "paw paw laboratory",
    "rockford water lab",
    "grand ledge water lab",
}

# Health-district labs whose name lacks "health"
HEALTH_OVERRIDE = {
    "assurance water laboratory",  # cmdhd.org — Central Michigan District Health
}

# Keep even if omit substring matches (consultants / commercial with wastewater in name)
KEEP_OVERRIDE = {
    "b&b water/wastewater consultants inc.",
    "egle laboratory services",
}

HEALTH_SUBSTRINGS = [
    "health department",
    "health division",
    "hsd laboratory",
    "hsd lab",
    "community health",
    "health agency",
    "county health",
    "public health",
]

STATE_LAB_NAMES = {
    "egle laboratory services",
}


def normalize_bullet(line: str) -> str:
    # pdftotext sometimes uses odd bullets
    return re.sub(r"^[\s]*[·•\u2022\u00b7]\s*", "· ", line.strip())


def clean_phone(p: str | None) -> str | None:
    if not p:
        return None
    digits = re.sub(r"\D", "", p)
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    if len(digits) == 11 and digits.startswith("1"):
        return f"({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    return p.strip() or None


def slugify(lab_id: str, name: str, city: str) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", f"{name}-{city}".lower()).strip("-")
    return f"mi-{lab_id}-{base[:70]}"


def parse_analytes(block_lines: list[str]) -> list[str]:
    """Parse multi-column analyte rows into a sorted unique list."""
    analytes: list[str] = []
    for raw in block_lines:
        line = raw.rstrip("\n")
        if not line.strip():
            continue
        if line.strip().startswith("Michigan.gov"):
            break
        if HEADER_RE.match(line.strip()):
            break
        # skip page headers that leaked
        if any(line.strip().startswith(p) for p in SKIP_LINE_PREFIXES):
            continue
        if "Certified Analytes" in line:
            continue
        # Split on 2+ spaces for columns
        parts = re.split(r"\s{2,}", line.strip())
        for part in parts:
            a = part.strip()
            if not a:
                continue
            # strip leading underscore used for micro markers in PDF
            a = a.lstrip("_").strip()
            # drop PFAS cross-ref note as analyte
            if a.lower().startswith("z *please"):
                continue
            if a.lower().startswith("*please"):
                continue
            if "please see pfas" in a.lower():
                continue
            if len(a) < 2:
                continue
            analytes.append(a)
    # unique preserve order
    seen = set()
    out = []
    for a in analytes:
        key = a.lower()
        if key not in seen:
            seen.add(key)
            out.append(a)
    return out


def analyte_flags(analytes: list[str]) -> dict:
    joined = " | ".join(a.lower() for a in analytes)
    def has(*needles: str) -> bool:
        return any(n in joined for n in needles)

    coliform = has(
        "total coliform",
        "e. coli",
        "e.coli",
        "fecal coliform",
        "enumeration of tc",
        "enumeration of e. coli",
        "heterotrophic",
    )
    nitrate = has("nitrate", "nitrite")
    lead = has("lead")  # word lead; "lead" as analyte
    # avoid false positive from "please" etc — already filtered
    arsenic = has("arsenic")
    return {
        "coliform_listed": coliform,
        "nitrate_listed": nitrate,
        "lead_listed": lead,
        "arsenic_listed": arsenic,
    }


def should_omit(name: str) -> bool:
    n = name.lower().strip()
    if n in KEEP_OVERRIDE or n in HEALTH_OVERRIDE:
        return False
    if any(h in n for h in HEALTH_SUBSTRINGS):
        return False
    if n in STATE_LAB_NAMES:
        return False
    # LMAS = district health lab
    if n.startswith("lmas "):
        return False
    if n in OMIT_EXACT:
        return True
    for s in OMIT_SUBSTRINGS:
        if s in n:
            return True
    # GLWA without trailing space
    if n.startswith("glwa"):
        return True
    # city/township utility leftovers
    if "utilities authority" in n:
        return True
    if "regional utility" in n:
        return True
    if "regional water authority" in n:
        return True
    if "charter township" in n and "health" not in n:
        return True
    return False


def category_for(name: str) -> str:
    n = name.lower()
    if n in STATE_LAB_NAMES or n.startswith("egle "):
        return "state_lab"
    if n in HEALTH_OVERRIDE or any(h in n for h in HEALTH_SUBSTRINGS) or n.startswith("lmas "):
        return "health_department"
    if "university" in n or "college" in n:
        return "university"
    return "commercial"


def parse_labs(text: str) -> list[dict]:
    lines = text.splitlines()
    labs: list[dict] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = HEADER_RE.match(line.strip())
        if not m:
            i += 1
            continue
        lab_id, name = m.group(1), m.group(2).strip()
        i += 1
        address = None
        city = None
        zip_code = None
        street = None
        contact_name = None
        phone = None
        email = None
        analyte_lines: list[str] = []
        in_analytes = False

        while i < len(lines):
            raw = lines[i]
            stripped = raw.strip()
            # next lab
            if HEADER_RE.match(stripped):
                break
            # page form feed
            if stripped.startswith("\x0c") or stripped == "\x0c":
                i += 1
                continue
            if stripped.startswith("Michigan.gov/EGLELab"):
                i += 1
                # skip until next lab or continue collecting? footer ends page; next lines are headers
                i += 1
                # consume following department headers until blank or next lab
                while i < len(lines):
                    s2 = lines[i].strip()
                    if HEADER_RE.match(s2):
                        break
                    if s2.startswith("Michigan.gov"):
                        i += 1
                        continue
                    if any(s2.startswith(p) for p in SKIP_LINE_PREFIXES) or not s2:
                        i += 1
                        continue
                    # if somehow analytes continue across page (rare) — keep
                    if in_analytes and s2 and not HEADER_RE.match(s2):
                        analyte_lines.append(lines[i])
                        i += 1
                        continue
                    i += 1
                continue

            norm = normalize_bullet(raw)
            if "Certified Analytes" in stripped:
                in_analytes = True
                i += 1
                continue

            if in_analytes:
                if any(stripped.startswith(p) for p in SKIP_LINE_PREFIXES):
                    i += 1
                    continue
                analyte_lines.append(raw)
                i += 1
                continue

            # address / contact bullets
            if norm.startswith("·"):
                body = norm[1:].strip()
                # contact line: Name: (phone) email
                cm = CONTACT_RE.match("· " + body)
                if cm:
                    contact_name = cm.group(1).strip()
                    phone = clean_phone(cm.group(2))
                    email = (cm.group(3) or "").strip() or None
                    if email:
                        email = email.rstrip(".,;")
                    i += 1
                    continue
                # try looser contact: has phone
                if PHONE_ONLY.search(body) and ":" in body:
                    name_part, rest = body.split(":", 1)
                    contact_name = name_part.strip()
                    ph = PHONE_ONLY.search(rest)
                    phone = clean_phone(ph.group(1) if ph else None)
                    em = EMAIL_RE.search(rest)
                    email = em.group(0).rstrip(".,;") if em else None
                    i += 1
                    continue
                # address
                am = ADDR_RE.match("· " + body) or ADDR_LOOSE.match("· " + body)
                if am:
                    street = am.group(1).strip().rstrip(",")
                    city = am.group(2).strip()
                    zip_code = am.group(3) if am.lastindex >= 3 else None
                    if zip_code == "":
                        zip_code = None
                    # Isle Royale special: "Rock Harbor Water Analysis Lab, Houghton, MI"
                    address_parts = [street]
                    if city:
                        address_parts.append(city)
                    address_parts.append("MI")
                    if zip_code:
                        address_parts[-1] = f"MI {zip_code}"
                    address = ", ".join(
                        [street, f"{city}, MI" + (f" {zip_code}" if zip_code else "")]
                    )
                    i += 1
                    continue
                # fallback address without perfect parse
                if ", MI" in body or ",MI" in body:
                    address = body.strip().rstrip("-").strip()
                    # try extract city/zip
                    zm = re.search(
                        r",\s*([A-Za-z .'-]+),\s*MI,?\s*(\d{5})?", body
                    )
                    if zm:
                        city = zm.group(1).strip()
                        zip_code = zm.group(2)
                        street = body[: zm.start()].strip().lstrip("· ").rstrip(",")
                    i += 1
                    continue
            i += 1

        analytes = parse_analytes(analyte_lines)
        flags = analyte_flags(analytes)
        omit = should_omit(name)
        cat = None if omit else category_for(name)

        labs.append(
            {
                "lab_id": lab_id,
                "name": name,
                "street": street,
                "city": city,
                "state": "MI",
                "zip": zip_code,
                "address": address,
                "contact_name": contact_name,
                "phone": phone,
                "email": email,
                "analytes": analytes,
                **flags,
                "omit": omit,
                "category": cat,
            }
        )
    return labs


def main() -> None:
    if not TEXT.exists():
        raise SystemExit(f"missing {TEXT}; run pdftotext -layout")
    text = TEXT.read_text(encoding="utf-8", errors="replace")
    # normalize weird bullet char to middot
    text = text.replace("\uf0b7", "·").replace("", "·")

    parsed = parse_labs(text)
    if len(parsed) < 100:
        raise SystemExit(f"too few labs parsed: {len(parsed)}")

    omitted = [p for p in parsed if p["omit"]]
    kept_raw = [p for p in parsed if not p["omit"]]

    labs_out = []
    for p in kept_raw:
        is_egle = p["name"].lower().startswith("egle laboratory")
        accepts = "yes" if is_egle else "unknown"
        mail = (
            "ship or pickup — order kits by phone (EGLE drinking-water testing page)"
            if is_egle
            else "unknown"
        )
        notes = (
            "EGLE Laboratory Services. EGLE’s drinking-water testing page states the lab "
            "accepts homeowner kits; order by phone; ship or pick up. Prices omitted."
            if is_egle
            else (
                "Listed on EGLE State of Michigan Certified Laboratories (microbiological / "
                "chemistry) PDF dated 3/11/2026. Appearance on that list is certification for "
                "the stated analytes, not verification that the lab accepts private-well / "
                "homeowner samples. Call before shipping."
            )
        )
        labs_out.append(
            {
                "id": slugify(p["lab_id"], p["name"], p["city"] or "mi"),
                "lab_id": p["lab_id"],
                "name": p["name"],
                "city": p["city"] or "unknown",
                "state": "MI",
                "zip": p["zip"],
                "address": p["address"],
                "street": p["street"],
                "phone": p["phone"] or "unknown",
                "email": p["email"],
                "contact_name": p["contact_name"],
                "category": p["category"],
                "accepts_private_well_samples": accepts,
                "sample_dropoff_or_mail": mail,
                "coliform_listed": p["coliform_listed"],
                "nitrate_listed": p["nitrate_listed"],
                "lead_listed": p["lead_listed"],
                "arsenic_listed": p["arsenic_listed"],
                "analytes": p["analytes"],
                "notes": notes,
                "source_url": SOURCE_PDF_URL,
                "source_urls": [SOURCE_PDF_URL, CERT_PAGE, DW_TESTING],
                "source_document": (
                    "State of Michigan Certified Laboratories: Microbiological "
                    "(SOM Certified Labs - Chemistry 3/11/2026)"
                ),
                "source_retrieved": "2026-09-03",
                "source_document_date": "2026-03-11",
            }
        )

    # sort kept by name
    labs_out.sort(key=lambda L: (L["name"].lower(), L["city"].lower()))

    omitted_list = [
        {
            "lab_id": p["lab_id"],
            "name": p["name"],
            "city": p["city"],
            "reason": "municipal_utility_or_pws_lab",
        }
        for p in omitted
    ]
    omitted_list.sort(key=lambda x: x["name"].lower())

    health_n = sum(1 for L in labs_out if L["category"] == "health_department")
    commercial_n = sum(1 for L in labs_out if L["category"] == "commercial")
    state_n = sum(1 for L in labs_out if L["category"] == "state_lab")
    univ_n = sum(1 for L in labs_out if L["category"] == "university")

    doc = {
        "state": "Michigan",
        "state_code": "MI",
        "last_updated": "2026-09-03",
        "source": {
            "title": (
                "State of Michigan Certified Laboratories: Microbiological "
                "(EGLE; footer SOM Certified Labs - Chemistry 3/11/2026)"
            ),
            "url": SOURCE_PDF_URL,
            "document_date": "2026-03-11",
            "retrieved": "2026-09-03",
            "certifications_page": CERT_PAGE,
            "drinking_water_testing": DW_TESTING,
            "drinking_water_lab": DW_LAB,
            "egle_lab": EGLE_LAB_SITE,
            "archived_pdf": "data/sources/mi-microbiological-lab-certifications.pdf",
            "limitations": [
                (
                    "The EGLE SOM certified-labs PDF lists laboratories certified for the "
                    "analytes shown (microbiological and chemistry mixed). It is not, by "
                    "itself, a private-well-owner directory."
                ),
                (
                    "Municipal water-treatment, filtration, wastewater, water-authority, "
                    "board-of-public-works/utilities, GLWA, and similar utility plant "
                    "laboratories were omitted from this directory. That omission is a "
                    "directory choice for private well owners, not a statement about their "
                    "certification. They remain on the official EGLE list."
                ),
                (
                    "Except for EGLE Laboratory Services (verified via EGLE’s drinking-water "
                    "testing page for homeowner kits), Well Labs Index has not independently "
                    "verified that these laboratories currently accept private-well samples."
                ),
                (
                    "Coliform/micro, nitrate, lead, and arsenic columns are derived from "
                    "analytes printed on the official PDF. Always call to confirm current "
                    "certification and sample acceptance. Prices are intentionally omitted."
                ),
            ],
            "pdf_labs_total": len(parsed),
            "omitted_municipal_utility_count": len(omitted),
            "omitted_labs": omitted_list,
        },
        "lab_count": len(labs_out),
        "verified_private_well_count": sum(
            1 for L in labs_out if L["accepts_private_well_samples"] == "yes"
        ),
        "category_counts": {
            "state_lab": state_n,
            "health_department": health_n,
            "commercial": commercial_n,
            "university": univ_n,
        },
        "labs": labs_out,
    }

    OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
    print(
        f"wrote {OUT}: kept={len(labs_out)} omitted={len(omitted)} "
        f"total={len(parsed)} health={health_n} commercial={commercial_n} "
        f"state={state_n}"
    )
    # sanity: EGLE present
    egle = [L for L in labs_out if L["lab_id"] == "0001"]
    assert egle and egle[0]["accepts_private_well_samples"] == "yes"
    print("EGLE verified OK:", egle[0]["phone"], egle[0]["address"])


if __name__ == "__main__":
    main()
