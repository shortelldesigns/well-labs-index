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
