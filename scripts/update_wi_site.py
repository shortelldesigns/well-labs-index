#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path("/workspace/well-lab-index")

WI_ROOT = '        <li><a href="labs/wisconsin.html">Wisconsin labs</a></li>\n'
WI_LAB = '        <li><a href="wisconsin.html">Wisconsin labs</a></li>\n'

def inject_after_ohio_root(text):
    if "labs/wisconsin.html" in text:
        return text, False
    # insert after ohio labs li (with or without aria-current)
    pat = re.compile(r'(        <li><a href="labs/ohio\.html"(?: aria-current="page")?>Ohio labs</a></li>\n)')
    m = pat.search(text)
    if not m:
        raise SystemExit("root ohio li not found")
    return text[: m.end()] + WI_ROOT + text[m.end() :], True

def inject_after_ohio_lab(text):
    if re.search(r'href="wisconsin\.html"', text):
        return text, False
    pat = re.compile(r'(        <li><a href="ohio\.html"(?: aria-current="page")?>Ohio labs</a></li>\n)')
    m = pat.search(text)
    if not m:
        raise SystemExit("lab ohio li not found")
    return text[: m.end()] + WI_LAB + text[m.end() :], True

root_pages = [
    "index.html", "states.html", "about.html",
    "test-private-well.html", "iron-stains.html", "rotten-egg.html",
]
for name in root_pages:
    p = ROOT / name
    t, changed = inject_after_ohio_root(p.read_text())
    if changed:
        p.write_text(t)
        print("nav root", name)
    else:
        print("nav root already", name)

for name in ["minnesota.html", "pennsylvania.html", "ohio.html", "wisconsin.html"]:
    p = ROOT / "labs" / name
    t = p.read_text()
    if name == "wisconsin.html":
        print("nav lab wisconsin ok")
        continue
    t2, changed = inject_after_ohio_lab(t)
    if changed:
        p.write_text(t2)
        print("nav lab", name)
    else:
        print("nav lab already", name)

# index content updates
idx = ROOT / "index.html"
t = idx.read_text()
t = t.replace(
    'content="Find a state-certified lab that will test a private well, then match treatment to the report. Minnesota, Pennsylvania, and Ohio live. No invented labs."',
    'content="Find a state-certified lab that will test a private well, then match treatment to the report. Minnesota, Pennsylvania, Ohio, and Wisconsin live. No invented labs."',
)
if "Wisconsin —" not in t:
    ohio_card_end = '''        <a class="btn secondary" href="labs/ohio.html">Open Ohio labs</a>
      </div>
    </div>'''
    wi_card = '''        <a class="btn secondary" href="labs/ohio.html">Open Ohio labs</a>
      </div>
      <div class="card">
        <h3><a href="labs/wisconsin.html">Wisconsin — 74 labs listed, 2 verified for private wells</a></h3>
        <p>Wisconsin State Laboratory of Hygiene and UW–Stevens Point WEAL are confirmed for homeowner / private-well testing. Other rows are from WI DNR’s January 2026 chemistry list and DATCP BactiLab. Call before you ship. Municipal plant labs were omitted.</p>
        <a class="btn secondary" href="labs/wisconsin.html">Open Wisconsin labs</a>
      </div>
    </div>'''
    if ohio_card_end not in t:
        raise SystemExit("ohio card end not found")
    t = t.replace(ohio_card_end, wi_card, 1)
t = t.replace(
    "All states — Minnesota, Pennsylvania, and Ohio live; others coming soon",
    "All states — Minnesota, Pennsylvania, Ohio, and Wisconsin live; others coming soon",
)
old_meta = "Directory first published 29 August 2026. Minnesota listings transcribed from the Minnesota Department of Health July 2026 private-well lab map. Pennsylvania listings from a PA DEP bacteriology accreditation report dated 13 June 2024, plus Penn State’s public drinking-water program. Ohio listings from Ohio EPA’s Combined Lab List dated August 2026, rev. 8/13/2026, plus Mahoning County Public Health’s laboratory-services page."
new_meta = "Directory first published 29 August 2026; Wisconsin added 1 September 2026. Minnesota listings transcribed from the Minnesota Department of Health July 2026 private-well lab map. Pennsylvania listings from a PA DEP bacteriology accreditation report dated 13 June 2024, plus Penn State’s public drinking-water program. Ohio listings from Ohio EPA’s Combined Lab List dated August 2026, rev. 8/13/2026, plus Mahoning County Public Health’s laboratory-services page. Wisconsin listings from WI DNR’s January 2026 drinking-water chemistry Excel (NR 809/NR 812) and the DATCP/DNR BactiLab portal, plus WSLH and WEAL public pages."
if old_meta in t:
    t = t.replace(old_meta, new_meta)
t = t.replace("Last updated 29 August 2026 (US/Pacific).", "Last updated 1 September 2026 (US/Pacific).")
idx.write_text(t)
print("index content ok")

st = ROOT / "states.html"
t = st.read_text()
t = t.replace(
    'content="State-certified laboratories for private well owners. Minnesota, Pennsylvania, and Ohio are live; other states when an official list can be transcribed."',
    'content="State-certified laboratories for private well owners. Minnesota, Pennsylvania, Ohio, and Wisconsin are live; other states when an official list can be transcribed."',
)
t = t.replace("Last updated 29 August 2026.", "Last updated 1 September 2026.")
t = t.replace("Last updated 29 August 2026 (US/Pacific).", "Last updated 1 September 2026 (US/Pacific).")
if 'href="labs/wisconsin.html"><strong>Wisconsin</strong>' not in t:
    old = '''      <li><span><a href="labs/ohio.html"><strong>Ohio</strong></a> — Mahoning County verified; 28 other Ohio labs from Ohio EPA’s August 2026 list</span> <span class="badge">Live</span></li>
      <li><span>Alabama through Wyoming (except MN, PA, and OH)</span> <span class="badge soon">Coming soon</span></li>'''
    new = '''      <li><span><a href="labs/ohio.html"><strong>Ohio</strong></a> — Mahoning County verified; 28 other Ohio labs from Ohio EPA’s August 2026 list</span> <span class="badge">Live</span></li>
      <li><span><a href="labs/wisconsin.html"><strong>Wisconsin</strong></a> — WSLH and WEAL verified; chemistry from DNR January 2026 list plus DATCP BactiLab</span> <span class="badge">Live</span></li>
      <li><span>Alabama through Wyoming (except MN, PA, OH, and WI)</span> <span class="badge soon">Coming soon</span></li>'''
    if old not in t:
        raise SystemExit("states list pattern missing")
    t = t.replace(old, new, 1)
st.write_text(t)
print("states ok")

for name in ["about.html", "test-private-well.html", "iron-stains.html", "rotten-egg.html"]:
    p = ROOT / name
    t = p.read_text()
    nt = t.replace("Last updated 29 August 2026 (US/Pacific).", "Last updated 1 September 2026 (US/Pacific).")
    if nt != t:
        p.write_text(nt)
        print("footer", name)

for name in ["minnesota.html", "pennsylvania.html", "ohio.html"]:
    p = ROOT / "labs" / name
    t = p.read_text()
    nt = t.replace("Last updated 29 August 2026 (US/Pacific).", "Last updated 1 September 2026 (US/Pacific).")
    if nt != t:
        p.write_text(nt)
        print("footer labs/"+name)

sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://shortelldesigns.github.io/well-labs-index/</loc><lastmod>2026-09-01</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>
  <url><loc>https://shortelldesigns.github.io/well-labs-index/test-private-well.html</loc><lastmod>2026-09-01</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>
  <url><loc>https://shortelldesigns.github.io/well-labs-index/labs/minnesota.html</loc><lastmod>2026-09-01</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>
  <url><loc>https://shortelldesigns.github.io/well-labs-index/labs/pennsylvania.html</loc><lastmod>2026-09-01</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>
  <url><loc>https://shortelldesigns.github.io/well-labs-index/labs/ohio.html</loc><lastmod>2026-09-01</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>
  <url><loc>https://shortelldesigns.github.io/well-labs-index/labs/wisconsin.html</loc><lastmod>2026-09-01</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>
  <url><loc>https://shortelldesigns.github.io/well-labs-index/states.html</loc><lastmod>2026-09-01</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>
  <url><loc>https://shortelldesigns.github.io/well-labs-index/iron-stains.html</loc><lastmod>2026-09-01</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>
  <url><loc>https://shortelldesigns.github.io/well-labs-index/rotten-egg.html</loc><lastmod>2026-09-01</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>
  <url><loc>https://shortelldesigns.github.io/well-labs-index/about.html</loc><lastmod>2026-09-01</lastmod><changefreq>yearly</changefreq><priority>0.4</priority></url>
</urlset>
'''
(ROOT / "sitemap.xml").write_text(sitemap)
print("sitemap ok")

sources = ROOT / "SOURCES.md"
s = sources.read_text()
if "DWLabs012126" not in s:
    append = '''

## Wisconsin (1 September 2026)

Retrieve date: **1 September 2026** (US/Pacific).

### Succeeded

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| WI DNR certified lab lists | https://dnr.wisconsin.gov/topic/labCert/certified-lab-lists | Retrieved 1 September 2026 | Lists “Accredited Laboratories - January 2026” / drinking water certified labs — chemistry (NR 809 and NR 812); also “Drinking Water Laboratories for Homeowners”. |
| WI DNR DW chemistry Excel | https://dnr.wisconsin.gov/sites/default/files/topic/LabCert/DWLabs012126.xlsx | January 2026 (filename DWLabs012126.xlsx → 21 Jan 2026) | Archived at `data/sources/wi-dw-labs-jan-2026.xlsx`. Columns: FID, Lab Name, Lab Type, Parameter, State, County, City, Phone. WI-only rows kept; out-of-state (often PFAS) omitted. Municipal / PWS / industrial Lab Types omitted. |
| DATCP/DNR BactiLab portal | https://apps.dnr.wi.gov/dwsportalpub/BactiLab | Live table retrieved 1 September 2026 | curl archive: `data/sources/wi-bactilab-2026-09-01.html`. DATCP-certified coliform (enzyme substrate). Municipal utilities / WWTP / sanitary districts omitted from directory. |
| WI DNR private well testing | https://dnr.wisconsin.gov/topic/Wells/privateWellTest.html | Retrieved 1 September 2026 | Annual bacteria + nitrate; arsenic every 5 years (yearly Outagamie, Winnebago, Brown). |
| WSLH public health tests for citizens | https://www.slh.wisc.edu/environmental/water/public-health-tests-available-to-wisconsin-citizens/ | Retrieved / verified 1 September 2026 | Homeowner Package / public health tests for Wisconsin citizens. Used to verify private-well acceptance only. |
| WSLH kit ordering / prices page | https://www.slh.wisc.edu/environmental/water/public-environmental-and-water-testing-prices/ | Retrieved / verified 1 September 2026 | Kit phones (800) 442-4618 / (608) 224-6202; address 2601 Agriculture Drive; drop-off Mon–Fri 7:45 AM–4:30 PM. **Prices not copied to the site.** |
| WEAL / UWSP well water testing | https://www.uwsp.edu/center-for-watershed-science-and-education/well-water-testing/ | Retrieved / verified 1 September 2026 | Serves private well owners; kits via county Extension; weal@uwsp.edu; (715) 346-3209. |

### Failed or incomplete (Wisconsin)

| Attempt | URL | What happened | What we did instead |
| --- | --- | --- | --- |
| (none blocking) | — | Excel and BactiLab HTML both retrieved successfully for this build | — |

### Not used as WI lab sources

- Third-party directories.
- Invented phone numbers or private-well acceptance claims beyond WSLH and WEAL public pages.
'''
    sources.write_text(s.rstrip() + append + "\n")
    print("SOURCES appended")
else:
    print("SOURCES already")

readme = ROOT / "README.md"
r = readme.read_text()
r2 = r.replace("states.html                MN + PA + OH live; others coming soon",
               "states.html                MN + PA + OH + WI live; others coming soon")
if "labs/wisconsin.html" not in r2:
    r2 = r2.replace("labs/ohio.html\n", "labs/ohio.html\nlabs/wisconsin.html\n")
if "data/labs-wi.json" not in r2:
    r2 = r2.replace("data/labs-oh.json\n", "data/labs-oh.json\ndata/labs-wi.json\n")
if r2 != r:
    readme.write_text(r2)
    print("README updated")
else:
    print("README ok/unchanged")
print("DONE")
