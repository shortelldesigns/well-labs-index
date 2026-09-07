# Well Labs Index

Static first version of a U.S. directory for private well owners.

**Homepage line:** Find a state-certified lab that will actually test your private well — then the treatment that matches the report.

**Byline:** Shortell Designs / Well Labs Index (public byline updated from personal name)

**Published:** 29 August 2026 (US/Pacific)

Open `index.html` in a browser. All links are relative; no build step is required.

## Rules (do not break these)

- Never invent a laboratory, phone number, address, price, certification, or statistic.
- If a field is not on the official source, write `unknown` or omit it and link the source.
- Do not add “best water filter” reviews.
- Every lab record in `data/*.json` must include a `source_url`.

## How to add a nightly page

This is a file-based site. A “nightly page” is a new or refreshed HTML file plus, if labs changed, an updated JSON file.

1. **Pick the official source.** Start with EPA’s state certification contact page:  
   <https://www.epa.gov/dwlabcert/contact-information-certification-programs-and-certified-laboratories-drinking-water>  
   Then open that state’s own certified-lab list (PDF, search tool, or HTML table).

2. **Fetch and archive.** Download the source to `data/sources/` with `curl`. For PDFs run `pdftotext -layout`. Record the URL, HTTP status, document date, and retrieve date in `SOURCES.md`.

3. **Transcribe, do not enrich.** Copy name, city, phone, address, and listed tests only as they appear. Do not fill gaps from Google or the lab’s marketing site. Mark missing fields `unknown`.

4. **Write JSON first.** Add or replace `data/labs-xx.json` with one object per lab, each with `source_url` and `source_document_date`. Keep a top-level `source` block describing limitations (for example “bacteriology only” or “does not state private-well acceptance”).

5. **Generate the HTML page.** Follow `labs/minnesota.html` (private-well-specific official list) or `labs/pennsylvania.html` (honest page when the official dump is accreditation-only). Use `css/site.css`. Add the state to `states.html` and the homepage only when the table has real, sourced rows.

6. **Cite dates.** Use the document’s own date plus the retrieve date. Site “last updated” is the calendar day you publish, in US/Pacific.

7. **Do not publish** municipal water-plant labs as homeowner labs unless the official source says they accept private-well samples.

8. **Log failures.** If a fetch fails, say so in `SOURCES.md` and on the state page. Do not substitute a stale unofficial list.

Optional later: a small script can turn `data/labs-xx.json` into the HTML table. This version’s tables were generated once from those JSON files.

## Layout

```
index.html                 homepage
states.html                MN + PA + OH + WI + TX + MI + ME + IN + NC live; others coming soon
test-private-well.html     CDC / EPA annual panel
iron-stains.html           what to test before buying treatment
rotten-egg.html            MDH hydrogen sulfide (anode vs well vs aquifer)
about.html                 methodology + commission disclosure
labs/minnesota.html
labs/pennsylvania.html
labs/ohio.html
labs/wisconsin.html
labs/texas.html            TCEQ PWS Lab Map Table (03/26/2026); LCRA verified
labs/michigan.html         EGLE SOM certified list (3/11/2026); EGLE Lab verified
labs/maine.html            Maine CDC commercial list (5/16/2026); HETL verified
labs/indiana.html          IDEM in-state list (revised 11/7/2025); IDOH verified
labs/north-carolina.html   NCSLPH commercial DW list (2026-09-06); State Lab via LHD verified
css/site.css
data/labs-mn.json
data/labs-pa.json
data/labs-oh.json
data/labs-wi.json
data/labs-tx.json
data/labs-mi.json
data/labs-me.json
data/labs-in.json
data/labs-nc.json
data/sources/              archived official files
SOURCES.md
RESULT.md
```

## Local check

```
cd well-lab-index
python3 -m http.server 8080
# open http://127.0.0.1:8080/
```

Or double-click `index.html`. Relative links work either way.
