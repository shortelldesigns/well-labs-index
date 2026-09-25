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

## Georgia — 12 September 2026 (US/Pacific)

- EPD Drinking Water hub: https://epd.georgia.gov/watershed-protection-branch/drinking-water
- Chemical monitoring labs PDF (revised January 9, 2025): https://epd.georgia.gov/document/pdf/laboratoriescertifiedbygeorgiachemicalmonitoring2025/download
- Microbiological monitoring labs PDF (revised January 9, 2025): https://epd.georgia.gov/document/pdf/laboratoriescertifiedbygeorgiamicrobiologicalmonitoring2025/download
- DPH Well Water: https://dph.georgia.gov/environmental-health/well-water
- DPH well testing fact sheet: https://dph.georgia.gov/document/fact-sheets/envhealthchemhazwell-water-fact-sheet0723pdf/download
- DPH County Environmental Health contacts: https://dph.georgia.gov/contacts/environmental-health
- UGA AESL water analyses: http://aesl.ces.uga.edu/water.html
- UGA Extension county offices: https://extension.uga.edu/county-offices.html
- Archived copies: data/sources/ga-chem-labs-2025-01-09.pdf|.txt, data/sources/ga-micro-labs-2025-01-09.pdf|.txt
- Page: labs/georgia.html · data: data/labs-ga.json
- Notes: 14 in-state commercial rows; GA EPD lab omitted; out-of-state omitted; UGA AESL W33C via Extension verified; County EH bacteria path noted as may-be-available.

## Kentucky — 13 September 2026 (US/Pacific)

Retrieve date: **13 September 2026** (US/Pacific).

### Succeeded

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| DOW Drinking Water Lab Certification Program | https://eec.ky.gov/Environmental-Protection/Water/PermitCert/LabCert/Pages/Drinking-Water-Lab-Certification-Program.aspx | Retrieved 13 September 2026 | Official program hub. |
| 2025 KY Certified Drinking Water Laboratory List (Greenup CHD mirror) | https://greenupchdky.gov/wp-content/uploads/2025/11/KY-Certified-DW-Laboratory-List.pdf | Revised 4/28/2025 | Same title/date as DOW list. Archived `data/sources/ky-certified-dw-labs-2025-04-28.pdf|.txt` (also kept greenup-named copies). |
| Greenup CHD water-testing laboratories | https://greenupchdky.gov/water-testing-laboratories/ | Retrieved 13 September 2026 | Links the certified list; example LHD private-well/cistern coliform sampling description. |
| DOW Water Well Information for Homeowners | https://eec.ky.gov/Environmental-Protection/Water/GW/Pages/GWOwnerAssist.aspx | Retrieved 13 September 2026 | Annual testing; contact certified lab; local health department after floods. |
| UK Extension ENRI — Well Treatment | https://water.mgcafe.uky.edu/welltreatment | Retrieved 13 September 2026 | Annual bacteria, nitrates, pH, TDS; use state certified lab; points to DOW list. |
| HydroAnalytical well water | https://www.hydroanalytical.com/well-water-information | Retrieved 13 September 2026 | Well water package (metals, anions, pH, total coliform, E. coli). |
| HydroAnalytical contact / about | https://www.hydroanalytical.com/contact · https://www.hydroanalytical.com/about | Retrieved 13 September 2026 | Street 2413 Nashville Road Ste. 100; sample collection/pickup noted on about. |
| Marshall County Health Department water testing | https://www.marshallcohealthdepartment.com/2020/water-testing/ | Page last updated 1-26-2026; retrieved 13 September 2026 | Western KY Regional Lab private well bacterial testing. Fee on county page — not copied as statewide price. |
| CHFS Local Health Departments | https://www.chfs.ky.gov/agencies/dph/dafm/pages/lhd.aspx | Retrieved 13 September 2026 | LHD directory links. |
| KHDA Find Your Local Health Department | https://khda-ky.org/find-your-local-health-department/ | Retrieved 13 September 2026 | County map finder. |

### Failed or incomplete (Kentucky)

| Attempt | URL | What happened | What we did instead |
| --- | --- | --- | --- |
| Official DOW Documents PDF | https://eec.ky.gov/Environmental-Protection/Water/PermitCert/LabCert/Documents/KYCertifiedDWLaboratoryList.pdf | HTTP 404 / unavailable at retrieve time | Used Greenup CHD mirror PDF (same title, Revised 4/28/2025). |
| Statewide LHD fee | various | Fees vary by county | No statewide price on public HTML; Marshall County fee noted only as “confirm locally.” |

### Directory choices (Kentucky)

| Choice | Detail |
| --- | --- |
| In-state commercial/regional | 16 labs tabulated (KY00030, 35, 44, 47, 50, 60, 61, 66, 67, 72, 74, 76, 78, 89, 90, 08031). |
| Verified paths | HydroAnalytical well package; Western KY Regional Lab / Marshall County bacterial testing; ask LHD about sampling. |
| Omitted | Municipal/utility plant labs; KY Division of Laboratory Services (KY00033); ESB Centralized Lab (KY00041); all out-of-state KY9xxxx / KY98026. |
| Prices | Intentionally omitted. |

### Page / data

- Page: labs/kentucky.html · data: data/labs-ky.json

## Alabama — 14 September 2026 (US/Pacific)

Retrieve date: **14 September 2026** (US/Pacific).

### Succeeded

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| ADEM Drinking Water Laboratory Certification Program | https://adem.alabama.gov/water/drinking-water-branch/information-public-water-systems/adem-drinking-water-laboratory-certification-program | Retrieved 14 September 2026 | Consumers may use certified labs to test private wells; lists mix commercial and water-system labs. |
| Certified Bacteriological Labs PDF | https://adem.alabama.gov/programs/water/waterforms/BacteriologicalLabs.pdf | Revised October 30, 2023 | Archived `data/sources/al-bact-labs-2026-09-14.pdf|.txt`. |
| In-State Certified Chemical Labs PDF | https://adem.alabama.gov/programs/water/waterforms/InStateChemicalLabs.pdf | Revised November 6, 2023 | Archived `data/sources/al-instate-chem-labs-2026-09-14.pdf|.txt`. |
| Out-of-State Certified Chemical Labs PDF | https://adem.alabama.gov/sites/default/files/2025-10/OutofStateChemicalLabs_0.pdf | Revised October 03, 2025 | Cite/link only; omitted from main table. Archived `data/sources/al-outofstate-chem-labs-2025-10.pdf|.txt`. |
| Certified PFAS Labs PDF | https://adem.alabama.gov/sites/default/files/2025-10/CertifiedPFASLabs.pdf | Updated October 03, 2025 | Optional; all labs out-of-state. Archived `data/sources/al-pfas-labs-2025-10.pdf|.txt`. |
| ADPH Well Water | https://www.alabamapublichealth.gov/environmental/well-water.html | Retrieved 14 September 2026 | County health dept / BCL bacterial path. |
| ADPH private water collection instructions | https://www.alabamapublichealth.gov/bcl/assets/privatewaterinstructionsandsampleform.pdf | ADPH CL-27 / Rev. 05-24 | Total coliform incl. E. coli; BCL does not do chemical analysis of private wells; fee currently waived (confirm). Archived `data/sources/al-adph-privatewater-instructions-2026-09-14.pdf|.txt`. |
| ADPH Bureau of Clinical Laboratories | https://www.alabamapublichealth.gov/bcl/ | Retrieved 14 September 2026 | Hub for BCL. |
| ACES — Where to Get Your Well Water Tested | https://www.aces.edu/blog/topics/private-well-program/where-to-get-your-well-water-tested/ | Posted February 17, 2021; retrieved 14 September 2026 | County HD bacterial path + ADEM certified labs for chemical; includes county contacts. |

### Failed or incomplete (Alabama)

| Attempt | URL | What happened | What we did instead |
| --- | --- | --- | --- |
| ADPH health departments finder | https://www.alabamapublichealth.gov/about/health-departments.html | Soft HTTP 200 with 404 page body | Noted on page; used ACES county list + ADPH Well Water. |
| ADPH locations (linked from Well Water) | https://www.alabamapublichealth.gov/about/locations.html | Soft HTTP 200 with 404 page body | Same — ACES county list. |
| ADPH wellwater.pdf asset | https://www.alabamapublichealth.gov/environmental/assets/wellwater.pdf | Soft 404 HTML | ACES step-by-step guide linked from ADPH Well Water instead. |

### Directory choices (Alabama)

| Choice | Detail |
| --- | --- |
| In-state commercial | 10 labs tabulated (ERA, Guardian, Living Water, Pace Decatur/Tuscaloosa/Mobile, Polyenvironmental, SET Decatur/Florence, Sutherland). |
| Verified paths | ADPH county HD / BCL bacterial testing; ADEM-certified labs for chemical (call first). |
| Omitted | Municipal/utility plant labs; ADPH BCL branch rows from commercial table; Houston County Regional Water Lab; all out-of-state chemical; all PFAS-list labs. |
| Prices | Intentionally omitted (BCL form waiver noted as confirm-locally only). |

### Page / data

- Page: labs/alabama.html · data: data/labs-al.json

## South Dakota — 15 September 2026 (US/Pacific)

Retrieve date: **15 September 2026** (US/Pacific).

### Succeeded

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| DANR Laboratory Certification | https://danr.sd.gov/OfficeOfWater/DrinkingWater/LaboratoryCert.aspx | Retrieved 15 September 2026 | In-state: State Health Lab (Pierre), Sioux Falls PHL, Mid Continent Testing, American Engineering Testing; plus out-of-state labs. Archived `data/sources/sd-danr-lab-cert-2026-09-15.html|.txt`. |
| DANR Private Well Sampling | https://danr.sd.gov/OfficeOfWater/DrinkingWater/PrivateWellSampling.aspx | Retrieved 15 September 2026 | Bacteriological and chemical parameter guidance for private wells. Archived `data/sources/sd-danr-private-well-2026-09-15.html`. |
| DANR New Well Sampling Program | https://danr.sd.gov/OfficeOfWater/DrinkingWater/NewWellSamplingProgram.aspx | Retrieved 15 September 2026 | Optional program page. Archived `data/sources/sd-danr-new-well-sampling-2026-09-15.html`. |
| SD DOH Environmental Testing | https://doh.sd.gov/laboratory/environmental-testing/ | Content last updated July 9, 2026; retrieved 15 September 2026 | Private persons: get kit from DOH or special location; DANR private-well info linked. Contact Rea Riggle. Archived `data/sources/sd-doh-environmental-testing-2026-09-15.html|.txt`. |
| SD DOH Test a Private Well | https://doh.sd.gov/laboratory/environmental-testing/test-a-private-well/ | Content last updated September 14, 2026; retrieved 15 September 2026 | Sample bottle order form; fee information included with bottles; County Extension also distributes bottles. Archived `data/sources/sd-doh-private-well-2026-09-15.html|.txt`. |
| SD DOH Environmental Testing Fees | https://doh.sd.gov/laboratory/environmental-testing/environmental-testing-fees/ | Content last updated September 14, 2026; retrieved 15 September 2026 | Official fee schedule (inorganic, micro, organics, radiochemistry). Linked from directory; dollar amounts not republished on public HTML. Archived `data/sources/sd-doh-environmental-testing-fees-2026-09-15.html|.txt`. |

### Failed or incomplete (South Dakota)

| Attempt | URL | What happened | What we did instead |
| --- | --- | --- | --- |
| Commercial private-well acceptance | Mid Continent; American Engineering Testing | No official page confirmed private-well acceptance | Marked unknown — call first. |
| Sioux Falls PHL private-well path | DANR + DOH pages | Municipal/public health; private-well acceptance not confirmed for homeowners | Short card/note only; not a commercial table row. |
| Republish DOH fee table | Environmental Testing Fees | Fees verified on official page but may change | Link only; confirm with lab. |

### Directory choices (South Dakota)

| Choice | Detail |
| --- | --- |
| In-state commercial | 2 labs tabulated (Mid Continent Testing Laboratory; American Engineering Testing). |
| Verified path | SD DOH Public Health Laboratory / Environmental Health Laboratory private-person kits (State Health Lab on DANR list). |
| Documented separately | Sioux Falls Public Health Laboratory (public health note). |
| Omitted | All out-of-state labs on DANR Laboratory Certification page. |
| Prices | Intentionally omitted from public HTML; official fees page linked. |

### Page / data

- Page: labs/south-dakota.html · data: data/labs-sd.json

## Tennessee — 16 September 2026 (US/Pacific)

Retrieve date: **16 September 2026** (US/Pacific).

### Succeeded

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| TDEC Laboratory Certification Program | https://www.tn.gov/environment/program-areas/wr-water-resources/water-quality/drinking-water-redirect/lab-certification-program.html | Retrieved 16 September 2026 | Links to certified commercial and microbiological PDFs. Archived `data/sources/tn-lab-cert-program-2026-09-16.html`. |
| TDEC Certified Commercial Labs PDF | https://www.tn.gov/content/dam/tn/environment/water/drinking-water-unit/wr_wq_dw_certified-commercial-labs.pdf | Footer date 03/17/2026 | In-state commercial/independent/university + military/federal + out-of-state. Archived `data/sources/tn-certified-commercial-labs-2026-09-16.pdf|.txt`. |
| TDEC Certified Microbiological Labs PDF | https://www.tn.gov/content/dam/tn/environment/water/drinking-water-unit/wr_wq_dw_certified-microbiological-labs.pdf | Retrieved 16 September 2026 | Broader micro roster (many utility plants). Archived `data/sources/tn-certified-micro-labs-2026-09-16.pdf|.txt`. |
| TDH Division of Laboratory Services | https://www.tn.gov/health/lab.html | Retrieved 16 September 2026 | Environmental Microbiology accepts private wells; Chemistry lists private wells among typical sources. Contacts Kristin Dunaway 615-262-6337; Chemistry bottle orders TDOH-EnvLogin / 615-262-6346. Archived `data/sources/tn-tdh-lab-2026-09-16.html|.txt`. |
| TDH Well Water Test Kit Instructions PDF | https://www.tn.gov/content/dam/tn/health/documents/WellWaterTestKitInstructions.pdf | V1. 10/3/2024 | Home coliform color kit guidance; Waterborne.Health@tn.gov / 615-532-7111. Archived `data/sources/tn-well-water-test-kit-instructions-2026-09-16.pdf|.txt`. |
| Williamson County Well Water Testing flyer | https://williamsoncounty-tn.gov/DocumentCenter/View/22926/Well-Water-Testing-Flyer | Retrieved 16 September 2026 | Corroborates TDH Division of Laboratory Services testing at 630 Hart Lane; supply request TDOH-ENVLogin.Health@tn.gov or 615-262-6337. Archived `data/sources/tn-williamson-well-flyer-2026-09-16.pdf|.txt`. |

### Failed or incomplete (Tennessee)

| Attempt | URL | What happened | What we did instead |
| --- | --- | --- | --- |
| Private Water Supply hub (linked from kit PDF as “Private Water Supply (tn.gov)”) | Common TDH healthy-homes paths | HTTP 404 at several guessed paths | Used TDH lab page + Williamson flyer + kit PDF as working sources. |
| Stale health.tn.gov commercial PDF | https://www.tn.gov/content/dam/tn/health/documents/wr_wq_dw_approved-commercial-labs.pdf | Rev ~08/03/2017; expired cert dates | Archived for contrast only; **not** used for the directory table. Prefer TDEC `wr_wq_dw_certified-commercial-labs.pdf` (03/17/2026). |
| Older micro PDF path | https://www.tn.gov/content/dam/tn/environment/water/drinking-water-unit/wr_wq_dw_approved-microbiological-labs.pdf | HTTP 404 | Used `wr_wq_dw_certified-microbiological-labs.pdf` from the LCP page. |
| Commercial private-well acceptance | 10 commercial rows | No official page confirmed homeowner acceptance | Marked unknown — call first. |

### Directory choices (Tennessee)

| Choice | Detail |
| --- | --- |
| In-state commercial | 10 labs tabulated from TDEC commercial PDF (03/17/2026). |
| Verified path | TDH Environmental Microbiology (private wells / Total Coliform–E. coli) + Chemistry Laboratory (private wells among typical sources). |
| Omitted | BNH AEDC (Arnold AFB); DOE Y-12 CNS; NAS Arnold AFB WTP Micro Lab; all out-of-state commercial-PDF labs. |
| Prices | Intentionally omitted; confirm with TDH or the lab. |

### Page / data

- Page: labs/tennessee.html · data: data/labs-tn.json

## West Virginia — 17 September 2026 (US/Pacific)

Retrieve date: **17 September 2026** (US/Pacific).

### Succeeded

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| OLS Laboratory Certified Parameter List PDF | https://dhhr.wv.gov/ols/labs/Documents/Environmental%20Chemistry/waterqualitylabs%20%282026%29%20-%20Updated%20List%20%288-20-26%29.pdf | Updated 8/20/2026 (footer Thursday, August 20, 2026; 104 pages) | Primary roster. Archived `data/sources/wv-ols-certified-labs-2026-08-20.pdf|.txt`. |
| OEHS certified labs listing page | https://oehs.wvdhhr.org/eed/data-management/water-quality-laboratories-certified-in-west-virginia/ | Retrieved 17 September 2026 | Hub linking the certified list. Archived `data/sources/wv-ols-listing-page-2026-09-17.html|.txt`. |
| OLS Environmental Microbiology | https://dhhr.wv.gov/ols/labs/Pages/EnvironmentalMicrobiology.aspx | Retrieved 17 September 2026 | Tests private / individual households; prefer county health department collection; OLS bottles; 30-hour hold. Archived `data/sources/wv-ols-env-microbiology-2026-09-17.html|.txt`. |
| OLS Environmental Chemistry | https://dhhr.wv.gov/ols/labs/Pages/EnvironmentalChemistry.aspx | Retrieved 17 September 2026 | Support to private well owners; bottle order 304-965-2694 / Apr 2026 form. Archived `data/sources/wv-ols-env-chemistry-2026-09-17.html|.txt`. |
| Bottle request form (Chemistry, Apr 2026) | https://dhhr.wv.gov/ols/labs/Documents/Environmental%20Chemistry/Bottle_Request_Form_With%20Fees%206.0_Apr2026.pdf | Apr 2026 | Archived `data/sources/wv-ols-bottle-request-form-apr2026.pdf|.txt`. Fees not republished on HTML. |
| Microbiology bottle request | https://dhhr.wv.gov/ols/labs/Documents/Environmental%20Micro/Bottle_Request_Form.pdf | Retrieved 17 September 2026 | Archived `data/sources/wv-ols-micro-bottle-request.pdf|.txt`. |
| Information for Private Well Owners pamphlet | https://dhhr.wv.gov/ols/labs/Documents/Environmental%20Chemistry/Water%20Pamphlet.pdf | Retrieved 17 September 2026 | Archived `data/sources/wv-ols-private-well-pamphlet.pdf|.txt`. |
| OEHS Individual Water Supplies | https://oehs.wvdhhr.org/phs/public-health-sanitation/individual-water-supplies/ | Retrieved 17 September 2026 | Rules/guidance hub. Archived `data/sources/wv-individual-water-supplies-2026-09-17.html|.txt`. |
| Local health departments map | https://dhhr.wv.gov/localhealth/Pages/Map.aspx | Linked from OLS | Preferred first contact for private-well bacteriological sampling per OLS Microbiology page. |

### Failed or incomplete (West Virginia)

| Attempt | URL | What happened | What we did instead |
| --- | --- | --- | --- |
| Older certified-labs PDF (5/14/2026) | https://dhhr.wv.gov/ols/labs/Documents/Environmental%20Chemistry/waterqualitylabs%20%282026%29%20-%20Updated%20List%20%285-14-26%29.pdf | Not needed — 8/20/2026 PDF retrieved successfully | Used 8/20/2026 PDF only. |
| Commercial phone numbers on OLS PDF | OLS certified parameter list | Not printed on the PDF | Marked phone unknown for all 6 commercial rows. |
| Commercial private-well acceptance | 6 commercial rows | No official page confirmed homeowner acceptance | Marked unknown — call first. |
| County Extension private-well kit path | Extension search | No independently verified statewide Extension kit path found beyond OLS / LHD / OEHS materials | Linked OLS + local health map + OEHS Individual Water Supplies only. |

### Directory choices (West Virginia)

| Choice | Detail |
| --- | --- |
| In-state commercial | 6 labs tabulated from OLS PDF 8/20/2026 (Advanced Analytical Solutions; Analabs; Pace Beaver; Pace Morgantown; Standard Laboratories Lab 67; Sturm Environmental Services). |
| Verified path | OLS Environmental Microbiology (private / individual households via county health department preferred) + OLS Environmental Chemistry (private well owners). |
| Omitted | 13 municipal/utility water-plant labs; WV Dept. of Agriculture Moorefield field office; OLS Chemistry/Microbiology/District (in verified path); 27 out-of-state labs. |
| Prices | Intentionally omitted; confirm with OLS or the lab. |

### Page / data

- Page: labs/west-virginia.html · data: data/labs-wv.json

## Oklahoma (added 18 September 2026)

Retrieve date: **18 September 2026** (US/Pacific).

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| DEQ Accredited_Labs_2026 GIS layer | https://gis.deq.ok.gov/server/rest/services/Accredited_Labs_2026/MapServer/6 | Layer name Accredited_Labs_2026; queried 18 Sep 2026 | curl REST query `Physical_State='OK'` → 100 in-state features. Archived `data/sources/ok-accredited-labs-2026-gis.json`. BusinessCa=Commercial → 19 rows; tabulated 17 after omitting state SELS + state agriculture. |
| DEQ Accredited Laboratory search | https://labaccreditation.deq.ok.gov/labaccreditation/ | Retrieved 18 Sep 2026 | Official search UI; notes “Commercial Sample” column for labs accepting private samples (column not present on GIS export). |
| Laboratory Accreditation hub | https://oklahoma.gov/deq/divisions/state-environmental-laboratory-services/laboratory-accreditation.html | Retrieved 18 Sep 2026 | Parameter verification: 405-702-1000 / labaccreditation@deq.ok.gov. |
| SELS Sample Collection Assistance | https://oklahoma.gov/deq/divisions/state-environmental-laboratory-services/sample-collection-assistance.html | Retrieved 18 Sep 2026 | Private TC and private nitrate+nitrite instruction links; kit contact 405-702-1000 / selsd@deq.ok.gov. |
| Water Test Request | https://www.deq.ok.gov/water-test-request/ | Retrieved 18 Sep 2026 | Private-well kit request form (coliform, nitrate/nitrite, lead, Water Wellness). Fee amounts not republished on site HTML. |
| Private Total Coliform & E. coli instructions PDF | https://oklahoma.gov/content/dam/ok/en/deq/documents/deqmainresources/Instruction_Private_TC_8999-GUI30-R02-102324.pdf | Doc id 8999-GUI30-R02-102324 | 28-hour hold; no Friday/weekend ship. Archived + pdftotext. |
| Private Nitrate + Nitrite instructions PDF | https://oklahoma.gov/content/dam/ok/en/deq/documents/deqmainresources/Private_Nitrate_Nitrite_R02-102324.pdf | R02-102324 | 48-hour hold; DEQ bottle required. Archived + pdftotext. |
| Private Water Well Analysis PDF | https://oklahoma.gov/content/dam/ok/en/deq/documents/executive-offices/fact-sheets/Private%20Well%20Analysis.pdf | Retrieved 18 Sep 2026 | Water Wellness panel parameters listed. Archived + pdftotext. |
| Home Water Testing PDF | https://oklahoma.gov/content/dam/ok/en/deq/documents/deqmainresources/HomeWaterTesting.pdf | Fact sheet 10/2024 | Annual private-well testing recommendations. Archived + pdftotext. |
| SELS Technical Assistance | https://oklahoma.gov/deq/divisions/state-environmental-laboratory-services/technical-assistance.html | Retrieved 18 Sep 2026 | No state rules requiring private-well testing; lenders often require TC/E. coli. |
| Laboratory Services Fees | https://oklahoma.gov/deq/divisions/state-environmental-laboratory-services/laboratory-services-fees.html | FY2027 schedule linked on page | Linked only; fee table not republished. |
| Oklahoma Well Owner Network (OSU) | https://water.okstate.edu/our-work/oklahoma-well-owner-network | Retrieved via search 18 Sep 2026 | Linked as Extension screening tool; OWON states certified tests go through DEQ. Not used as certified roster. |

### Omitted from Oklahoma commercial table

| Category | Count | Notes |
| --- | --- | --- |
| Municipal / utility (Muncipality/Municipal) | 9 | City of Lawton; OKC Hefner; Norman WTP; Edmond Micro; Midwest City; Durant; Tulsa Microbiology / Wet Chemistry / Instrumentation |
| State SELS principal lab | 1 | Documented in verified paths only |
| State agriculture lab | 1 | Ok Dept. of Ag-Laboratory |
| Permittee | 58 | Industrial permittee labs |
| Industrial / Induistrial | 12 | Spelling as printed on GIS |
| Field laboratory Accreditation | 1 | |
| Research | 1 | Oklahoma Water Survey/OU |
| Out-of-state | n/a | Filtered by Physical_State=OK; use official DEQ search |

### Page / data

- Page: labs/oklahoma.html · data: data/labs-ok.json
- Sources archive: data/sources/ok-*


## Nebraska (added 19 September 2026)

Retrieve date: **19 September 2026** (US/Pacific).

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| DHHS certified labs.pdf | https://dhhs.ne.gov/Public%20Health%20Lab%20Documents/certified%20labs.pdf | PDF metadata ModDate 22 May 2024; retrieved 19 Sep 2026 | Linked from Lab Certification Requirements “Certified Labs”. Archived `data/sources/ne-certified-labs-2026-09-19.pdf` + pdftotext. 5 rows total; tabulated 3 commercial/reciprocity. |
| Lab Certification Requirements | https://dhhs.ne.gov/Pages/Lab-Certification-Requirements.aspx | Retrieved 19 Sep 2026 | Program hub; Certified Labs action item. Archived HTML+txt. |
| Public Health Environmental Lab | https://dhhs.ne.gov/Pages/Public-Health-Lab.aspx | Retrieved 19 Sep 2026 | Main lab 402-471-2122; kits 471-3935; private well interpretation 471-4982; address 3701 South 14th St., Lincoln, NE 68502. |
| Private Citizen Water Test Kit Request Form | https://www.nebraska.gov/dhhs/water-test-kits/private.html | Retrieved 19 Sep 2026 | Bacteria (P/A or Numerical Count) + Nitrate kits; 30-hour coliform hold; Mon–Thu mail. |
| NPHEL Customer Service / Lab Price List | https://dhhs.ne.gov/Pages/Lab-Price-List.aspx | Retrieved 19 Sep 2026 | Order kits online or 402-471-3935; NPHEL kits required. Fees linked only — not republished. |
| DWEE: Sample private drinking water wells | https://dwee.nebraska.gov/news-events/press-releases/all-about-dwee-sample-private-drinking-water-wells | Retrieved 19 Sep 2026 | Corroborates DHHS online kit path; coliform/nitrate guidance. Not used as certified roster. |
| UNL Water — Drinking Water Testing | https://water.unl.edu/article/drinking-water-wells/water-testing | Retrieved 19 Sep 2026 | Extension context; points to DHHS certified list. Not used as roster. |

### Omitted from Nebraska commercial table

| Category | Count | Names |
| --- | --- | --- |
| Local health department | 1 | Central District Health Department (NE-04-01, Grand Island) |
| Municipal / utility | 1 | Metropolitan Utilities Districts (NE-04-04, Omaha) |

### Page / data

- Page: labs/nebraska.html · data: data/labs-ne.json

## New Hampshire (added 20 September 2026)

Retrieve date: **20 September 2026** (US/Pacific).

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| labs-private-wells.pdf | https://www.des.nh.gov/sites/g/files/ehbemt341/files/documents/labs-private-wells.pdf | Document header April 2026; PDF ModDate 20 Apr 2026; lab list footer updated 9/20/2024; retrieved 20 Sep 2026 | Primary roster: laboratories that serve NH private well users. Archived `data/sources/nh-labs-private-wells.pdf` + pdftotext. 10 rows on PDF; tabulated 9 commercial (NHDHHS in verified paths). |
| NHDES Private Wells | https://www.des.nh.gov/water/drinking-water/private-wells | Retrieved 20 Sep 2026 | Private-well hub; links guidance PDF and Be Well Informed. |
| Be Well Informed | https://www4.des.state.nh.us/DWITool/Welcome.aspx | Retrieved 20 Sep 2026 | Result interpreter / treatment guidance — not a lab roster. |
| NHELAP hub | https://www.des.nh.gov/water/drinking-water/new-hampshire-environmental-laboratory-accreditation-program | Retrieved 20 Sep 2026 | Program hub; points to Accredited Laboratory Search and private-wells guidance. |
| Accredited Laboratory Search | https://www4.des.state.nh.us/CertifiedLabs/Certified-Method.aspx | Retrieved 20 Sep 2026 | Live NHELAP database. HTML archived; live results not scraped into table. |
| WAL Program | https://www.dhhs.nh.gov/programs-services/environmental-health-and-you/water-analysis-laboratory-program | Retrieved 20 Sep 2026 | Homeowner Water Testing verified path. |
| WAL contact | https://www.dhhs.nh.gov/water-analysis-laboratory | Retrieved 20 Sep 2026 | 29 Hazen Drive, Concord NH 03301; Waterlab@dhhs.nh.gov; 603-271-3445. |
| Home Owner Container Request | https://www4.des.state.nh.us/DESOnestop/HOBottles.aspx | Retrieved 20 Sep 2026 | Kit/bottle request form including NH Well Water Test For Home Buyers. |

### Omitted from New Hampshire commercial table

| Category | Count | Names |
| --- | --- | --- |
| State public health lab (on PDF; covered in verified paths) | 1 | NHDHHS Public Health Laboratories |

### Page / data

- Page: labs/new-hampshire.html · data: data/labs-nh.json
- Sources archive: data/sources/nh-*

## Vermont (added 24 September 2026)

Retrieve date: **24 September 2026** (US/Pacific).

| Source | URL | Document / page date | Notes |
| --- | --- | --- | --- |
| VDH DW certified laboratory list PDF | https://www.healthvermont.gov/sites/default/files/document/lsid-phl-DW-certified-laboratory-list.pdf | June 11, 2026; metadata CreationDate 11 Jun 2026; ModDate 12 Jun 2026; retrieved 24 Sep 2026 | Full certified roster; green highlight = accept private samples. Archived `data/sources/vt-vdh-dw-certified-laboratory-list-2026-06-11.pdf` + pdftotext. |
| DEC Certified Laboratories for Landowner Water Quality Testing | https://dec.vermont.gov/drinking-water-and-groundwater-protection/wastewater-systems-and-potable-water-supply-program-2-0 | Retrieved 24 Sep 2026 | Primary private-well / landowner roster (table + map). 18 rows including VDH Laboratory; tabulated 17 commercial. |
| DEC interactive map | https://vtanr.maps.arcgis.com/apps/Embed/index.html?webmap=fa5dec59b193484f9bcf4ea1704c0c04 | Retrieved 24 Sep 2026 | Map URL archived. |
| VDH Drinking Water Testing | https://www.healthvermont.gov/lab/lab-testing/drinking-water-testing | Retrieved 24 Sep 2026 | Verified homeowner kit path hub. |
| VDH Forms & Ordering | https://www.healthvermont.gov/lab/forms | Retrieved 24 Sep 2026 | Webstore + kit order form + schedule notes. |
| VDH kit webstore | https://vdh.webapps.aidcvt.com/water-test | Retrieved 24 Sep 2026 | Online water/radon kit orders. |
| VDH Sample Drop-off | https://www.healthvermont.gov/lab/lab-testing/drinking-water-sample-drop-information | Retrieved 24 Sep 2026 | Lab hours + Local Health Office drop-off. |
| How to Test Your Drinking Water | https://www.healthvermont.gov/environment/drinking-water/how-test-your-drinking-water | Retrieved 24 Sep 2026 | Homeowner Testing Package guidance. |
| Private Water (Wells & Springs) | https://www.healthvermont.gov/environment/drinking-water/private-drinking-water | Retrieved 24 Sep 2026 | Private-well hub. |
| New Drilled Well Testing | https://www.healthvermont.gov/environment/drinking-water/new-drilled-well-testing-what-you-need-know | Retrieved 24 Sep 2026 | New-well path. |

### Omitted from Vermont commercial table

| Category | Count | Notes |
| --- | --- | --- |
| State public health lab (on DEC + PDF; covered in verified paths) | 1 | Vermont Department of Health Laboratory |
| VDH-certified labs not on DEC landowner table | many | Municipal/utility and other specialty rows (e.g. Champlain Water District). City of Rutland Water Laboratory is green on PDF (accept private samples) but not on DEC landowner table — PDF only. |

### Page / data

- Page: labs/vermont.html · data: data/labs-vt.json
- Sources archive: data/sources/vt-*
