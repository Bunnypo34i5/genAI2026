# Activity Log — Group 4 Fire Services Project

---

## 12 February 2026

### Session Summary
Comprehensive research and documentation session focused on the Wang Fuk Court fire, emergency alert systems, and fire safety training. Executed all tasks from `update12Feb.md`.

### Tasks Completed

#### 1. GoogleNotes.md — Created
- **Source:** [Google Doc](https://docs.google.com/document/d/1KHJv5TiUSB4fDAt5UniQZEVI0QuWQI3GghQI6EW5rZc/edit?usp=sharing)
- Fetched full contents from Google Doc (Tab 1 — Public Info Curation)
- Excluded Tab 2 (project report / outline) as instructed
- Captured 5 curated articles with facts, comments, and full texts:
  1. HK01 — Hongfuyuan Fire: Failed Fire Alarm Causes Public Panic (Luk Kan Yiu Shannon)
  2. SCMP — Failure of fire alarms in Tai Po (Chang Yan Tung Brookye)
  3. Storm.mg — Review of 7 Major Fires in HK in 30 Years (LU Haihong Iris)
  4. BBC — Final death toll placed at 168 (Yick Minny)
  5. IFSJ — Wang Fuk Court fire and global lessons for high-rise safety (Tu Yixin)

#### 2. Link Visits — Content Added to GoogleNotes.md
- Visited all 5 article links and fetched additional content
- Added detailed notes from each source including:
  - Full SCMP article: Anthony Lam (former FSD director) quotes on alarm failures
  - Full BBC article: Final death toll, demographics, arrests
  - Full IFSJ article: Comprehensive analysis including NFPA framework, renovation issues, residents' warnings timeline, corruption investigation, relief measures
  - Full HK01 article: Detailed fire alarm system explainer (manual vs automatic, FS251 certificates, legal requirements, "break-turn-pull-shoot" emergency steps)
  - Storm.mg article: 7 major fires timeline with causes and legislative reforms

#### 3. MoreInfoOnline.md — Created
- Performed web searches on SCMP, gov.hk, and the web
- Documented 11 key online sources with titles, links, relevance ratings, and notes
- Key findings:
  - **Independent Committee** established 12 Dec 2025 (Justice David Lok) — first meeting 5 Feb 2026 found "systemic problems"
  - **Emergency Alert System** (EAS): HK$150M system used only ONCE since 2020 launch — NOT activated during Wang Fuk Court fire
  - **FSD fire safety education**: 324 talks reaching 16,550 people in 2024 — question is whether Wang Fuk Court residents received any training
  - Public hearings scheduled **March 2026**
  - 200 sites ordered to remove scaffold netting post-fire

#### 4. outlineDraft01.md — Created
- Updated report outline with new focus on **emergency alert systems** and **fire safety training**
- New title: "When the Alarm Didn't Sound: Hong Kong's Emergency Alert and Fire Safety Training Failures..."
- Structured around two hard questions:
  1. What if the Emergency Alert System had been used during the fire?
  2. What if victims had received better training?
- Added sections on EAS analysis, FSD education programmes, investigation progress
- Included suggested questions for government enquiries (FSD and OFCA)
- Added media investigation angles and recommendations

#### 5. crawl_fsd_directory.py — Created and Executed
- Python program to crawl https://tel.directory.gov.hk/index_FSD_ENG.html
- Crawled 91 FSD offices/divisions
- Identified **23 HIGH-relevance teams** for project contact
- Key teams identified:
  - Fire Safety Command & Building Improvement Divisions
  - Public Safety and Communication Division
  - Licensing & Certification Command
  - Fire Protection Facilities Supervision Division
  - Outsourcing and Complaints Section
  - Mobilising and Communications Division
  - Prosecution Section
- Output: `fsd_directory_results.md` (structured report) and `fsd_directory_raw.json` (raw data)

#### 6. govEnquiries.md — Created
- 29 specific questions organized by FSD team
- Addressed to 7 FSD divisions with contact details (phone, email)
- Questions grouped by theme:
  - Emergency Alert System (Q22-Q25)
  - Fire Safety Training & Education (Q6-Q11, Q26-Q27)
  - Fire Alarm Systems & Contractor Oversight (Q12-Q17)
  - Building Safety Compliance (Q1-Q5)
  - Complaints Handling (Q18-Q21)
- Includes next steps for drafting formal enquiry letters

#### 7. activityLog.md — Created (this file)

### Files Created/Modified This Session
| File | Status | Description |
|---|---|---|
| `GoogleNotes.md` | NEW | Google Doc contents + link visit findings |
| `MoreInfoOnline.md` | NEW | Web search findings on investigation, EAS, training |
| `outlineDraft01.md` | NEW | Updated report outline v2 |
| `crawl_fsd_directory.py` | NEW | Python crawler for FSD directory |
| `fsd_directory_results.md` | NEW | Crawler output — teams to contact |
| `fsd_directory_raw.json` | NEW | Crawler raw data |
| `govEnquiries.md` | NEW | Questions for FSD teams |
| `activityLog.md` | NEW | This activity log |

### Key Research Findings

1. **Emergency Alert System is almost dormant** — HK$150M investment, used once in 5 years, not activated for the worst fire disaster in decades
2. **All 8 building fire alarms failed** — deactivated during renovation, false reports to FSD
3. **Residents were untrained** — didn't know alarms were manual, couldn't activate call points
4. **Systematic corruption** in renovation procurement — non-compliant materials substituted, falsified certificates
5. **Independent Committee** already found "systemic problems" — evidence to be disclosed in March 2026 hearings
6. **FSD education reach is limited** — 324 talks / 16,550 people for a city of 7.5M; unclear if Wang Fuk Court received any training

### Next Steps
- [ ] Draft formal enquiry letters based on `govEnquiries.md`
- [ ] Monitor Independent Committee hearings (March 2026)
- [ ] Follow up on SCMP/BBC/IFSJ for new articles
- [ ] Begin drafting report sections based on `outlineDraft01.md`
- [ ] Send ATIP (Code on Access to Information) requests to FSD and OFCA
- [ ] Prepare questions about EAS activation protocols for OFCA

---

## Previous Sessions

### 5 February 2026
- Reference: `Followup5Feb.md`
- Focus on fire safety education; locating responsible FSD team; Tai Po fire link

### Earlier Sessions
- Reference: `WebSearchReport.md` — 5 rounds of AI web search on FSD operations, equipment, training, Fire Safety Ordinance
- Reference: `public-info.md` — FSD operations, equipment, training, prevention, community engagement
- Reference: `outlineDraft.md` — First draft of report outline
