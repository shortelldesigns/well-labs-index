#!/usr/bin/env python3
"""Wire Texas into nav, homepage, states, sitemap, SOURCES, README, footers."""
from pathlib import Path
import re

ROOT = Path("/workspace/well-lab-index")

# Nav: insert Texas after Wisconsin in every HTML page
NAV_OLD_ROOT = '''        <li><a href="labs/wisconsin.html">Wisconsin labs</a></li>
        <li><a href="test-private-well.html">How to test</a></li>'''
NAV_NEW_ROOT = '''        <li><a href="labs/wisconsin.html">Wisconsin labs</a></li>
        <li><a href="labs/texas.html">Texas labs</a></li>
        <li><a href="test-private-well.html">How to test</a></li>'''

NAV_OLD_LABS = '''        <li><a href="wisconsin.html">Wisconsin labs</a></li>
        <li><a href="../test-private-well.html">How to test</a></li>'''
NAV_NEW_LABS = '''        <li><a href="wisconsin.html">Wisconsin labs</a></li>
        <li><a href="texas.html">Texas labs</a></li>
        <li><a href="../test-private-well.html">How to test</a></li>'''

# For texas.html itself already has aria-current Texas — skip double insert
FOOTER_OLD = "Last updated 1 September 2026 (US/Pacific)."
FOOTER_NEW = "Last updated 2 September 2026 (US/Pacific)."

html_files = list(ROOT.glob("*.html")) + list((ROOT / "labs").glob("*.html"))

for path in html_files:
    text = path.read_text()
    orig = text
    if path.name == "texas.html":
        # already has texas nav; just ensure footer
        text = text.replace(FOOTER_OLD, FOOTER_NEW)
    else:
        if "labs/texas.html" not in text and 'href="texas.html"' not in text:
            if path.parent.name == "labs":
                if NAV_OLD_LABS in text:
                    text = text.replace(NAV_OLD_LABS, NAV_NEW_LABS)
            else:
                if NAV_OLD_ROOT in text:
                    text = text.replace(NAV_OLD_ROOT, NAV_NEW_ROOT)
        text = text.replace(FOOTER_OLD, FOOTER_NEW)
    if text != orig:
        path.write_text(text)
        print("updated", path.relative_to(ROOT))

# index.html homepage cards + meta
index = ROOT / "index.html"
t = index.read_text()
if "labs/texas.html" not in t or "Texas —" not in t:
    # expand cards class if needed — already "cards two"
    card = '''      <div class="card">
        <h3><a href="labs/texas.html">Texas — 49 labs listed, 1 verified for private wells</a></h3>
        <p>LCRA Environmental Laboratory Services is confirmed for residential / private water-supply testing. Other rows are commercial and health-department labs from TCEQ’s PWS Lab Map Table (updated 03/26/2026). Call before you ship. Municipal utility labs were omitted.</p>
        <a class="btn secondary" href="labs/texas.html">Open Texas labs</a>
      </div>
'''
    # insert after Wisconsin card closing
    marker = '''        <a class="btn secondary" href="labs/wisconsin.html">Open Wisconsin labs</a>
      </div>
    </div>'''
    if marker in t and "Open Texas labs" not in t:
        t = t.replace(
            marker,
            '''        <a class="btn secondary" href="labs/wisconsin.html">Open Wisconsin labs</a>
      </div>
''' + card + "    </div>",
        )
t = t.replace(
    "Find a state-certified lab that will test a private well, then match treatment to the report. Minnesota, Pennsylvania, Ohio, and Wisconsin live. No invented labs.",
    "Find a state-certified lab that will test a private well, then match treatment to the report. Minnesota, Pennsylvania, Ohio, Wisconsin, and Texas live. No invented labs.",
)
t = t.replace(
    "All states — Minnesota, Pennsylvania, Ohio, and Wisconsin live; others coming soon",
    "All states — Minnesota, Pennsylvania, Ohio, Wisconsin, and Texas live; others coming soon",
)
t = t.replace(
    "Directory first published 29 August 2026; Wisconsin added 1 September 2026.",
    "Directory first published 29 August 2026; Wisconsin added 1 September 2026; Texas added 2 September 2026.",
)
if "Texas listings from TCEQ" not in t:
    t = t.replace(
        "Wisconsin listings from WI DNR’s January 2026 drinking-water chemistry Excel (NR 809/NR 812) and the DATCP/DNR BactiLab portal, plus WSLH and WEAL public pages.",
        "Wisconsin listings from WI DNR’s January 2026 drinking-water chemistry Excel (NR 809/NR 812) and the DATCP/DNR BactiLab portal, plus WSLH and WEAL public pages. Texas listings from TCEQ’s Public Water System Lab Map Table dated 03/26/2026, plus LCRA’s residential water testing page.",
    )
index.write_text(t)
print("homepage done")

# states.html
states = ROOT / "states.html"
s = states.read_text()
s = s.replace(
    "State-certified laboratories for private well owners. Minnesota, Pennsylvania, Ohio, and Wisconsin are live; other states when an official list can be transcribed.",
    "State-certified laboratories for private well owners. Minnesota, Pennsylvania, Ohio, Wisconsin, and Texas are live; other states when an official list can be transcribed.",
)
s = s.replace("Last updated 1 September 2026.", "Last updated 2 September 2026.")
if "labs/texas.html" not in s or "<strong>Texas</strong>" not in s:
    s = s.replace(
        '''      <li><span><a href="labs/wisconsin.html"><strong>Wisconsin</strong></a> — WSLH and WEAL verified; chemistry from DNR January 2026 list plus DATCP BactiLab</span> <span class="badge">Live</span></li>
      <li><span>Alabama through Wyoming (except MN, PA, OH, and WI)</span> <span class="badge soon">Coming soon</span></li>''',
        '''      <li><span><a href="labs/wisconsin.html"><strong>Wisconsin</strong></a> — WSLH and WEAL verified; chemistry from DNR January 2026 list plus DATCP BactiLab</span> <span class="badge">Live</span></li>
      <li><span><a href="labs/texas.html"><strong>Texas</strong></a> — LCRA verified; commercial and health labs from TCEQ PWS Lab Map Table (03/26/2026)</span> <span class="badge">Live</span></li>
      <li><span>Alabama through Wyoming (except MN, PA, OH, WI, and TX)</span> <span class="badge soon">Coming soon</span></li>''',
    )
states.write_text(s)
print("states done")

# sitemap
sm = ROOT / "sitemap.xml"
sx = sm.read_text()
sx = sx.replace(">2026-09-01<", ">2026-09-02<")
if "labs/texas.html" not in sx:
    sx = sx.replace(
        '''  <url><loc>https://shortelldesigns.github.io/well-labs-index/labs/wisconsin.html</loc><lastmod>2026-09-02</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>
''',
        '''  <url><loc>https://shortelldesigns.github.io/well-labs-index/labs/wisconsin.html</loc><lastmod>2026-09-02</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>
  <url><loc>https://shortelldesigns.github.io/well-labs-index/labs/texas.html</loc><lastmod>2026-09-02</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>
''',
    )
sm.write_text(sx)
print("sitemap done")

# SOURCES.md append
sources = ROOT / "SOURCES.md"
st = sources.read_text()
if "Texas (2 September 2026)" not in st:
    st += """

## Texas (2 September 2026)

Retrieve date: **2 September 2026** (US/Pacific).

### Succeeded

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| TCEQ PWS Lab Map Table (PDF) | https://www.tceq.texas.gov/downloads/drinking-water/quality-assurance/pws-lab-map-table.pdf | Updated 03/26/2026 | Archived at `data/sources/tx-pws-lab-map-table-2026-03-26.pdf`. 80 labs; microbial / LCR / WQP flags. |
| TCEQ PWS Lab Map Table (Excel) | https://www.tceq.texas.gov/downloads/drinking-water/quality-assurance/pws-lab-map-table.xlsx | Updated 03/26/2026 | Archived at `data/sources/tx-pws-lab-map-table-2026-03-26.xlsx`. Parsed sheet `Public Labs`. |
| TCEQ PWSS program page | https://www.tceq.texas.gov/drinkingwater/pwss.html | Retrieved 2 September 2026 | Links map + table; NELAP drinking-water public labs. |
| TCEQ steps to locate accredited lab | https://www.tceq.texas.gov/assistance/resources/steps-to-locate-an-accredited-laboratory | Retrieved 2 September 2026 | NELAP LAMS search instructions. |
| TWDB Sampling a Private Water Well | https://www.twdb.texas.gov/groundwater/data/privwwsamp.asp | Retrieved 2 September 2026 | Points private-well owners to the same TCEQ map/table; mentions LCRA typical analyses. Archived `data/sources/tx-twdb-private-well-2026-09-02.html`. |
| LCRA residential water supply testing | https://www.lcra.org/services/els/residential-water-testing/ | Retrieved 2 September 2026 | Verifies private/residential testing, kits, mail/drop-off. Archived `data/sources/tx-lcra-residential-2026-09-02.html`. Prices not copied. |

### Failed or incomplete (Texas)

| Attempt | URL | What happened | What we did instead |
| --- | --- | --- | --- |
| TCEQ dwapprovedlabs.pdf | https://www.tceq.texas.gov/downloads/drinking-water/quality-assurance/dwapprovedlabs.pdf | Not required for this build once PWS Lab Map Table Excel parsed cleanly | Used PWS Lab Map Table as primary directory source. |
| Interactive NELAP map scrape | TCEQ drinking-water labs map | Not a static extractable list | Linked official map/table and NELAP search steps. |

### Not used as TX lab sources

- Third-party directories.
- Filter-review or affiliate sites.
- Invented private-well acceptance claims beyond LCRA’s public residential page.
"""
    sources.write_text(st)
    print("SOURCES appended")

# README live states
readme = ROOT / "README.md"
if readme.exists():
    r = readme.read_text()
    r2 = r
    for old, new in [
        ("Minnesota, Pennsylvania, Ohio, and Wisconsin", "Minnesota, Pennsylvania, Ohio, Wisconsin, and Texas"),
        ("MN, PA, OH, and WI", "MN, PA, OH, WI, and TX"),
        ("MN/PA/OH/WI", "MN/PA/OH/WI/TX"),
    ]:
        r2 = r2.replace(old, new)
    if "texas.html" not in r2 and "Texas" in r2:
        pass
    if "labs/texas.html" not in r2:
        # try add a bullet if there's a live list
        if "labs/wisconsin.html" in r2:
            r2 = r2.replace("labs/wisconsin.html", "labs/wisconsin.html")
            if "- Texas" not in r2 and "* Texas" not in r2:
                r2 = r2.replace(
                    "wisconsin.html",
                    "wisconsin.html\n- [Texas labs](labs/texas.html) — TCEQ PWS Lab Map Table (03/26/2026); LCRA verified",
                    1,
                )
    if r2 != r:
        readme.write_text(r2)
        print("README updated")

print("done")
