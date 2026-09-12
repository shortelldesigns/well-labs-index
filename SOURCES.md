# Sources fetched for Well Labs Index v1

Retrieve date: **29 August 2026** (US/Pacific; fetch ran 30 August 2026 UTC).

## Succeeded

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| CDC Guidelines for Testing Well Water | https://www.cdc.gov/drinking-water/safety/guidelines-for-testing-well-water.html | 1 July 2024 | WebFetch. Annual panel: total coliforms, nitrates, TDS, pH. State-certified lab. Hotline (800) 426-4791. |
| EPA Protect Your Home’s Water | https://www.epa.gov/privatewells/protect-your-homes-water | Last updated 26 February 2026 | WebFetch. Symptom-to-test chart; annual tests; treatment caveats. |
| EPA certified-lab contacts | https://www.epa.gov/dwlabcert/contact-information-certification-programs-and-certified-laboratories-drinking-water | Last updated 11 August 2026 | WebFetch. Points to August 2025 state-program PDF. EPA does not test private wells. |
| EPA state certification programs PDF (2023 file still hosted) | https://www.epa.gov/system/files/documents/2023-03/state-cert-programs-certify-labs-to-conduct-drinking-water-analyses.pdf | EPA 815-B-23-004, March 2023 | WebFetch. MN: search DW. PA: search matrix DW. The August 2025 filename linked from EPA’s HTML page was not retrieved as a PDF (see Failures). |
| EPA Home Water Testing fact sheet | https://www.epa.gov/sites/default/files/2015-05/documents/epa816f05013.pdf | EPA 816-F-05-013, May 2005 | curl + pdftotext. “Find out what is in your water … before contacting potential dealers.” Stained fixtures → iron, copper, manganese. |
| USGS Domestic (Private) Supply Wells | https://www.usgs.gov/mission-areas/water-resources/science/domestic-private-supply-wells | Retrieved 29 August 2026 (page does not show a single “last updated” in the fetch) | WebFetch. “More than 43 million people—about 15 percent of the U.S. population.” |
| MDH hydrogen sulfide | https://www.health.mn.gov/communities/environment/water/wells/waterquality/hydrosulfide.html | Last updated 18 October 2024 | WebFetch. Anode vs bacteria vs groundwater; treatment types and mg/L cutoffs. |
| MDH iron | https://www.health.state.mn.us/communities/environment/water/wells/waterquality/iron.html | Last updated 1 August 2025 | WebFetch. Forms of iron; 0.3 mg/L aesthetic point of reference. |
| MDH iron bacteria | https://www.health.state.mn.us/communities/environment/water/wells/waterquality/ironbacteria.html | Last updated 7 January 2026 | WebFetch. |
| MDH manganese | https://www.health.state.mn.us/communities/environment/water/contaminants/manganese.html | Last updated 17 November 2025 | WebFetch. Guidance values 100 µg/L (infants drinking tap water) and 300 µg/L. |
| MDH lab map PDF | https://www.health.state.mn.us/communities/environment/water/docs/wells/waterquality/labmap.pdf | July 2026 (PDF metadata CreationDate 8 July 2026 UTC; title “Accredited Labs in Minnesota Accepting Drinking Water Samples from Private Well Users”) | curl + pdftotext -layout. 5 pages, 24 labs. Archived at `data/sources/mdh-labmap-july-2026.pdf`. Star icons for courier/drop-off did not appear in the text layer. |
| PA DEP private well water testing | https://www.pa.gov/agencies/dep/residents/my-water/private-wells/water-testing | Retrieved 29 August 2026 | WebFetch. Annual tests; regional kit-sale offices; links to chemical and bacteriological lab PDFs. |
| PA DEP Bureau of Laboratories | https://www.pa.gov/agencies/dep/programs-and-services/bureau-of-labs | Retrieved 29 August 2026 | WebFetch. Accreditation program description. Not listed as a homeowner lab. |
| PA DEP DW microbiology accreditation report | https://files.dep.state.pa.us/Water/BSDW/DrinkingWaterManagement/PrivateWaterWells/DW_Micro_Lab_Certification_06-13-2024%20Accreditation%20Report.pdf | 13 June 2024 | **curl HTTPS failed** (TLS unexpected EOF). **WebFetch succeeded.** Used for commercial-lab rows. Municipal plants omitted from the directory. |
| Penn State Extension, Testing Your Drinking Water | https://extension.psu.edu/testing-your-drinking-water | Updated 2 June 2025 | WebFetch. |
| Penn State Extension, Chain of Custody Water Testing | https://extension.psu.edu/chain-of-custody-water-testing | Updated 29 May 2025 | WebFetch. How to search DEP accredited labs. AASL does not offer chain of custody. |
| Penn State Extension, How To Use the Penn State Drinking Water Test Kit | https://extension.psu.edu/how-to-use-the-penn-state-drinking-water-test-kit | Retrieved 29 August 2026 | WebFetch (video transcript). Mail-in kit, 30-hour bacteria window, ship Mon–Wed. Price mentioned in the transcript was **not** copied onto the site (could be stale). |
| Penn State AASL water testing | https://agsci.psu.edu/aasl/water-testing | Retrieved 29 August 2026 (via search snippet + related pages) | Direct WebFetch of the drinking-water-testing subpage **timed out**. Parent water-testing URL and Extension pages supplied address 720 Tower Rd, University Park, PA 16802; phone 814-863-0841; email aaslab@psu.edu; hours Mon–Fri 8:00 AM–4:00 PM. DEP PDF lists the same lab as 111 Ag Analytical Srvcs Lab, University Park, PA 16802, ID 14-00588. Public page uses the Tower Road address. |
| Ohio EPA Combined Lab List PDF | https://dam.assets.ohio.gov/image/upload/epa.ohio.gov/Portals/28/documents/labcert/Combined-Lab-List.pdf | August 2026, rev. 8/13/2026 (PDF title; CreationDate 13 August 2026 UTC) | curl of the DAM/Cloudinary URL returned HTTP 200, 232723 bytes. Archived at `data/sources/ohio-epa-combined-lab-list.pdf`. pdftotext -layout, 8 pages. The still-linked portal path `epa.ohio.gov/static/Portals/28/documents/labcert/Combined-Lab-List.pdf` returned 404. |
| Ohio EPA FAQ: Testing water from private wells | https://ohioepa.custhelp.com/app/answers/detail/a_id/1057 | Published 7 August 2007; updated 2 September 2025 | WebFetch. Ohio EPA does not regulate or test private wells; points to the certified-lab list and local health departments. |
| Ohio Department of Health Private Water Systems Program | https://odh.ohio.gov/know-our-programs/private-water-systems-program | Retrieved 29 August 2026 | WebFetch. Contact 614-644-7558, Privatewater@odh.ohio.gov. Program regulates wells serving fewer than 15 connections. |
| ODH find local health districts | https://odh.ohio.gov/wps/portal/gov/odh/find-local-health-districts | Retrieved 29 August 2026 | WebFetch. Search/map page; used as the official locator link, not scraped into a table. |
| Mahoning County Public Health laboratory services | https://www.mahoninghealth.org/laboratory-services/ | Retrieved 29 August 2026 | WebFetch. States Ohio EPA certification for public and private drinking-water systems and invites well owners to arrange bacteria testing. Used only to verify private-well acceptance for the lab Ohio EPA lists as Mahoning County Board of Health. |

## Failed or incomplete

| Attempt | URL | What happened | What we did instead |
| --- | --- | --- | --- |
| EPA August 2025 state-program PDF | Guessed path `https://www.epa.gov/system/files/documents/2025-08/state-certification-programs-certify-laboratories-to-conduct-drinking-water-analyses.pdf` | curl returned HTML, not a PDF | Used EPA’s HTML contact page (11 August 2026) plus the still-hosted March 2023 PDF. Did not invent 2025 file contents. |
| PA DEP bacteriology PDF via curl | `https://files.dep.state.pa.us/Water/BSDW/DrinkingWaterManagement/PrivateWaterWells/DW_Micro_Lab_Certification_06-13-2024%20Accreditation%20Report.pdf` | curl TLS error `unexpected eof while reading` (HTTPS and HTTP-then-redirect) | WebFetch retrieved the PDF text. |
| PA DEP chemical-lab PDF | Linked from PA DEP water-testing page; older URLs such as `zAccredited_Laboratories.pdf` and `Accredited_Laboratories_21sep2021.pdf` | curl TLS failure; not retried via WebFetch after bacteriology PDF succeeded | Chemical accreditation not tabulated. PA page tells readers to use DEP’s search tool. |
| PA DEP live search tool | ReportViewer / cedatareporting.pa.gov | Not a static extractable list from this environment | Linked the official accreditation program page instead of scraping a live report server. |
| Penn State AASL drinking-water-testing page | https://agsci.psu.edu/aasl/water-testing/drinking-water-testing | WebFetch timed out | Used parent water-testing page details via search plus Extension pages and the DEP PDF. |
| MDH map “star” courier/drop-off icons | Same labmap.pdf | Not present in pdftotext output | `sample_dropoff_or_mail` = unknown on every MN row. |
| Ohio EPA lab-certification HTML page | https://epa.ohio.gov/divisions-and-offices/drinking-and-ground-waters/public-water-systems/laboratory-certification | WebFetch 404 | Used the Combined Lab List PDF (DAM URL) plus the private-well FAQ. |
| Ohio EPA data-reporting-resources (Combined Lab List link) | https://epa.ohio.gov/divisions-and-offices/drinking-and-ground-waters/guides-manuals/data-reporting-resources | WebFetch 404 | Combined Lab List retrieved from the DAM URL that search returned. |
| Ohio EPA static Combined-Lab-List.pdf | https://epa.ohio.gov/static/Portals/28/documents/labcert/Combined-Lab-List.pdf | curl HTTP 404 | Used https://dam.assets.ohio.gov/image/upload/epa.ohio.gov/Portals/28/documents/labcert/Combined-Lab-List.pdf instead. Same filename, document dated August 2026, rev. 8/13/2026. |
| ODH water-quality / info-for-LHDs pages | Guessed paths under odh.ohio.gov/know-our-programs/private-water-systems-program/ | WebFetch 404 | Cited the Private Water Systems program landing page and the find-local-health-districts locator. Did not invent an ODH private-well lab list. |

## Not used as lab sources

- Third-party directories (TapWaterData and similar).
- Truncated search-engine snippets of old PA lab PDFs (incomplete phones/addresses).
- Filter-review or affiliate sites.

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


## Maine (4 September 2026)

Retrieve date: **4 September 2026** (US/Pacific).

### Succeeded

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| Maine In-State Commercial Drinking Water Labs (PDF) | https://www.maine.gov/dhhs/mecdc/sites/maine.gov.dhhs.mecdc/files/CommercialListMaineLabs.pdf | Last updated 5/16/2026 | Archived at `data/sources/me-commercial-drinking-water-labs.pdf`. 12 labs; lab code, name, website, city, telephone. Specialty notes (PFAS Only, Bacteria only) printed on list. Linked from Maine private-well and accreditation pages as the certified-lab list for well owners. |
| Maine Laboratory Accreditation | https://www.maine.gov/dhhs/mecdc/services/business-services/laboratory-accreditation | Retrieved 4 September 2026 | Archived `data/sources/me-laboratory-accreditation.html`. Links commercial PDF, PFAS list, asbestos/radium list, All Accredited Laboratories Excel. Lab Accreditation contact Christine Blais (207) 287-3220. |
| Maine CDC Private Well Water | https://www.maine.gov/dhhs/mecdc/healthy-living/health-and-safety/drinking-water-safety/private-well-water | Retrieved 4 September 2026 | Archived `data/sources/me-private-well-water.html`. Annual bacteria/nitrate; 3–5 year metals panel; points to commercial labs PDF; free technical assistance (866) 292-3474 / (207) 287-4311. |
| HETL Environmental Chemistry | https://www.maine.gov/dhhs/mecdc/services/maine-public-health-laboratory/environmental-chemistry | Retrieved 4 September 2026 | Archived `data/sources/me-hetl-environmental-chemistry.html`. States HETL tests drinking water from public utilities and from private wells. Used to verify private-well acceptance for HETL only. |
| HETL Testing Your Wellwater | https://www.maine.gov/dhhs/mecdc/services/maine-public-health-laboratory/environmental-chemistry/testing-wellwater | Retrieved 4 September 2026 | Archived `data/sources/me-hetl-testing-wellwater.html`. General well-testing guidance; points to accredited laboratory PDF. |

### Failed or incomplete (Maine)

| Attempt | URL | What happened | What we did instead |
| --- | --- | --- | --- |
| Street addresses on commercial PDF | same commercial PDF | Not printed in the PDF text layer | Address = unknown on every row; link lab website / call. |
| All Accredited Laboratories Excel | Linked from commercial PDF / accreditation page | Not required for this build once the commercial in-state list transcribed cleanly | Linked the Excel from the accreditation page for readers who need the full accredited set. |

### Not used as ME lab sources

- Third-party directories.
- Filter-review or affiliate sites.
- Invented private-well acceptance claims beyond HETL’s Environmental Chemistry page.
- Lab marketing sites for phones/addresses (websites used only as printed on the official PDF).

## Indiana (5 September 2026)

Retrieve date: **5 September 2026** (US/Pacific).

### Succeeded

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| IDEM Indiana Certified Drinking Water Laboratories (PDF) | https://www.in.gov/idem/cleanwater/files/dw_cert_lab_in-state.pdf | Revised 11/7/2025 | Archived at `data/sources/in-certified-dw-labs-2025-11-07.pdf` (+ `.txt` via pdftotext -layout). Title: Indiana Certified Drinking Water Laboratories. Transcribed **only** the section “Labs that accept samples from the public” (49 labs). Separate “Labs that do not accept samples from the public” section not tabulated; linked from the Indiana page. Municipal utilities in the public-accepting section included. |
| IDOH Laboratory — Well Water | https://www.in.gov/health/laboratories/testing/well-water/ | Retrieved 5 September 2026 | Archived `data/sources/in-idoh-well-water.html`. States IDOH offers testing for private citizens using well water for drinking; annual bacteria + nitrate; every 5 years fluoride/arsenic/lead/copper; order kits via Access Indiana; address IDOH Laboratory Suite B, 550 W 16th St, Indianapolis, IN 46202. **Dollar prices not copied to public HTML.** Used to verify private-well acceptance for IDOH Laboratories only (M-IN-00 / C-IN-00). |
| IDOH EPH — Well Water Quality and Testing | https://www.in.gov/health/eph/well-water-quality-and-testing/ | Retrieved 5 September 2026 | Archived `data/sources/in-eph-well-water-quality.html`. Context for private well owners. |
| Drinking Water Laboratory Certification (IDOH) | https://www.in.gov/health/laboratories/drinking-water-laboratory-certification/ | Retrieved 5 September 2026 | Archived `data/sources/in-drinking-water-lab-certification.html`. Certification program context. |
| IDEM Laboratories page | https://www.in.gov/idem/cleanwater/drinking-water/drinking-water-compliance-section/water-systems/laboratories/ | Linked 5 September 2026 | Context link; PDF is the transcribed source. |

### Failed or incomplete (Indiana)

| Attempt | URL | What happened | What we did instead |
| --- | --- | --- | --- |
| Multi-column PDF text layer | same IDEM PDF | City of Goshen Water Lab and Elkhart Public Works & Utilities Laboratory both print lab ID M-20-01; Pace Analytical Services, LLC (Indianapolis) prints only C-49-06 (same C-id string as EMSL). Five labs have blank website fields. | Kept IDs/websites as printed; marked website unknown where blank; disclosed on page and in JSON notes. |
| Non-public section of IDEM PDF | same PDF | Not transcribed into the directory table | Callout + PDF link only. |

### Not used as IN lab sources

- Third-party directories.
- Filter-review or affiliate sites.
- Invented private-well acceptance claims beyond the IDOH well-water page and the PDF’s “accept samples from the public” section label.
- Dollar prices from the IDOH well-water page (intentionally omitted on public HTML).


## North Carolina (6 September 2026)

Retrieve date: **6 September 2026** (US/Pacific).

### Succeeded

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| NCSLPH Certified Drinking Water Commercial Laboratories (search UI) | https://slphreporting.dph.ncdhhs.gov/Certification/CertifiedLaboratory.asp | Retrieved 6 September 2026 | Archived `data/sources/nc-slph-CertifiedLaboratory-2026-09-06.html`. Contaminant search form; “View a list of all laboratories” POSTs SubTopic=ShowDWLabs. |
| NCSLPH ShowDWLabs commercial list | same ASP endpoint, POST SubTopic=ShowDWLabs&LabType=Commercial | Retrieved 6 September 2026 | Archived `data/sources/nc-slph-ShowDWLabs-commercial-2026-09-06.html`. 86 commercial labs all states; **47 with State=NC** transcribed. Columns: State, City, Lab Name, Lab No., Phone. |
| NCSLPH DisplayDWLab detail pages | same ASP endpoint, POST SubTopic=DisplayDWLab&LabNumber=… | Retrieved 6 September 2026 | Archived per lab as `data/sources/nc-lab-<LabNo>-2026-09-06.html` (47 files). Street, mailing address, city/ZIP, phone, fax, certification sectionHeader analyte lists. |
| NC DHHS Private Well Water Testing FAQs | https://epi.dph.ncdhhs.gov/oee/wellwater/faqs.html | Retrieved 6 September 2026 | Archived `data/sources/nc-private-well-faqs-2026-09-06.html`. New wells: State Lab (via local health department) or state-certified commercial lab. Existing wells: local health department or certified commercial lab. Links the NCSLPH certified-lab search. |
| NC DHHS Private Wells program | https://epi.dph.ncdhhs.gov/oee/programs/wellwater.html | Retrieved 6 September 2026 | Archived `data/sources/nc-private-wells-oee-2026-09-06.html`. Program context for private well owners. |
| NCSLPH Environmental Inorganic Chemistry | https://slph.dph.ncdhhs.gov/environmentalsciences/inorganic/default.asp | Retrieved 6 September 2026 | Archived `data/sources/nc-slph-inorganic-2026-09-06.html`. States homeowner chemical analyses only if submitted through the local health department. Used to verify the State Lab private-well path. |
| NCSLPH Environmental Sciences Certifications hub | https://slph.dph.ncdhhs.gov/environmentalsciences/certification/default.asp | Retrieved 6 September 2026 | Archived `data/sources/nc-slph-certification-hub-2026-09-06.html`. Program context; links certified laboratories. |
| DPH local health department directory | https://www.dph.ncdhhs.gov/contact/LHD | Linked 6 September 2026 | Official locator for the State Lab submission path; not scraped into a table. |

### Failed or incomplete (North Carolina)

| Attempt | URL | What happened | What we did instead |
| --- | --- | --- | --- |
| Direct GET ShowDWLabs.asp | https://slphreporting.dph.ncdhhs.gov/Certification/ShowDWLabs.asp | HTTP 404 | Used POST to CertifiedLaboratory.asp with SubTopic=ShowDWLabs (as the site’s own “View a list of all laboratories” control does). |
| Per-lab private-well acceptance on commercial roster | ShowDWLabs / DisplayDWLab | Not stated | Marked accepts_private_well_samples unknown on every commercial row; verified card documents State Lab via local health department only. |
| Websites / counties on roster | same | Not printed | website=null; county=null. |
| NC DEQ WW/GW certified laboratory listings | https://www.deq.nc.gov/about/divisions/water-resources/water-sciences/chemistry-laboratory/certified-laboratory-listing | Wastewater/groundwater certification lists (commercial in-state updated 5/2026) | Not used as the drinking-water commercial source; NCSLPH drinking-water certification roster is the correct SDWA drinking-water list for this directory. Linked only if readers need DEQ WW/GW context — not transcribed here. |

### Not used as NC lab sources

- Stale `/workspace/lab-lists/nc_*.html` caches alone (re-fetched live; caches used only as URL hints).
- Third-party directories.
- Filter-review or affiliate sites.
- Invented private-well acceptance claims for commercial labs beyond DHHS FAQ guidance that such labs are an option.

## Iowa (7 September 2026)

Retrieve date: **7 September 2026** (US/Pacific).

### Succeeded

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| Iowa DNR LabCert — List of Certified Labs | https://programs.iowadnr.gov/labcert/Home/LabListing | Date Generated: 9/7/2026 | Archived `data/sources/ia-labcert-lablisting-2026-09-07.html`. Columns: Lab Type, Lab Name, Lab Number, Lab Address, Phone Number, Program. Filtered to Program including Drinking Water. |
| Iowa DNR Private Well Testing | https://www.iowadnr.gov/environmental-protection/water-quality/private-well-program/well-testing | Retrieved 7 September 2026 | Archived `data/sources/ia-dnr-well-testing-2026-09-07.html`. County environmental health path; Private Well Grants (PWG) free testing for recommended analytes; points to SHL and DNR Certified Drinking Water Laboratories. |
| Iowa DNR Private Well Program hub | https://www.iowadnr.gov/environmental-protection/water-quality/private-well-program | Retrieved 7 September 2026 | Archived `data/sources/ia-dnr-private-well-program-2026-09-07.html`. Program context. |
| State Hygienic Laboratory — Request Private Well Testing | https://shl.uiowa.edu/request-private-well-testing | Retrieved 7 September 2026 | Archived `data/sources/ia-shl-request-private-well-testing-2026-09-07.html`. Homeowner kit for coliform bacteria and nitrate; notes PWG / county funding may be available. Used to verify SHL private-well path. |
| SHL private well (env) | https://shl.uiowa.edu/env/privatewell | Linked 7 September 2026 | Follow redirects if the URL moves; not required for transcription. |

### Directory choices (Iowa)

| Choice | Detail |
| --- | --- |
| In-state Commercial DW | 11 labs tabulated (007, 051, 061, 084, 095, 113, 279, 311, 379, 396, 416). Private-well acceptance unknown — call first. |
| SHL verified | 3 LabCert locations: Coralville (027), Lakeside (393), Ankeny (397). |
| County / district health DW | 3 rows: Dubuque County (016), Siouxland District (024), Linn County (029). Acceptance unknown — call first; DNR says counties can arrange testing / PWG. |
| Omitted | Municipal utility / WWTP / WRF / water works / regional water association; Industrial/Private (incl. Iowa Soybean Association); Nonpotable-only; out-of-state Commercial; DNR (Test - Not a Lab). |
| Prices | Analysis prices omitted. PWG service grant dollar amounts appear on DNR well-testing page but were not copied onto public HTML. |

### Failed or incomplete (Iowa)

| Attempt | URL | What happened | What we did instead |
| --- | --- | --- | --- |
| Per-lab private-well acceptance on LabCert commercial rows | LabCert | Not stated | Marked accepts_private_well_samples unknown; verified card documents SHL + county/PWG path. |
| Mail vs. drop-off for commercial labs | LabCert | Not stated | Marked unknown. |


## Virginia (11 September 2026)

Retrieve date: **11 September 2026** (US/Pacific).

### Succeeded

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| DCLS Find a Lab | https://dgs.virginia.gov/division-of-consolidated-laboratory-services/certification-accreditation/find-a-lab | Retrieved 11 September 2026 | Links DW PDF/Excel and Ch46/Ch45 directories. Archived `data/sources/va-find-a-lab-2026-09-11.html`. |
| DCLS DW Certified Labs Excel | https://dgs.virginia.gov/content/dam/site-assets/dcls/Lab%20Certification/VELAP/DW_Certified_Labs_20260801.xlsx | Current as of 8/1/2026 | Archived `data/sources/va-dw-certified-labs-2026-08-01.xlsx`. |
| DCLS DW Laboratories with certification detail PDF | https://dgs.virginia.gov/content/dam/site-assets/dcls/Lab%20Certification/VELAP/Ch%2046%20Ch%2041%20DW%20Laboratories%20w%20detail%2020260804.pdf | Effective 08/04/2026 | Archived PDF + txt. |
| DCLS VELAP Chapter 46 commercial directory | https://dgs.virginia.gov/content/dam/site-assets/dcls/Lab%20Certification/VELAP/Q3%202026%20VELAP/DIRECTORY%20COMMERCIAL%20LABS%20CH46.pdf | List dated 7/1/2026 on PDF footer | Archived PDF + txt. Used to identify commercial CERTIFIED labs. |
| VAHWQP | https://www.wellwater.bse.vt.edu/vahwqp.php | Retrieved 11 September 2026 | Verified private-well clinic path. Archived HTML. |
| VCE Extension offices | https://ext.vt.edu/offices.html | Retrieved 11 September 2026 | Clinic entry point. |
| VDH Private Well Water Testing | https://www.vdh.virginia.gov/environmental-health/water-testing/ | Retrieved 11 September 2026 via WebFetch (curl HTTP 403) | Points to DCLS lists + VAHWQP. Archive note `.webfetch.md`. |
| VDH Private Well Program | https://www.vdh.virginia.gov/environmental-health/private-well-program/ | Retrieved 11 September 2026 via WebFetch (curl HTTP 403) | States VDH does not test private wells. |
| DCLS Environmental FAQ | https://dgs.virginia.gov/division-of-consolidated-laboratory-services/lab-testing/environmental | Retrieved 11 September 2026 | States DCLS does not test private wells for homeowners. |

### Failed or incomplete (Virginia)

| Attempt | URL | What happened | What we did instead |
| --- | --- | --- | --- |
| VDH pages via curl | vdh.virginia.gov environmental-health URLs | HTTP 403 | Used WebFetch text + `.webfetch.md` archive notes. |

### Not used as VA lab sources

- Third-party directories (TapWaterData and similar).
- Invented private-well acceptance claims for commercial rows.
