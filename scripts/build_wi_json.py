import openpyxl, json, re, html as htmlmod
from collections import defaultdict
from pathlib import Path

ROOT = Path("/workspace/well-lab-index")
XLSX = ROOT / "data/sources/wi-dw-labs-jan-2026.xlsx"
BACTI_HTML = ROOT / "data/sources/wi-bactilab-2026-09-01.html"
OUT_JSON = ROOT / "data/labs-wi.json"

SOURCE_EXCEL_URL = "https://dnr.wisconsin.gov/sites/default/files/topic/LabCert/DWLabs012126.xlsx"
SOURCE_LISTS_PAGE = "https://dnr.wisconsin.gov/topic/labCert/certified-lab-lists"
SOURCE_BACTI = "https://apps.dnr.wi.gov/dwsportalpub/BactiLab"
SOURCE_PRIVATE_WELL = "https://dnr.wisconsin.gov/topic/Wells/privateWellTest.html"
WSLH_PUBLIC = "https://www.slh.wisc.edu/environmental/water/public-health-tests-available-to-wisconsin-citizens/"
WSLH_KITS = "https://www.slh.wisc.edu/environmental/water/public-environmental-and-water-testing-prices/"
WEAL_PAGE = "https://www.uwsp.edu/center-for-watershed-science-and-education/well-water-testing/"
RETRIEVED = "2026-09-01"
DOC_DATE_EXCEL = "2026-01-21"

def fmt_phone(raw):
    if raw is None:
        return "unknown"
    digits = re.sub(r"\D", "", str(raw))
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    if len(digits) == 10:
        return f"{digits[0:3]}-{digits[3:6]}-{digits[6:10]}"
    s = str(raw).strip()
    return s if s else "unknown"

def slugify(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.lower())
    return s.strip("-")[:60]

def param_bases(params):
    bases = []
    for p in params:
        base = p.split(" - ")[0].replace("## ", "").strip()
        if base and base not in bases:
            bases.append(base)
    return bases

def summarize_other(bases, nitrate, arsenic):
    skip = set()
    if nitrate:
        skip.update({"Nitrate", "Nitrite", "Nitrate + Nitrite"})
    if arsenic:
        skip.add("Arsenic")
    kept = [b for b in bases if b not in skip]
    if not kept:
        return "—"
    if len(kept) <= 6:
        return ", ".join(kept)
    return ", ".join(kept[:5]) + f", +{len(kept)-5} more"

wb = openpyxl.load_workbook(XLSX, data_only=True)
rows = list(wb.active.iter_rows(values_only=True))
headers = rows[0]
by_fid = defaultdict(list)
for r in rows[1:]:
    if not any(r):
        continue
    d = dict(zip(headers, r))
    by_fid[d["FID"]].append(d)

OMIT_EXCEL_TYPES = {"Municipal Lab", "Public Water Supply Lab", "Industrial Lab"}
excel_labs = []
for fid, rs in sorted(by_fid.items(), key=lambda x: str(x[1][0]["Lab Name"]).lower()):
    r0 = rs[0]
    state = str(r0["State"] or "").strip().upper()
    if state != "WI":
        continue
    lab_type = str(r0["Lab Type"] or "").strip()
    if lab_type in OMIT_EXCEL_TYPES:
        continue
    params = sorted({str(x["Parameter"]) for x in rs})
    bases = param_bases(params)
    nitrate = any("nitrate" in p.lower() for p in params)
    arsenic = any("arsenic" in p.lower() for p in params)
    name = str(r0["Lab Name"]).strip()
    category = "public_health" if "Public Health" in lab_type else "commercial"
    excel_labs.append({
        "id": f"wi-{slugify(name)}",
        "fid": str(fid),
        "name": name,
        "city": str(r0["City"] or "unknown").strip(),
        "county": str(r0["County"] or "unknown").strip(),
        "state": "WI",
        "address": "unknown",
        "phone": fmt_phone(r0["Phone"]),
        "lab_type": lab_type,
        "category": category,
        "source_lists": ["dnr_chemistry"],
        "accepts_private_well_samples": "unknown",
        "sample_dropoff_or_mail": "unknown",
        "coliform_listed": False,
        "nitrate_listed": nitrate,
        "arsenic_listed": arsenic,
        "chemistry_parameter_bases": bases,
        "chemistry_other_summary": summarize_other(bases, nitrate, arsenic),
        "notes": "Listed on WI DNR Accredited Laboratories — January 2026 drinking-water chemistry list (NR 809 and NR 812). Appearance is not a statement that the lab accepts private-well samples unless separately verified.",
        "source_url": SOURCE_EXCEL_URL,
        "source_urls": [SOURCE_EXCEL_URL, SOURCE_LISTS_PAGE],
        "source_document": "Accredited Laboratories - January 2026 / Drinking water certified labs - chemistry - NR 809 and NR 812 (DWLabs012126.xlsx)",
        "source_retrieved": RETRIEVED,
        "source_document_date": DOC_DATE_EXCEL,
    })

html = BACTI_HTML.read_text(errors="replace")
tbody = re.search(r"<tbody>(.*?)</tbody>", html, re.S | re.I).group(1)
bacti_rows = []
for r in re.findall(r"<tr>(.*?)</tr>", tbody, re.S | re.I):
    cells = re.findall(r"<td[^>]*>(.*?)</td>", r, re.S | re.I)
    if len(cells) < 7:
        continue
    def clean(c):
        c = re.sub(r"<br\s*/?>", ", ", c, flags=re.I)
        c = re.sub(r"<[^>]+>", "", c)
        c = htmlmod.unescape(c)
        return re.sub(r"\s+", " ", c).strip(" ,")
    bacti_rows.append({
        "name": clean(cells[0]),
        "lab_ids": clean(cells[1]),
        "phone": clean(cells[3]),
        "street_address": clean(cells[4]),
    })

OMIT_BACTI = re.compile(
    r"(water\s*(treatment|utility|works|department|dept|plant)|waste\s*water|wastewater|wwtp|"
    r"pollution\s*control|sanitary\s*district|sewerage|sewage|water\s*&\s*sewer|water\s*&\s*light|"
    r"water\s*light\s*power|public\s*utilities|utility\s*commission|\butilities\b|m\s*m\s*s\s*d|"
    r"water\s*division|water\s*&\s*sewage)",
    re.I,
)
MUNI_ENTITY = re.compile(r"^(CITY|VILLAGE|TOWN)\s+OF\s+(?!.*HEALTH).+", re.I)
EXTRA = {
    "NORTH SHORE WATER COMMISSION", "KOHLER CO.", "KWIK TRIP INC *", "KWIK TRIP INC",
    "FARM FIRST DAIRY COOPERATIVE", "WISCONSIN DEPARTMENT OF AGRICULTURE, TRADE AND CONSUMER PROTECTION",
    "MANITOWOC PUBLIC UTILITIES", "SUPERIOR WATER LIGHT POWER CO", "TWO RIVERS WATER & LIGHT",
    "MARSHFIELD UTILITIES", "LAKE GENEVA UTILITY COMMISSION",
}
EXTRA_NORM = {re.sub(r"[* ]+$", "", x.upper()) for x in EXTRA}

def omit_bacti(name):
    n = name.strip()
    if re.sub(r"[* ]+$", "", n.upper()) in EXTRA_NORM:
        return True
    if OMIT_BACTI.search(n):
        if re.search(r"health", n, re.I) and not re.search(
            r"wastewater|water utility|water works|water treatment|water dept|water department", n, re.I
        ):
            return False
        return True
    if MUNI_ENTITY.match(n) and not re.search(r"health", n, re.I):
        return True
    return False

bacti_kept, bacti_omitted = [], []
for lab in bacti_rows:
    (bacti_omitted if omit_bacti(lab["name"]) else bacti_kept).append(lab)

def parse_city(street):
    m = re.search(r",\s*([^,]+)\s+WI\s+(\d{5})", street, re.I)
    if m:
        return m.group(1).strip().title()
    return "unknown"

def classify(name):
    n = name.upper()
    if "HEALTH" in n or "DHHS" in n or "HUMAN SERVICES" in n:
        return "health_department"
    if "STATE LABORATORY OF HYGIENE" in n:
        return "public_health"
    if "WATER & ENVIRONMENTAL ANALYSIS" in n or "UWSP" in n:
        return "public_health"
    if "UNIVERSITY OF WISCONSIN" in n or n.startswith("UW-"):
        return "university"
    if n.startswith("COUNTY OF ") or n in {"CHIPPEWA COUNTY", "IOWA COUNTY", "LANGLADE COUNTY"}:
        return "health_department"
    if "PARKS" in n and "LAND USE" in n:
        return "health_department"
    return "commercial"

def norm_name(n):
    n = n.upper().replace("&", "AND")
    n = re.sub(r"[^A-Z0-9]+", " ", n)
    n = re.sub(r"\b(INC|LLC|LABORATORIES|LABORATORY|LABS|LAB|CO|COMPANY|THE|DEPT|DEPARTMENT)\b", " ", n)
    return re.sub(r"\s+", " ", n).strip()

excel_by_norm = {norm_name(l["name"]): l for l in excel_labs}
excel_by_fid = {l["fid"]: l for l in excel_labs}
for b in bacti_kept:
    matched = None
    for fid in re.findall(r"\d{9}", b["lab_ids"]):
        if fid in excel_by_fid:
            matched = excel_by_fid[fid]
            break
    if not matched:
        nn = norm_name(b["name"])
        if nn in excel_by_norm:
            matched = excel_by_norm[nn]
        else:
            for en, el in excel_by_norm.items():
                if nn and (nn in en or en in nn):
                    matched = el
                    break
    if matched:
        matched["coliform_listed"] = True
        if "bactilab" not in matched["source_lists"]:
            matched["source_lists"].append("bactilab")
        if SOURCE_BACTI not in matched["source_urls"]:
            matched["source_urls"].append(SOURCE_BACTI)
        if matched["address"] == "unknown" and b["street_address"]:
            matched["address"] = b["street_address"]
        b["_matched"] = matched["id"]
    else:
        b["_matched"] = None

bacti_only = []
for b in bacti_kept:
    if b.get("_matched"):
        continue
    cat = classify(b["name"])
    lab = {
        "id": f"wi-bacti-{slugify(b['name'])}",
        "fid": (re.findall(r"\d{9}", b["lab_ids"]) or [None])[-1],
        "name": b["name"],
        "city": parse_city(b["street_address"]),
        "county": "unknown",
        "state": "WI",
        "address": b["street_address"] or "unknown",
        "phone": fmt_phone(b["phone"]),
        "lab_type": "DATCP coliform-certified (BactiLab)",
        "category": cat,
        "source_lists": ["bactilab"],
        "accepts_private_well_samples": "unknown",
        "sample_dropoff_or_mail": "unknown",
        "coliform_listed": True,
        "nitrate_listed": False,
        "arsenic_listed": False,
        "chemistry_parameter_bases": [],
        "chemistry_other_summary": "—",
        "notes": "Listed on WI DNR/DATCP BactiLab portal as certified for Coliform Bacteria analysis of drinking water samples (enzyme substrate method). Municipal water utilities and wastewater plants were omitted from this directory.",
        "source_url": SOURCE_BACTI,
        "source_urls": [SOURCE_BACTI],
        "source_document": "Drinking Water Bacti Labs (DATCP-certified coliform), apps.dnr.wi.gov/dwsportalpub/BactiLab",
        "source_retrieved": RETRIEVED,
        "source_document_date": RETRIEVED,
    }
    if "WATER & ENVIRONMENTAL ANALYSIS" in b["name"].upper():
        lab["accepts_private_well_samples"] = "yes"
        lab["verified_private_well"] = True
        lab["name"] = "WATER & ENVIRONMENTAL ANALYSIS (WEAL, UW-Stevens Point)"
        lab["sample_dropoff_or_mail"] = "Kits via county UW-Extension offices; call (715) 346-3209; weal@uwsp.edu"
        lab["source_urls"].append(WEAL_PAGE)
    bacti_only.append(lab)

for l in excel_labs:
    if "State Laboratory of Hygiene" in l["name"]:
        l["accepts_private_well_samples"] = "yes"
        l["verified_private_well"] = True
        l["sample_dropoff_or_mail"] = "Drop-off Mon–Fri 7:45 AM–4:30 PM, 2601 Agriculture Drive, Madison; kits: call (800) 442-4618 or (608) 224-6202 (WSLH public pages)"
        l["source_urls"] = list(dict.fromkeys(l["source_urls"] + [WSLH_PUBLIC, WSLH_KITS, SOURCE_BACTI]))
        l["coliform_listed"] = True
        l["address"] = "2601 Agriculture Drive, Madison, WI"
    if "UWSP Water and Environmental" in l["name"]:
        l["name"] = "UWSP Water and Environmental Analysis Lab (WEAL)"
        l["accepts_private_well_samples"] = "yes"
        l["verified_private_well"] = True
        l["sample_dropoff_or_mail"] = "Kits via county UW-Extension offices (WEAL well-water-testing page); call (715) 346-3209; weal@uwsp.edu"
        l["source_urls"] = list(dict.fromkeys(l["source_urls"] + [WEAL_PAGE, SOURCE_BACTI]))
        l["coliform_listed"] = True
        l["address"] = "800 Reserve St, Stevens Point, WI"

all_labs = []
seen = set()
for l in excel_labs + bacti_only:
    if l["id"] in seen:
        continue
    seen.add(l["id"])
    all_labs.append(l)

verified_count = sum(1 for l in all_labs if l.get("accepts_private_well_samples") == "yes")
payload = {
    "state": "Wisconsin",
    "state_code": "WI",
    "last_updated": "2026-09-01",
    "source": {
        "title": "WI DNR Accredited Laboratories - January 2026 (drinking water chemistry NR 809/NR 812) plus DATCP/DNR BactiLab coliform list",
        "url": SOURCE_LISTS_PAGE,
        "document_date": DOC_DATE_EXCEL,
        "retrieved": RETRIEVED,
        "excel_url": SOURCE_EXCEL_URL,
        "bactilab_url": SOURCE_BACTI,
        "private_well_testing_url": SOURCE_PRIVATE_WELL,
        "wslh_public_health_tests": WSLH_PUBLIC,
        "wslh_kit_ordering": WSLH_KITS,
        "weal_well_water_testing": WEAL_PAGE,
        "limitations": [
            "The January 2026 Excel is a drinking-water chemistry accreditation list (NR 809 and NR 812), also linked for homeowners on the DNR certified-lab-lists page. It is not by itself a private-well acceptance directory.",
            "BactiLab lists DATCP-certified labs for coliform bacteria analysis of drinking water. Certification is not an endorsement (portal disclaimer).",
            "Municipal water utilities, wastewater treatment plants, sanitary districts, and similar public-system laboratories were omitted from this directory. That is a directory choice for private well owners, not a statement about their certification.",
            "Out-of-state laboratories on the chemistry Excel (often PFAS-only or specialty) were omitted; they remain on the official file.",
            "Industrial laboratories (e.g., Kohler Co. CHEM Lab) and the DATCP agency laboratory itself were omitted as not homeowner-facing.",
            "Only Wisconsin State Laboratory of Hygiene and UWSP Water & Environmental Analysis Lab (WEAL) are independently verified here to serve private well / homeowner samples, via their own public pages.",
            "Prices are intentionally omitted (they change). Call the lab.",
            "Certification and phone numbers change. Confirm with the laboratory and WI DNR LabCert / DATCP before you ship a sample.",
        ],
        "excel_wi_labs_before_type_omit": sum(1 for fid, rs in by_fid.items() if str(rs[0]["State"]).upper() == "WI"),
        "bactilab_rows_total": len(bacti_rows),
        "bactilab_omitted_municipal_count": len(bacti_omitted),
    },
    "lab_count": len(all_labs),
    "verified_private_well_count": verified_count,
    "labs": all_labs,
    "bactilab_omitted_names": sorted(x["name"] for x in bacti_omitted),
}
OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print("labs", len(all_labs), "verified", verified_count)
print("excel", len(excel_labs), "bacti_kept", len(bacti_kept), "bacti_omit", len(bacti_omitted), "bacti_only", len(bacti_only))
Path("/tmp/wi-build/meta.json").write_text(json.dumps({
    "health_bacti": [b for b in bacti_kept if classify(b["name"]) != "commercial"],
    "commercial_bacti": [b for b in bacti_kept if classify(b["name"]) == "commercial"],
    "excel_labs": excel_labs,
    "bacti_omitted_count": len(bacti_omitted),
    "bacti_total": len(bacti_rows),
    "verified_count": verified_count,
    "lab_count": len(all_labs),
}, indent=2))
