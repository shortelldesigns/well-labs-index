#!/usr/bin/env python3
"""Build labs/michigan.html from data/labs-mi.json."""
from __future__ import annotations

import html as htmlmod
import json
import re
from pathlib import Path

ROOT = Path("/workspace/well-lab-index")
data = json.loads((ROOT / "data/labs-mi.json").read_text())
labs = data["labs"]

SOURCE_PDF = data["source"]["url"]
CERT_PAGE = data["source"]["certifications_page"]
DW_TESTING = data["source"]["drinking_water_testing"]
DW_LAB = data["source"]["drinking_water_lab"]
EGLE_LAB = data["source"]["egle_lab"]


def esc(s):
    return htmlmod.escape(str(s), quote=True)


def tel_href(phone):
    digits = re.sub(r"\D", "", phone or "")
    if len(digits) == 10:
        return f"+1{digits}"
    if len(digits) == 11 and digits.startswith("1"):
        return f"+{digits}"
    return digits or (phone or "")


def yesno(flag):
    if flag:
        return '<td class="yes">Yes</td>'
    return '<td class="no">—</td>'


def accepts_cell(lab):
    if lab.get("accepts_private_well_samples") == "yes":
        return '<td class="yes">Yes — EGLE homeowner kits</td>'
    return '<td class="unknown">unknown — call first</td>'


def mail_cell(lab):
    v = lab.get("sample_dropoff_or_mail") or "unknown"
    if v == "unknown":
        return '<td class="unknown">unknown</td>'
    return f"<td>{esc(v)}</td>"


def phone_cell(phone):
    if not phone or phone == "unknown":
        return "unknown"
    return f'<a href="tel:{tel_href(phone)}">{esc(phone)}</a>'


def row(lab):
    return (
        f"<tr><td>{esc(lab['name'])}</td><td>{esc(lab.get('city') or 'unknown')}</td>"
        f"<td>{esc(lab.get('street') or lab.get('address') or 'unknown')}</td>"
        f"<td>{phone_cell(lab.get('phone'))}</td>"
        f"{yesno(lab.get('coliform_listed'))}"
        f"{yesno(lab.get('nitrate_listed'))}"
        f"{yesno(lab.get('lead_listed'))}"
        f"{yesno(lab.get('arsenic_listed'))}"
        f"{accepts_cell(lab)}{mail_cell(lab)}</tr>\n"
    )


verified = [l for l in labs if l.get("accepts_private_well_samples") == "yes"]
health = [
    l
    for l in labs
    if l["category"] == "health_department"
    and l.get("accepts_private_well_samples") != "yes"
]
commercial = [
    l
    for l in labs
    if l["category"] in ("commercial", "university")
    and l.get("accepts_private_well_samples") != "yes"
]
# state lab that is not verified would go commercial-ish; EGLE is verified only

health.sort(key=lambda l: (l["name"].lower(), l["city"].lower()))
commercial.sort(key=lambda l: (l["name"].lower(), l["city"].lower()))

omit_n = data["source"].get("omitted_municipal_utility_count", 0)
total_pdf = data["source"].get("pdf_labs_total", 0)
lab_count = data["lab_count"]
ver_count = data["verified_private_well_count"]

health_rows = "".join(row(l) for l in health)
comm_rows = "".join(row(l) for l in commercial)

thead = """        <thead>
          <tr>
            <th>Laboratory</th>
            <th>City</th>
            <th>Address</th>
            <th>Phone</th>
            <th>Coliform / micro</th>
            <th>Nitrate</th>
            <th>Lead</th>
            <th>Arsenic</th>
            <th>Accepts private wells?</th>
            <th>Mail / drop-off</th>
          </tr>
        </thead>
"""

egle = verified[0]
egle_email = egle.get("email") or "kanem4@michigan.gov"
egle_contact = egle.get("contact_name") or "Marlene Kane"

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Michigan Certified Well Labs | Well Labs Index</title>
  <meta name="description" content="{lab_count} Michigan labs from EGLE’s SOM certified list (3/11/2026). EGLE Laboratory Services verified for homeowner kits. Municipal plant labs omitted.">
  <link rel="stylesheet" href="../css/site.css">
</head>
<body>
  <a class="skip" href="#content">Skip to content</a>
  <header class="site">
    <div class="brand">
      <h1><a href="../index.html">Well Labs Index</a></h1>
      <p class="tag">A U.S. directory for private well owners. Test first. Treat second.</p>
    </div>
    <nav class="primary" aria-label="Primary">
      <ul>
        <li><a href="../index.html">Home</a></li>
        <li><a href="../states.html">States</a></li>
        <li><a href="minnesota.html">Minnesota labs</a></li>
        <li><a href="pennsylvania.html">Pennsylvania labs</a></li>
        <li><a href="ohio.html">Ohio labs</a></li>
        <li><a href="wisconsin.html">Wisconsin labs</a></li>
        <li><a href="texas.html">Texas labs</a></li>
        <li><a href="michigan.html" aria-current="page">Michigan labs</a></li>
        <li><a href="../test-private-well.html">How to test</a></li>
        <li><a href="../iron-stains.html">Iron stains</a></li>
        <li><a href="../rotten-egg.html">Rotten egg odor</a></li>
        <li><a href="../about.html">About</a></li>
      </ul>
    </nav>
  </header>
  <main id="content" class="wide">
    <h1 class="page">Michigan labs</h1>
    <p class="lede">One laboratory is independently verified to accept homeowner drinking-water kits: EGLE Laboratory Services in Lansing. The other rows are Michigan commercial and health-department laboratories transcribed from EGLE’s State of Michigan certified laboratories PDF dated 3/11/2026. We have not verified that those other labs currently accept private-well samples. Call before you collect water.</p>
    <p class="meta">Sources retrieved 3 September 2026. Official list: <a href="{esc(SOURCE_PDF)}">Microbiological Laboratory Certifications (PDF)</a>, linked from <a href="{esc(CERT_PAGE)}">EGLE Laboratory Certification Program</a>. Homeowner kits: <a href="{esc(DW_TESTING)}">Drinking water testing</a> · <a href="{esc(DW_LAB)}">EGLE Drinking Water Lab</a> · <a href="{esc(EGLE_LAB)}">Michigan.gov/EGLELab</a>.</p>

    <div class="callout">
      <h2>What we could and could not verify</h2>
      <ul>
        <li>EGLE’s SOM certified-labs PDF lists laboratories certified for the analytes printed (microbiological and chemistry mixed). Appearance on it is not an endorsement and is not, by itself, a statement that the lab takes homeowner / private-well samples.</li>
        <li>{omit_n} municipal water-treatment, filtration, wastewater, water-authority, board-of-public-works/utilities, GLWA, and similar utility plant rows were omitted from this directory ({total_pdf} total PDF labs). That is a directory choice for private well owners, not a statement about their certification. They remain on the official EGLE file.</li>
        <li>Coliform/micro, nitrate, lead, and arsenic columns are Yes when those analytes appear on the official PDF for that lab. Other chemistry may also be certified — ask the lab. Prices are intentionally omitted.</li>
        <li>Always call to confirm address, kit instructions, drop-off or shipping hours, and current certification before you ship a sample.</li>
      </ul>
    </div>

    <h2>Verified for private well owners</h2>
    <div class="card">
      <h3>EGLE Laboratory Services</h3>
      <p>{esc(egle.get('address') or '3350 N MLK Blvd, Lansing, MI 48906')} · <a href="tel:{tel_href(egle.get('phone'))}">{esc(egle.get('phone'))}</a> · <a href="mailto:{esc(egle_email)}">{esc(egle_email)}</a> · contact {esc(egle_contact)}</p>
      <p>On EGLE’s SOM certified list (3/11/2026): Lab ID 0001; certified for total coliform, E. coli, nitrate/nitrite, lead, arsenic, and many other drinking-water analytes. EGLE’s public drinking-water testing page (retrieved 3 September 2026) states the lab accepts homeowner kits; order kits by phone; ship or pick up at 3350 N. Martin Luther King Jr. Blvd, Lansing, MI 48906. Prices are not copied here.</p>
      <p>Source: <a href="{esc(DW_TESTING)}">michigan.gov/egle/public/services/drinking-water-testing</a> · <a href="{esc(DW_LAB)}">EGLE Drinking Water Lab</a> · SOM certified-labs PDF.</p>
    </div>

    <h2>Local health department laboratories on the EGLE list</h2>
    <p>Except for EGLE Laboratory Services above, we have not verified that these laboratories currently accept a sample you collect yourself. Call first. Mail vs. drop-off is unknown on the certification PDF.</p>
    <div class="table-wrap">
      <table>
        <caption>{len(health)} local / district health laboratories. Source: EGLE SOM certified labs PDF, 3/11/2026.</caption>
{thead}        <tbody>
{health_rows}        </tbody>
      </table>
    </div>

    <h2>Commercial laboratories in Michigan on the EGLE list</h2>
    <p>Call to confirm they still hold certification, that they accept a private-well sample, and which analytes they can run. Mail vs. drop-off is unknown unless noted. {ver_count} of {lab_count} tabulated rows is verified for homeowner / private-well kits (EGLE, above).</p>
    <div class="table-wrap">
      <table>
        <caption>{len(commercial)} commercial laboratories (municipal utility rows omitted). Source: EGLE SOM certified labs PDF, 3/11/2026.</caption>
{thead}        <tbody>
{comm_rows}        </tbody>
      </table>
    </div>

    <h2>Official tools if you need more labs</h2>
    <ul>
      <li><a href="{esc(CERT_PAGE)}">EGLE Laboratory Certification Program</a> — full certified-lab PDFs, including chemistry and utility plant labs we omitted.</li>
      <li><a href="{esc(DW_TESTING)}">EGLE drinking water testing for the public</a> — homeowner kit guidance for the state lab.</li>
      <li><a href="{esc(SOURCE_PDF)}">Microbiological Laboratory Certifications (PDF)</a> — official SOM list used for this page (footer date 3/11/2026).</li>
    </ul>
  </main>
  <footer class="site">
    <div class="inner">
      <p><strong>Well Labs Index</strong> is a project by Shortell Designs. Last updated 3 September 2026 (US/Pacific).</p>
      <p><a href="../about.html">Methodology and disclosure</a> · <a href="../states.html">State directory</a></p>
      <div class="disclaimer">
        <p>This site is not a government agency and does not certify laboratories. Listings are transcribed from official state and federal sources cited on each page. Accreditation, phone numbers, and sample-acceptance policies change. Confirm with the laboratory and the state certification program before you ship a sample.</p>
        <p>Private wells are not regulated under the federal Safe Drinking Water Act in the way public water systems are. You are responsible for testing. This site is educational, not medical, legal, or engineering advice. We may earn a commission on future product or service links; there are no live affiliate links on this version.</p>
      </div>
    </div>
  </footer>
</body>
</html>
"""

out = ROOT / "labs/michigan.html"
out.write_text(page)
print(f"wrote {out} ({lab_count} labs, {len(health)} health, {len(commercial)} commercial)")
