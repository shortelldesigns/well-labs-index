#!/usr/bin/env python3
import html as htmlmod
import json
import re
from pathlib import Path

ROOT = Path("/workspace/well-lab-index")
data = json.loads((ROOT / "data/labs-wi.json").read_text())
labs = data["labs"]

def esc(s):
    return htmlmod.escape(str(s), quote=True)

def tel_href(phone):
    digits = re.sub(r"\D", "", phone)
    if len(digits) == 10:
        return f"+1{digits}"
    if len(digits) == 11 and digits.startswith("1"):
        return f"+{digits}"
    return digits or phone

def yesno(flag, yes_text="Yes"):
    if flag:
        return f'<td class="yes">{yes_text}</td>'
    return '<td class="no">—</td>'

def accepts_cell(lab):
    if lab.get("accepts_private_well_samples") == "yes":
        return '<td class="yes">Yes — lab’s own public page</td>'
    return '<td class="unknown">unknown — call first</td>'

def mail_cell(lab):
    v = lab.get("sample_dropoff_or_mail") or "unknown"
    if v == "unknown":
        return '<td class="unknown">unknown</td>'
    return f'<td>{esc(v)}</td>'

def phone_cell(phone):
    if not phone or phone == "unknown":
        return "unknown"
    return f'<a href="tel:{tel_href(phone)}">{esc(phone)}</a>'

# Groups
verified = [l for l in labs if l.get("accepts_private_well_samples") == "yes"]
# Health / public / university for bacteria+chemistry combined tables
# Prefer excel-sourced names when present; include bacti-only health
healthish = [l for l in labs if l["category"] in ("public_health", "health_department", "university")]
commercial = [l for l in labs if l["category"] == "commercial"]

# Sort
healthish.sort(key=lambda l: (l["name"].lower(), l.get("city","")))
commercial.sort(key=lambda l: (l["name"].lower(), l.get("city","")))

bacti_omit = data["source"].get("bactilab_omitted_municipal_count", 0)
bacti_total = data["source"].get("bactilab_rows_total", 0)

def row(lab):
    coli = yesno(lab.get("coliform_listed"))
    nit = yesno(lab.get("nitrate_listed"))
    ars = yesno(lab.get("arsenic_listed"))
    other = esc(lab.get("chemistry_other_summary") or "—")
    county = esc(lab.get("county") or "unknown")
    city = esc(lab.get("city") or "unknown")
    name = esc(lab["name"])
    return (
        f"<tr><td>{name}</td><td>{city}</td><td>{county}</td>"
        f"<td>{phone_cell(lab.get('phone','unknown'))}</td>"
        f"{coli}{nit}{ars}<td>{other}</td>"
        f"{accepts_cell(lab)}{mail_cell(lab)}</tr>\n"
    )

health_rows = "".join(row(l) for l in healthish)
comm_rows = "".join(row(l) for l in commercial)

omit_note = (
    f"{bacti_omit} municipal / utility / wastewater / sanitary-district rows were omitted from the "
    f"BactiLab table ({bacti_total} total portal rows). That is a directory choice for private well owners, "
    "not a statement about their certification."
)

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Wisconsin Certified Well Labs | Well Labs Index</title>
  <meta name="description" content="{esc(str(data['lab_count']))} Wisconsin labs from DNR’s January 2026 chemistry list and DATCP BactiLab. WSLH and WEAL verified for private wells. Municipal plants omitted.">
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
        <li><a href="wisconsin.html" aria-current="page">Wisconsin labs</a></li>
        <li><a href="../test-private-well.html">How to test</a></li>
        <li><a href="../iron-stains.html">Iron stains</a></li>
        <li><a href="../rotten-egg.html">Rotten egg odor</a></li>
        <li><a href="../about.html">About</a></li>
      </ul>
    </nav>
  </header>
  <main id="content" class="wide">
    <h1 class="page">Wisconsin labs</h1>
    <p class="lede">Two laboratories are independently verified to serve private-well / homeowner samples: the Wisconsin State Laboratory of Hygiene (WSLH) and the UW–Stevens Point Water &amp; Environmental Analysis Lab (WEAL). Other rows are Wisconsin laboratories transcribed from WI DNR’s Accredited Laboratories chemistry list dated January 2026 (NR 809 and NR 812) and from the DATCP/DNR BactiLab portal for coliform bacteria. We have not verified that those other labs currently accept private-well samples. Call before you collect water.</p>
    <p class="meta">Sources retrieved 1 September 2026. Chemistry list: <a href="https://dnr.wisconsin.gov/sites/default/files/topic/LabCert/DWLabs012126.xlsx">DWLabs012126.xlsx</a> (“Accredited Laboratories - January 2026” / drinking water certified labs — chemistry), linked from <a href="https://dnr.wisconsin.gov/topic/labCert/certified-lab-lists">WI DNR certified lab lists</a> (also under “Drinking Water Laboratories for Homeowners”). Bacteria list: <a href="https://apps.dnr.wi.gov/dwsportalpub/BactiLab">BactiLab</a> (DATCP-certified coliform). Private-well guidance: <a href="https://dnr.wisconsin.gov/topic/Wells/privateWellTest.html">WI DNR private well testing</a>.</p>

    <div class="callout">
      <h2>What we could and could not verify</h2>
      <ul>
        <li>WI DNR recommends private well owners test annually for bacteria and nitrate, and for arsenic every 5 years (yearly in Outagamie, Winnebago, and Brown counties). Source: <a href="https://dnr.wisconsin.gov/topic/Wells/privateWellTest.html">dnr.wisconsin.gov/…/privateWellTest.html</a>.</li>
        <li>The January 2026 Excel is a drinking-water chemistry accreditation list (NR 809 / NR 812). Appearance on it is not an endorsement and is not, by itself, a statement that the lab takes homeowner samples.</li>
        <li>BactiLab states labs are certified by DATCP to perform coliform bacteria analysis of drinking water samples, and that certification is not an endorsement or guarantee of the data.</li>
        <li>{esc(omit_note)}</li>
        <li>Out-of-state laboratories on the chemistry Excel (often PFAS-only or specialty) were not tabulated. Industrial labs (e.g., Kohler Co. CHEM Lab) and the DATCP agency laboratory were omitted as not homeowner-facing.</li>
        <li>Nitrate / arsenic columns are marked Yes when the Excel Parameter list includes those words. Coliform is marked Yes when the lab appears on BactiLab (after municipal omissions). Contact the lab for methods offered.</li>
        <li>Prices are intentionally omitted — they change. Confirm current fees with the laboratory.</li>
      </ul>
    </div>

    <h2>Verified for private well owners</h2>
    <div class="card">
      <h3>Wisconsin State Laboratory of Hygiene (WSLH)</h3>
      <p>2601 Agriculture Drive, Madison, WI · BactiLab phone <a href="tel:+16082246260">(608) 224-6260</a> · kit ordering <a href="tel:+18004424618">(800) 442-4618</a> or <a href="tel:+16082246202">(608) 224-6202</a></p>
      <p>On WI DNR’s January 2026 chemistry list (Public Health Lab, Dane County, Madison) and on BactiLab as STATE LABORATORY OF HYGIENE. WSLH’s public pages describe public-health tests available to Wisconsin citizens, a Homeowner Package, and kit ordering. Drop-off hours on the kit page: Monday–Friday 7:45 AM–4:30 PM at 2601 Agriculture Drive, Madison.</p>
      <p>Sources: <a href="https://www.slh.wisc.edu/environmental/water/public-health-tests-available-to-wisconsin-citizens/">Public health tests available to Wisconsin citizens</a> · <a href="https://www.slh.wisc.edu/environmental/water/public-environmental-and-water-testing-prices/">Public environmental and water testing / kit ordering</a> · <a href="https://apps.dnr.wi.gov/dwsportalpub/BactiLab">BactiLab</a> · January 2026 chemistry Excel.</p>
    </div>
    <div class="card">
      <h3>Water &amp; Environmental Analysis Lab (WEAL), UW–Stevens Point</h3>
      <p>800 Reserve St, Stevens Point, WI · <a href="tel:+17153463209">(715) 346-3209</a> · <a href="mailto:weal@uwsp.edu">weal@uwsp.edu</a></p>
      <p>On the January 2026 chemistry list as UWSP Water and Environmental Analysis Lab (Public Health Lab, Portage County) and on BactiLab as WATER &amp; ENVIRONMENTAL ANALYSIS. WEAL’s well-water-testing page states it serves private well owners; kits are available through county UW-Extension offices.</p>
      <p>Source: <a href="https://www.uwsp.edu/center-for-watershed-science-and-education/well-water-testing/">UWSP / CWSE well water testing</a> · <a href="https://apps.dnr.wi.gov/dwsportalpub/BactiLab">BactiLab</a> · January 2026 chemistry Excel.</p>
    </div>

    <h2>County, city, and university public-health laboratories</h2>
    <p>Includes public-health and local health department laboratories from the January 2026 chemistry list and additional county/city health rows from BactiLab. Except for WSLH and WEAL above, we have not verified that these laboratories currently accept a sample you collect yourself. Call first.</p>
    <div class="table-wrap">
      <table>
        <caption>{len(healthish)} public-health / health-department / university laboratories. Sources: WI DNR DWLabs012126.xlsx (January 2026) and BactiLab (retrieved 1 September 2026).</caption>
        <thead>
          <tr>
            <th>Laboratory</th>
            <th>City</th>
            <th>County</th>
            <th>Phone</th>
            <th>Coliform</th>
            <th>Nitrate</th>
            <th>Arsenic</th>
            <th>Other chemistry listed</th>
            <th>Accepts private wells?</th>
            <th>Mail / drop-off</th>
          </tr>
        </thead>
        <tbody>
{health_rows}        </tbody>
      </table>
    </div>

    <h2>Commercial laboratories in Wisconsin</h2>
    <p>Call to confirm they still hold certification, that they accept a private-well sample, and which analytes they can run. Coliform comes from BactiLab; nitrate, arsenic, and other chemistry come from the January 2026 Excel when the lab appears there. Mail vs. drop-off is unknown unless noted.</p>
    <div class="table-wrap">
      <table>
        <caption>{len(commercial)} commercial or independent laboratories with Wisconsin listings. Sources: WI DNR January 2026 chemistry Excel and BactiLab. {data['verified_private_well_count']} of {data['lab_count']} total directory rows are verified for private wells (WSLH and WEAL, above).</caption>
        <thead>
          <tr>
            <th>Laboratory</th>
            <th>City</th>
            <th>County</th>
            <th>Phone</th>
            <th>Coliform</th>
            <th>Nitrate</th>
            <th>Arsenic</th>
            <th>Other chemistry listed</th>
            <th>Accepts private wells?</th>
            <th>Mail / drop-off</th>
          </tr>
        </thead>
        <tbody>
{comm_rows}        </tbody>
      </table>
    </div>
    <p>Machine-readable copy: <a href="../data/labs-wi.json">data/labs-wi.json</a>. Every record includes a source URL.</p>
    <p>CDC annual panel (total coliform, nitrates, TDS, pH) and how to read a report: <a href="../test-private-well.html">how to test a private well</a>.</p>
  </main>
  <footer class="site">
    <div class="inner">
      <p><strong>Well Labs Index</strong> is a project by Shortell Designs. Last updated 1 September 2026 (US/Pacific).</p>
      <p><a href="../about.html">Methodology and disclosure</a> · <a href="../states.html">State directory</a></p>
      <div class="disclaimer">
        <p>This site is not a government agency and does not certify laboratories. Listings are transcribed from official state and federal sources cited on each page. Accreditation, phone numbers, and sample-acceptance policies change. Confirm with the laboratory and the state certification program before you ship a sample.</p>
        <p>Private wells are not regulated under the federal Safe Drinking Water Act in the way public water systems are. You are responsible for testing. This site is educational, not medical, legal, or engineering advice. We may earn a commission on future product or service links; there are no live affiliate links on this version.</p>
      </div>
    </div>
  </footer>
</body>
</html>
'''

out = ROOT / "labs/wisconsin.html"
out.write_text(html)
print(f"Wrote {out} bytes={out.stat().st_size} health={len(healthish)} commercial={len(commercial)} verified={len(verified)}")
