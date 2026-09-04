#!/usr/bin/env python3
"""Wire Michigan into nav, homepage, states, sitemap, SOURCES, README, footers."""
from pathlib import Path

ROOT = Path("/workspace/well-lab-index")

NAV_OLD_ROOT = '''        <li><a href="labs/texas.html">Texas labs</a></li>
        <li><a href="test-private-well.html">How to test</a></li>'''
NAV_NEW_ROOT = '''        <li><a href="labs/texas.html">Texas labs</a></li>
        <li><a href="labs/michigan.html">Michigan labs</a></li>
        <li><a href="test-private-well.html">How to test</a></li>'''

NAV_OLD_LABS = '''        <li><a href="texas.html">Texas labs</a></li>
        <li><a href="../test-private-well.html">How to test</a></li>'''
NAV_NEW_LABS = '''        <li><a href="texas.html">Texas labs</a></li>
        <li><a href="michigan.html">Michigan labs</a></li>
        <li><a href="../test-private-well.html">How to test</a></li>'''

# texas.html has aria-current on Texas — still needs Michigan inserted after Texas
NAV_OLD_TEXAS_PAGE = '''        <li><a href="texas.html" aria-current="page">Texas labs</a></li>
        <li><a href="../test-private-well.html">How to test</a></li>'''
NAV_NEW_TEXAS_PAGE = '''        <li><a href="texas.html" aria-current="page">Texas labs</a></li>
        <li><a href="michigan.html">Michigan labs</a></li>
        <li><a href="../test-private-well.html">How to test</a></li>'''

FOOTER_OLD = "Last updated 2 September 2026 (US/Pacific)."
FOOTER_NEW = "Last updated 3 September 2026 (US/Pacific)."

html_files = list(ROOT.glob("*.html")) + list((ROOT / "labs").glob("*.html"))

for path in html_files:
    text = path.read_text()
    orig = text
    if path.name == "michigan.html":
        # already has Michigan nav + footer
        pass
    else:
        if "labs/michigan.html" not in text and 'href="michigan.html"' not in text:
            if path.name == "texas.html" and NAV_OLD_TEXAS_PAGE in text:
                text = text.replace(NAV_OLD_TEXAS_PAGE, NAV_NEW_TEXAS_PAGE)
            elif path.parent.name == "labs":
                if NAV_OLD_LABS in text:
                    text = text.replace(NAV_OLD_LABS, NAV_NEW_LABS)
            else:
                if NAV_OLD_ROOT in text:
                    text = text.replace(NAV_OLD_ROOT, NAV_NEW_ROOT)
        text = text.replace(FOOTER_OLD, FOOTER_NEW)
        # states.html also has "Last updated 2 September 2026." without PT tag
        text = text.replace("Last updated 2 September 2026.", "Last updated 3 September 2026.")
    if text != orig:
        path.write_text(text)
        print("updated", path.relative_to(ROOT))

# index.html homepage cards + meta
index = ROOT / "index.html"
t = index.read_text()
card = '''      <div class="card">
        <h3><a href="labs/michigan.html">Michigan — 47 labs listed, 1 verified for private wells</a></h3>
        <p>EGLE Laboratory Services is confirmed for homeowner kits (ship or pickup). Other rows are commercial and health-department labs from EGLE’s SOM certified list dated 3/11/2026. Call before you ship. Municipal plant labs were omitted.</p>
        <a class="btn secondary" href="labs/michigan.html">Open Michigan labs</a>
      </div>
'''
marker = '''        <a class="btn secondary" href="labs/texas.html">Open Texas labs</a>
      </div>
    </div>'''
if marker in t and "Open Michigan labs" not in t:
    t = t.replace(
        marker,
        '''        <a class="btn secondary" href="labs/texas.html">Open Texas labs</a>
      </div>
'''
        + card
        + "    </div>",
    )
t = t.replace(
    "Find a state-certified lab that will test a private well, then match treatment to the report. Minnesota, Pennsylvania, Ohio, Wisconsin, and Texas live. No invented labs.",
    "Find a state-certified lab that will test a private well, then match treatment to the report. Minnesota, Pennsylvania, Ohio, Wisconsin, Texas, and Michigan live. No invented labs.",
)
t = t.replace(
    "All states — Minnesota, Pennsylvania, Ohio, Wisconsin, and Texas live; others coming soon",
    "All states — Minnesota, Pennsylvania, Ohio, Wisconsin, Texas, and Michigan live; others coming soon",
)
t = t.replace(
    "Directory first published 29 August 2026; Wisconsin added 1 September 2026; Texas added 2 September 2026.",
    "Directory first published 29 August 2026; Wisconsin added 1 September 2026; Texas added 2 September 2026; Michigan added 3 September 2026.",
)
if "Michigan listings from EGLE" not in t:
    t = t.replace(
        "Texas listings from TCEQ’s Public Water System Lab Map Table dated 03/26/2026, plus LCRA’s residential water testing page.",
        "Texas listings from TCEQ’s Public Water System Lab Map Table dated 03/26/2026, plus LCRA’s residential water testing page. Michigan listings from EGLE’s SOM certified laboratories PDF dated 3/11/2026, plus EGLE’s drinking-water testing page for homeowner kits.",
    )
# ensure footer on index
t = t.replace(FOOTER_OLD, FOOTER_NEW)
index.write_text(t)
print("homepage done")

# states.html
states = ROOT / "states.html"
s = states.read_text()
s = s.replace(
    "State-certified laboratories for private well owners. Minnesota, Pennsylvania, Ohio, Wisconsin, and Texas are live; other states when an official list can be transcribed.",
    "State-certified laboratories for private well owners. Minnesota, Pennsylvania, Ohio, Wisconsin, Texas, and Michigan are live; other states when an official list can be transcribed.",
)
s = s.replace("Last updated 2 September 2026.", "Last updated 3 September 2026.")
s = s.replace(FOOTER_OLD, FOOTER_NEW)
if "<strong>Michigan</strong>" not in s:
    s = s.replace(
        '''      <li><span><a href="labs/texas.html"><strong>Texas</strong></a> — LCRA verified; commercial and health labs from TCEQ PWS Lab Map Table (03/26/2026)</span> <span class="badge">Live</span></li>
      <li><span>Alabama through Wyoming (except MN, PA, OH, WI, and TX)</span> <span class="badge soon">Coming soon</span></li>''',
        '''      <li><span><a href="labs/texas.html"><strong>Texas</strong></a> — LCRA verified; commercial and health labs from TCEQ PWS Lab Map Table (03/26/2026)</span> <span class="badge">Live</span></li>
      <li><span><a href="labs/michigan.html"><strong>Michigan</strong></a> — EGLE Laboratory Services verified; commercial and health labs from SOM certified list (3/11/2026)</span> <span class="badge">Live</span></li>
      <li><span>Alabama through Wyoming (except MN, PA, OH, WI, TX, and MI)</span> <span class="badge soon">Coming soon</span></li>''',
    )
states.write_text(s)
print("states done")

# sitemap
sm = ROOT / "sitemap.xml"
sx = sm.read_text()
sx = sx.replace(">2026-09-02<", ">2026-09-03<")
if "labs/michigan.html" not in sx:
    sx = sx.replace(
        '''  <url><loc>https://shortelldesigns.github.io/well-labs-index/labs/texas.html</loc><lastmod>2026-09-03</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>
''',
        '''  <url><loc>https://shortelldesigns.github.io/well-labs-index/labs/texas.html</loc><lastmod>2026-09-03</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>
  <url><loc>https://shortelldesigns.github.io/well-labs-index/labs/michigan.html</loc><lastmod>2026-09-03</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>
''',
    )
sm.write_text(sx)
print("sitemap done")

# SOURCES.md append
sources = ROOT / "SOURCES.md"
st = sources.read_text()
if "Michigan (3 September 2026)" not in st:
    st += """

## Michigan (3 September 2026)

Retrieve date: **3 September 2026** (US/Pacific).

### Succeeded

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| EGLE Microbiological Laboratory Certifications (PDF) | https://www.michigan.gov/egle/-/media/Project/Websites/egle/Documents/Programs/RRD/Lab/Microbiological-Laboratory-Certifications.pdf | Footer: SOM Certified Labs - Chemistry 3/11/2026 | Archived at `data/sources/mi-microbiological-lab-certifications.pdf`. 165 labs; Lab ID, address, contact, certified analytes (micro + chemistry). |
| EGLE Laboratory Certification Program | https://www.michigan.gov/egle/about/organization/remediation-and-redevelopment/laboratory/certifications | Retrieved 3 September 2026 | Links certified-lab PDFs. |
| EGLE drinking water testing (public / homeowner) | https://www.michigan.gov/egle/public/services/drinking-water-testing | Retrieved 3 September 2026 | Verifies EGLE Lab accepts homeowner kits; order by phone; ship or pickup. |
| EGLE Drinking Water Lab | https://www.michigan.gov/egle/about/organization/remediation-and-redevelopment/laboratory/drinking-water | Retrieved 3 September 2026 | 3350 N MLK Blvd / Martin Luther King Jr. Blvd, Lansing, MI 48906; (517) 335-8184. |
| Michigan.gov/EGLELab | https://www.michigan.gov/eglelab | Retrieved 3 September 2026 | Short URL cited on the certified-labs PDF. |

### Failed or incomplete (Michigan)

| Attempt | URL | What happened | What we did instead |
| --- | --- | --- | --- |
| Bare curl of EGLE PDF | same PDF URL | Akamai blocks bare curl | Re-download with Chrome User-Agent + Referer from certifications page (PDF already archived in repo). |

### Not used as MI lab sources

- Third-party directories.
- Filter-review or affiliate sites.
- Invented private-well acceptance claims beyond EGLE’s public drinking-water testing page.
"""
    sources.write_text(st)
    print("SOURCES appended")

# README
readme = ROOT / "README.md"
if readme.exists():
    r = readme.read_text()
    r2 = r
    for old, new in [
        ("Minnesota, Pennsylvania, Ohio, Wisconsin, and Texas", "Minnesota, Pennsylvania, Ohio, Wisconsin, Texas, and Michigan"),
        ("MN, PA, OH, WI, and TX", "MN, PA, OH, WI, TX, and MI"),
        ("MN/PA/OH/WI/TX", "MN/PA/OH/WI/TX/MI"),
        ("MN + PA + OH + WI live", "MN + PA + OH + WI + TX + MI live"),
    ]:
        r2 = r2.replace(old, new)
    if "labs/michigan.html" not in r2:
        r2 = r2.replace(
            "labs/texas.html) — TCEQ PWS Lab Map Table (03/26/2026); LCRA verified",
            "labs/texas.html) — TCEQ PWS Lab Map Table (03/26/2026); LCRA verified\n- [Michigan labs](labs/michigan.html) — EGLE SOM certified list (3/11/2026); EGLE Lab verified",
            1,
        )
        # also fix layout list if present as bare path
        if "labs/texas.html\n" in r2 and "labs/michigan.html" not in r2.split("Layout")[1] if "Layout" in r2 else True:
            r2 = r2.replace(
                "labs/wisconsin.html\n- [Texas labs](labs/texas.html)",
                "labs/wisconsin.html\nlabs/texas.html\nlabs/michigan.html\n- [Texas labs](labs/texas.html)",
                1,
            )
    if r2 != r:
        readme.write_text(r2)
        print("README updated")

print("done")
