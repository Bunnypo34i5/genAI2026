# Draft Report Outline v01: LegCo Data Access for Journalism and Public Engagement

**Date:** 12 February 2026  
**Version:** 01 (updated from outlineDraft.md with SCMP research findings)

---

## Title (working)
**"Connecting the Dots: How Fragmented LegCo Data Fails Journalists and Citizens — A Case Study in Healthcare Policy Coverage"**

---

## 1. Executive Summary
- Hong Kong's Legislative Council maintains extensive public data across 6+ separate databases, but fragmentation severely limits their usefulness for journalists and citizens
- SCMP journalists covering LegCo must manually search and cross-reference multiple unconnected systems to produce stories on healthcare policy, voting patterns, and legislative accountability
- Our investigation found that only voting data has a proper API; other databases (Bills, Members, Hansard) require manual web navigation
- We propose that a unified data platform with topic-based search would significantly improve both journalism and civic engagement with LegCo

---

## 2. Background: The Problem

### 2.1 The Data Landscape
- **LegCo Databases** ([legco.gov.hk](https://www.legco.gov.hk/en/visiting/library/legco-databases.html)): Members DB (since 1843), Bills DB (since 1844), Hansard DB (since 2012 for search), Rules DB, Research Publications DB, Members' Interests DB
- **Open LegCo** ([open-legco](https://www.legco.gov.hk/general/english/open-legco/open-data.html)): Voting results OData API, Hansard API, Bills API, Questions API, Webcast API
- **DATA.GOV.HK** ([data.gov.hk](https://data.gov.hk/en-datasets/provider/legco)): Portal with LegCo datasets, CKAN API
- See: `dataReport.md` for full technical analysis

### 2.2 Who Needs This Data?
- **Journalists**: SCMP politics team (Jeffie Lam, Matthew Cheng, Willa Wu) and health team (Emily Hung) regularly need LegCo data for coverage — see `JournalistNeeds.md`
- **Citizens**: Patients, caregivers, and advocates trying to track healthcare policy (e.g. rare disease drug subsidies)
- **Researchers**: Policy analysts studying voting patterns and legislative effectiveness

### 2.3 The Core Problem
- **No unified search** across all LegCo databases
- **No entity linking** — member IDs, bill references, and meeting dates are not standardised across systems
- **API gaps** — only voting results and a few newer databases have proper APIs; core systems (Members DB, Bills DB) still rely on legacy web interfaces
- **No topic-based access** — impossible to query "all LegCo activity on healthcare" or "all LegCo activity on rare diseases"

---

## 3. Evidence: What SCMP Coverage Reveals About Data Gaps

### 3.1 Healthcare Policy Coverage
Journalists covering healthcare policy must piece together data from multiple sources:

| Story Type | Data Needed | Sources Required | Difficulty |
|---|---|---|---|
| Drug subsidy reform | LCQ replies, panel papers, budget data | info.gov.hk + legco.gov.hk + data.gov.hk | High |
| Hospital fee changes | Panel discussion records, voting results | Hansard DB + Voting API + FC papers | High |
| eHealth system review | Committee papers, budget allocations, progress reports | Multiple panel papers (PDF) | Very High |
| Lawmaker accountability | Attendance, voting records, interests | Members DB + Voting API + Interests DB | Very High |

### 3.2 Key SCMP Articles Demonstrating the Problem
- **Ombudsman archives removed** ([SCMP, May 2025](https://www.scmp.com/news/hong-kong/society/article/3310959/outcry-among-lawmakers-hong-kong-ombudsman-removes-years-archived-reports)): Reduction of public access from 10 years to 3 years — shows the fragility of public data access
- **LegCo accountability reforms** ([SCMP, Apr 2025](https://www.scmp.com/news/hong-kong/politics/article/3307995/hong-kongs-legco-plans-require-meeting-attendance-voting-and-regular-reports)): New rules for attendance and work reports — but where will this data be published?
- **Finance Committee scrutiny** ([SCMP, Dec 2024](https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3291222/hong-kong-lawmakers-spent-2-hours-average-each-funding-plan-discussed)): Journalists had to calculate the 2-hour average manually from fragmented records

### 3.3 Healthcare-Specific Coverage Gaps
- **Fast-track drug approval** ([SCMP](https://www.scmp.com/news/hong-kong/health-environment/article/3326039/hong-kong-authorities-eye-fast-track-approval-option-life-saving-drugs)): Journalists need to track regulatory changes but there is no structured dataset linking policy announcements to legislative actions
- **Rare disease support** ([SCMP](https://scmp.com/comment/letters/article/3211467/review-drug-criteria-help-hongkongers-rare-diseases)): Letters to editor highlight public frustration, but citizens cannot easily find relevant LegCo discussions

---

## 4. The Three Data Sources: Detailed Assessment

### 4.1 LegCo Databases (Library System)
| Database | API Available | Data Format | Usability for Journalists |
|---|---|---|---|
| Members DB | No | ASPX web | Poor — no export, no bulk access |
| Bills DB | Yes (new) | JSON | Improved — API available |
| Hansard DB | Yes (new) | JSON/XML | Improved — API from 6th LegCo |
| Rules DB | No | Static HTML | Poor |
| Research Publications | No | Angular SPA | Poor |
| Members' Interests | No | HTML | Poor |

### 4.2 Open LegCo / Open Data
| API | Coverage | Usefulness |
|---|---|---|
| Voting Results OData | 5th LegCo onwards | High — well-structured, proper API |
| Hansard API | 6th LegCo onwards | High — full-text search possible |
| Bills API | All terms (JSON by term) | Medium — data available but not linked |
| Webcast API | 5th LegCo onwards | Medium — useful for multimedia |
| Questions API | Available | Medium — useful for Q&A tracking |

### 4.3 DATA.GOV.HK
- Central portal with LegCo datasets
- CKAN API for discovery
- Limited depth — mostly redirects to LegCo's own systems
- Not well-integrated with LegCo's own databases

---

## 5. Room for Improvement

### 5.1 Hypothesis
**Main hypothesis:** Improving the interconnection and API access of LegCo data sources would significantly enhance journalists' ability to cover legislative activities — especially healthcare policy — and would improve citizens' ability to track and engage with policy decisions affecting them.

### 5.2 Specific Improvements Needed
1. **Unified search API** — Single endpoint to search across Members, Bills, Hansard, Voting, and Committee papers
2. **Entity resolution** — Standardised IDs for members, bills, meetings, and committees across all databases
3. **Topic-based filtering** — Ability to query by policy area (healthcare, housing, education, etc.)
4. **Real-time notifications** — Alert system for new content related to specific topics or members
5. **Linked data** — Connect votes to debates to bills to committee papers

### 5.3 Comparative Examples
- **UK Parliament**: [data.parliament.uk](https://www.data.parliament.uk/) — unified API with linked data across all parliamentary activities
- **US Congress**: [congress.gov API](https://api.congress.gov/) — comprehensive, well-documented API with topic classification
- **Taiwan LegCo**: Open legislative data with structured bill tracking

---

## 6. Government Enquiries

### 6.1 Questions for LegCo Secretariat (Code on Access to Information)
1. What plans does LegCo have to implement a unified search API across all its databases?
2. What is the current usage data for the Open Data portal (number of API queries, downloads)?
3. Has any feasibility study been conducted on linking member IDs across databases?
4. What resources are allocated to maintaining and improving the open data infrastructure?
5. Why do key databases (Members, Rules, Research Publications) still lack API access?

### 6.2 Questions for Digital Policy Office
1. How does the government plan to improve cross-referencing between LegCo datasets and DATA.GOV.HK?
2. What standards are required for government data to be published on data.gov.hk?

### 6.3 Anticipated Answers and Follow-up Strategy
- If LegCo says "we have the Open Data portal already" — follow up with evidence that most databases still lack APIs
- If they cite budget constraints — ask for the current budget allocation for data infrastructure
- If they point to data.gov.hk — note that it mostly redirects to LegCo's own systems without added value

---

## 7. Complaints and Follow-up
- If government response is inadequate, consider a formal complaint about data accessibility
- The Ombudsman has demonstrated that data access can be reduced (archival reports case) — argue for guaranteed minimum access standards
- Draft a letter to the editor (SCMP) on LegCo data accessibility

---

## 8. Suggestions for Media Investigation and Coverage

### 8.1 Story Angles
1. **"Why can't you search LegCo like you search Google?"** — The fragmentation problem
2. **"The data deficit in healthcare policymaking"** — How scattered data undermines evidence-based policy scrutiny
3. **"Following the money at LegCo"** — How hard it is to link budget approvals to policy outcomes
4. **"Hong Kong vs the world"** — Comparing LegCo's data infrastructure to UK Parliament and US Congress

### 8.2 Potential Letter to Editor (SCMP)
- Frame: "As citizens concerned about healthcare policy, we found that LegCo's data systems make it unnecessarily difficult to track how our representatives are handling drug subsidies and rare disease support"
- Reference specific data gaps documented in this report
- Propose specific, achievable improvements

---

## 9. References

### Project Documents
- `JournalistNeeds.md` — SCMP reporter profiles, coverage analysis, and journalist data needs
- `dataReport.md` — Detailed technical report on LegCo data infrastructure
- `WebSearchReport.md` — AI web search results (5 rounds) on LegCo data and healthcare policy
- `public-info.md` — Overview of sources and rare disease policy context
- `Followup5Feb.md` — Next steps: define use case, map policy gaps
- `dataExplore.md` — Initial data exploration notes

### Key External Sources
- [LegCo Open Data Portal](https://www.legco.gov.hk/general/english/open-legco/open-data.html)
- [LegCo Databases](https://www.legco.gov.hk/en/visiting/library/legco-databases.html)
- [DATA.GOV.HK — LegCo datasets](https://data.gov.hk/en-datasets/provider/legco)
- [SCMP — Legislative Council of Hong Kong](https://www.scmp.com/topics/legislative-council-hong-kong)
- [LegCo Hansard API](https://www.legco.gov.hk/en/open-legco/open-data/hansard-database.html)
- [LegCo Bills API](https://www.legco.gov.hk/en/open-legco/open-data/bills-database.html)
- [LegCo Webcast API](https://www.legco.gov.hk/en/open-legco/open-data/webcast-api.html)
- [LegCo Questions API](https://www.legco.gov.hk/en/open-legco/open-data/questions-at-council-meetings.html)

---

## Comments and Feedback

> **Teacher:** [Add comments here]

> **Students:** [Add comments or questions here]

---

*Draft prepared 12 February 2026. Based on SCMP coverage analysis, LegCo Open Data review, and project research.*
