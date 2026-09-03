#!/usr/bin/env python3
import html as htmlmod
import json
import re
from pathlib import Path

ROOT = Path("/workspace/well-lab-index")
data = json.loads((ROOT / "data/labs-tx.json").read_text())
labs = data["labs"]


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
        return '<td class="yes">Yes — LCRA residential testing page</td>'
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
        f"<td>{esc(lab.get('county') or 'unknown')}</td>"
        f"<td>{esc(lab.get('street') or lab.get('address') or 'unknown')}</td>"
        f"<td>{phone_cell(lab.get('phone'))}</td>"
        f"{yesno(lab.get('coliform_listed'))}"
        f"{yesno(lab.get('lcr_listed'))}"
        f"{yesno(lab.get('wqp_listed'))}"
        f"{accepts_cell(lab)}{mail_cell(lab)}</tr>\n"
    )


verified = [l for l in labs if l.get("accepts_private_well_samples") == "yes"]
health = [l for l in labs if l["category"] == "health_department"]
university = [l for l in labs if l["category"] == "university"]
commercial = [l for l in labs if l["category"] == "commercial"]
# LCRA is river_authority_residential — shown in verified card, also in its own note; include in commercial-ish table? Better separate: only show in verified + not duplicate in commercial tables. Exclude verified from tables.
health = [l for l in health if l.get("accepts_private_well_samples") != "yes"]
university = [l for l in university if l.get("accepts_private_well_samples") != "yes"]
commercial = [l for l in commercial if l.get("accepts_private_well_samples") != "yes"]

health.sort(key=lambda l: (l["name"].lower(), l["city"].lower()))
university.sort(key=lambda l: (l["name"].lower(), l["city"].lower()))
commercial.sort(key=lambda l: (l["name"].lower(), l["city"].lower()))

omit_n = data["source"].get("omitted_municipal_utility_count", 0)
total_excel = data["source"].get("excel_rows_total", 80)
lab_count = data["lab_count"]
ver_count = data["verified_private_well_count"]

health_rows = "".join(row(l) for l in health)
univ_rows = "".join(row(l) for l in university)
comm_rows = "".join(row(l) for l in commercial)

thead = """        <thead>
          <tr>
            <th>Laboratory</th>
            <th>City</th>
            <th>County</th>
            <th>Address</th>
            <th>Phone</th>
            <th>Coliform (Micro)</th>
            <th>Lead &amp; copper (LCR)</th>
            <th>WQP</th>
            <th>Accepts private wells?</th>
            <th>Mail / drop-off</th>
          </tr>
        </thead>
"""

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Texas Certified Well Labs | Well Labs Index</title>
  <meta name="description" content="{lab_count} Texas labs from TCEQ’s PWS Lab Map Table (updated 03/26/2026). LCRA verified for residential/private wells. Municipal utility labs omitted.">
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
        <li><a href="texas.html" aria-current="page">Texas labs</a></li>
        <li><a href="../test-private-well.html">How to test</a></li>
        <li><a href="../iron-stains.html">Iron stains</a></li>
        <li><a href="../rotten-egg.html">Rotten egg odor</a></li>
        <li><a href="../about.html">About</a></li>
      </ul>
    </nav>
  </header>
  <main id="content" class="wide">
    <h1 class="page">Texas labs</h1>
    <p class="lede">One laboratory is independently verified to offer residential / private water-supply testing: Lower Colorado River Authority (LCRA) Environmental Laboratory Services. The other rows are Texas commercial, health-department, and university laboratories transcribed from TCEQ’s Public Water System Lab Map Table dated 03/26/2026. We have not verified that those other labs currently accept private-well samples. Call before you collect water.</p>
    <p class="meta">Sources retrieved 2 September 2026. Official table: <a href="https://www.tceq.texas.gov/downloads/drinking-water/quality-assurance/pws-lab-map-table.pdf">PWS Lab Map Table (PDF)</a> / <a href="https://www.tceq.texas.gov/downloads/drinking-water/quality-assurance/pws-lab-map-table.xlsx">Excel</a>, linked from <a href="https://www.tceq.texas.gov/drinkingwater/pwss.html">TCEQ Public Water System Supervision Program</a>. TWDB also points private-well owners to this map: <a href="https://www.twdb.texas.gov/groundwater/data/privwwsamp.asp">Sampling a Private Water Well</a>. Full NELAP search: <a href="https://www.tceq.texas.gov/assistance/resources/steps-to-locate-an-accredited-laboratory">Steps to Locate an Accredited Environmental Laboratory</a>.</p>

    <div class="callout">
      <h2>What we could and could not verify</h2>
      <ul>
        <li>TCEQ’s PWS Lab Map Table lists NELAP-accredited drinking-water public laboratories that offer microbial total coliforms, lead and copper (LCR), and/or water quality parameters (WQP). It is built for public water systems. Appearance on it is not an endorsement and is not, by itself, a statement that the lab takes homeowner samples.</li>
        <li>{omit_n} municipal water-plant, city utility, river-authority, water-district, and water-supply-corporation rows were omitted from this directory ({total_excel} total table rows). That is a directory choice for private well owners, not a statement about their certification. They remain on the official TCEQ file. LCRA is kept because it publishes a residential testing program.</li>
        <li>Microbial / LCR / WQP columns follow the TCEQ table (Y/N). Nitrate and other chemistry are not on this table — ask the lab. Weekend microbial acceptability columns change; always call. Prices are intentionally omitted.</li>
        <li>TCEQ and TWDB both say to always call to confirm address, drop-off hours, and prices before you ship a sample.</li>
      </ul>
    </div>

    <h2>Verified for private well owners</h2>
    <div class="card">
      <h3>Lower Colorado River Authority (LCRA) Environmental Laboratory Services</h3>
      <p>3505 Montopolis Drive, Austin, TX 78744 · <a href="tel:+15127306022">512-730-6022</a> · toll-free <a href="tel:+18773625272">877-362-5272</a> · <a href="mailto:Environmental.Lab@lcra.org">Environmental.Lab@lcra.org</a></p>
      <p>On TCEQ’s PWS Lab Map Table (updated 03/26/2026): Microbial Y, LCR Y, WQP Y. LCRA’s residential water supply testing page (retrieved 2 September 2026) states it offers testing of residential water supplies / private drinking or domestic water sources for common EPA contaminants; bottle kits can be ordered online and shipped or picked up; samples can be shipped on ice or dropped off; hours listed as 8 a.m. to 5 p.m. Monday through Friday. Prices are not copied here.</p>
      <p>Source: <a href="https://www.lcra.org/services/els/residential-water-testing/">lcra.org/services/els/residential-water-testing</a> · TCEQ PWS Lab Map Table.</p>
    </div>

    <h2>Local health department laboratories on the PWS Lab Map Table</h2>
    <p>Except for LCRA above, we have not verified that these laboratories currently accept a sample you collect yourself. Call first. Mail vs. drop-off is unknown on the TCEQ table.</p>
    <div class="table-wrap">
      <table>
        <caption>{len(health)} local / state health laboratories. Source: TCEQ PWS Lab Map Table, updated 03/26/2026.</caption>
{thead}        <tbody>
{health_rows}        </tbody>
      </table>
    </div>

    <h2>University / research laboratories on the PWS Lab Map Table</h2>
    <p>Call to confirm they accept a private-well sample and which analytes they can run.</p>
    <div class="table-wrap">
      <table>
        <caption>{len(university)} university / research laboratories. Source: TCEQ PWS Lab Map Table, updated 03/26/2026.</caption>
{thead}        <tbody>
{univ_rows}        </tbody>
      </table>
    </div>

    <h2>Commercial laboratories in Texas on the PWS Lab Map Table</h2>
    <p>Call to confirm they still hold accreditation, that they accept a private-well sample, and which analytes they can run. Mail vs. drop-off is unknown unless noted. {ver_count} of {lab_count} tabulated rows is verified for private / residential wells (LCRA, above).</p>
    <div class="table-wrap">
      <table>
        <caption>{len(commercial)} commercial laboratories with Texas addresses (municipal utility rows omitted). Source: TCEQ PWS Lab Map Table, updated 03/26/2026.</caption>
{thead}        <tbody>
{comm_rows}        </tbody>
      </table>
    </div>

    <h2>Official tools if you need more labs</h2>
    <ul>
      <li><a href="https://www.tceq.texas.gov/drinkingwater/pwss.html">TCEQ PWSS page</a> — map plus full PWS Lab Map Table (including utility labs we omitted).</li>
      <li><a href="https://www.tceq.texas.gov/assistance/resources/steps-to-locate-an-accredited-laboratory">Steps to Locate an Accredited Environmental Laboratory</a> — NELAP search by matrix and analyte.</li>
      <li><a href="https://www.tceq.texas.gov/agency/qa/env_lab_accreditation.html">TCEQ Environmental Laboratory (NELAP) Accreditation</a> — public database of accredited labs and fields of accreditation.</li>
    </ul>
  </main>
  <footer class="site">
    <div class="inner">
      <p><strong>Well Labs Index</strong> is a project by Stephen Shortell. Last updated 2 September 2026 (US/Pacific).</p>
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

out = ROOT / "labs/texas.html"
out.write_text(page)
print(f"Wrote {out} ({lab_count} labs, health={len(health)}, univ={len(university)}, comm={len(commercial)}, verified={ver_count})")
