# Journalist Needs: SCMP Coverage of LegCo and Data Access

**Date:** 12 February 2026  
**Purpose:** Identify what SCMP journalists cover about LegCo, what data they rely on, and how improved data access could support their work.

---

## 1. Key Topics and Issues Covered by SCMP on LegCo

### 1.1 LegCo Elections and Political Composition
- **2025 Legco Election** (7 Dec 2025): 90 seats contested, 31.9% turnout, 43.8% turnover of lawmakers
  - [2025 Legco election: meet the candidates](https://www.scmp.com/infographics/hong-kong/society/article/3334034/2025-legco-election-meet-your-candidates)
  - [4 incumbents lose seats as Hong Kong's Legco records 43.8% turnover](https://www.scmp.com/news/hong-kong/politics/article/3335573/4-incumbents-lose-re-election-hong-kongs-legco-sees-438-turnover)
  - [Surprises and defeats in Hong Kong Legco election – as it happened](https://www.scmp.com/news/hong-kong/politics/article/3335536/surprises-and-defeats-votes-tallied-hong-kong-legco-election)

### 1.2 Legislative Accountability and Transparency
- **New attendance/voting rules** (Apr 2025): Legco president proposed requiring lawmakers to attend meetings, participate in votes, and submit regular work reports
  - [Hong Kong's Legco plans to require meeting attendance, voting and regular reports](https://www.scmp.com/news/hong-kong/politics/article/3307995/hong-kongs-legco-plans-require-meeting-attendance-voting-and-regular-reports)
- **Finance Committee scrutiny**: Lawmakers spent on average 2 hours per funding application discussed in 2024, approving HK$250 billion across 58 applications
  - [Hong Kong lawmakers spent 2 hours on average on each funding plan discussed](https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3291222/hong-kong-lawmakers-spent-2-hours-average-each-funding-plan-discussed)
- **Ombudsman archives controversy** (May 2025): Archived reports reduced from 10 years to 3 years of public access, drawing lawmaker criticism
  - [Outcry among lawmakers as Hong Kong ombudsman removes years of archived reports](https://www.scmp.com/news/hong-kong/society/article/3310959/outcry-among-lawmakers-hong-kong-ombudsman-removes-years-archived-reports)

### 1.3 Budget and Fiscal Policy
- **2025-26 Budget debates**: Financial Secretary Paul Chan's budget drew criticism even from pro-establishment lawmakers; HK$87.2 billion deficit
  - [Budget 2025: pay freeze for Hong Kong public servants](https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3300132/budget-2025-can-hong-kongs-paul-chan-deliver-deficit-busting-plan)
  - [Legco patriots' budget criticism a warning that must be heard](https://scmp.com/opinion/hong-kong-opinion/article/3307073/legco-patriots-budget-criticism-warning-must-be-heard)

### 1.4 Healthcare Policy and LegCo
- **Medical fee reform**: New charges for non-urgent services (CT scans, labs); subsidy rate target reduced from 97.6% to 90% by 2030
  - [Hong Kong lawmakers urge clarity on fee waivers under new healthcare charges](https://scmp.com/news/hong-kong/health-environment/article/3306480/hong-kong-lawmakers-urge-clarity-fee-waivers-under-new-healthcare-charges)
  - [Heres all you need to know about Hong Kong's coming medical fee changes](https://www.scmp.com/news/hong-kong/health-environment/article/3304017/heres-all-you-need-know-about-hong-kongs-coming-medical-fee-changes)
- **Fast-track drug approval**: Government introducing "1+" mechanism for rare/severe disease drugs; processing time from 150 to 100 days
  - [Hong Kong authorities eye fast-track approval option for life-saving drugs](https://www.scmp.com/news/hong-kong/health-environment/article/3326039/hong-kong-authorities-eye-fast-track-approval-option-life-saving-drugs)
- **Rare disease drug subsidies**: Review of drug criteria to help patients; HK$15 prescription fee review to fund costly drugs
  - [Review drug criteria to help Hongkongers with rare diseases](https://scmp.com/comment/letters/article/3211467/review-drug-criteria-help-hongkongers-rare-diseases)
  - [Hong Kong reviews HK$15 prescriptions at public hospitals](https://www.scmp.com/news/hong-kong/health-environment/article/3301985/how-much-more-are-you-willing-pay-hong-kong-reviews-hk15-prescriptions)
- **eHealth+ system**: HK$1.4 billion upgrade; only <1% private sector data uploads; consent model reform
  - [Hong Kong health record plan in line for revamp to boost private sector data sharing](https://www.scmp.com/news/hong-kong/health-environment/article/3252275/80-hongkongers-are-using-citys-ehealth-record-scheme-authorities-say-most-arent-sharing-data-private)
- **Community Drug Programme**: Launching late 2026 in 4 pilot districts
  - [Hongkongers to get greater access to cheaper medicines under specific list of drugs](https://www.scmp.com/news/hong-kong/health-environment/article/3330957/hongkongers-get-greater-access-cheaper-medicines-under-specific-list-drugs)

### 1.5 Data Access and Open Government
- **LegCo records digitisation** (2013): Records dating back to 1877 made machine-readable (XML/PDF)
  - [Public gain greater access to Legco data as online records dating back to 1877 go online](https://www.scmp.com/news/hong-kong/article/1344903/public-gain-greater-access-legco-data-online-records-dating-back-1877)
- **Healthcare data sharing**: HA offering 200,000 patient records to biotech firms
  - [Hong Kong health authorities, Science Park offer 200,000 patients' data to biotech firms free of charge](https://www.scmp.com/news/hong-kong/health-environment/article/3257099/hong-kong-health-authorities-science-park-offer-200000-patients-data-biotech-firms-free-charge)

---

## 2. What Types of Data Do Journalists Need?

Based on SCMP coverage patterns, journalists covering LegCo need:

### 2.1 Voting and Attendance Data
- **Individual voting records** by member, by bill, by motion — to track consistency and accountability
- **Attendance records** at committee meetings — for stories on lawmaker performance
- **Voting patterns** across party lines — for political analysis
- **Current gap:** Voting data only available via OData API; no easy way to link votes to specific bills or debates

### 2.2 Legislative Process Data
- **Bill progression timelines** — from gazettal to passage, including committee stages
- **Amendment histories** — who proposed what changes and what was accepted/rejected
- **Finance Committee deliberation details** — time spent per application, approval rates
- **Current gap:** Bills DB has no API; manual web scraping required

### 2.3 Member Profile Data
- **Cross-referenced profiles** — linking voting records, speeches, interests declarations, committee memberships
- **Conflict of interest information** — members' interests register linked to voting behaviour
- **Current gap:** No unified member ID across databases; each system uses different identifiers

### 2.4 Healthcare-Specific Policy Data
- **Panel discussion records** — Health Services Panel debates and papers
- **Government replies to questions** — searchable database of LCQs on health topics
- **Budget allocations** — healthcare spending by programme, year-on-year
- **Drug subsidy data** — which drugs are subsidised, eligibility criteria, expenditure
- **Current gap:** Health panel papers scattered across legco.gov.hk; no structured dataset linking policy discussions to outcomes

### 2.5 Historical and Comparative Data
- **Long-term trends** — how policy positions evolved over multiple LegCo terms
- **Comparative data** — HK vs other jurisdictions (UK Parliament, US Congress, Singapore)
- **Hansard full-text** — searchable transcripts for fact-checking member statements
- **Current gap:** Hansard search only from 5th LegCo (2012); earlier records less accessible

---

## 3. Assessment: Can LegCo Data Sources Meet Journalist Needs?

| Journalist Need | LegCo Data Sources | Coverage | Gap |
|---|---|---|---|
| **Voting records** | Open LegCo OData API | Good (5th LegCo onwards) | Not linked to bills or debates |
| **Bill progression** | Bills DB (web only) | Good (since 1844) | No API access |
| **Member profiles** | Members DB (web only) | Good (since 1843) | No cross-referencing; no API |
| **Hansard/speeches** | Hansard DB + Open Data API | Moderate (6th LegCo onwards for API) | Limited historical coverage |
| **Interests register** | Members' Interests DB | Good | Not linked to voting data |
| **Committee papers** | LegCo website | Moderate | No structured dataset; PDF-heavy |
| **Healthcare policy** | Scattered across panels | Poor — fragmented | No topic-based aggregation |
| **Budget allocations** | FC papers, data.gov.hk | Moderate | Not easily cross-referenced |
| **Webcast/video** | Webcast OData API | Good | Not linked to agenda items in other DBs |
| **Real-time updates** | LegCo website | Poor | No notification or streaming API |

### Key Finding
LegCo maintains extensive data, but **fragmentation across 6+ siloed databases** means journalists must manually search and cross-reference multiple systems. The most critical gaps for journalism are:
1. **No unified search** across all LegCo data
2. **No entity linking** (member IDs, bill IDs) between databases
3. **No topic-based filtering** (e.g. "all LegCo activity on rare diseases")
4. **Limited API coverage** — only voting results and webcasts have proper APIs

---

## 4. SCMP Reporters Covering LegCo

### 4.1 Politics Team

| Reporter | Role | Expertise | Profile | Twitter |
|---|---|---|---|---|
| **Jeffie Lam** | News Editor, HK Politics | HK politics, constitutional and legislative issues, political analysis, aging population | [SCMP Profile](https://www.scmp.com/author/jeffie-lam) | [@jeffielam](https://twitter.com/jeffielam) |
| **Matthew Cheng** | Reporter | HK politics, general news | [SCMP Profile](https://www.scmp.com/author/matthew-cheng) | — |
| **Willa Wu** | Correspondent, City News | HK politics, society | [SCMP Profile](https://www.scmp.com/author/willa-wu) | — |

### 4.2 Health Team

| Reporter | Role | Expertise | Profile | Twitter |
|---|---|---|---|---|
| **Emily Hung** | Reporter, City Desk | HK health news and policies | [SCMP Profile](https://www.scmp.com/author/emily-hung) | [@tyhunghk](https://twitter.com/tyhunghk) |

### 4.3 Contact Information

- **SCMP Newsroom Phone:** +852 2565 2222
- **SCMP Editorial Hotline:** (852) 2680 8921
- **SCMP General Inquiries:** [Contact Page](https://www.scmp.com/contact-us)
- **SCMP Corporate:** [Corporate Contact](https://corp.scmp.com/contact-us/)
- **Physical Address:** 19/F, Tower 1, Times Square, 1 Matheson Street, Causeway Bay, Hong Kong
- **LegCo Enquiries:** enquiry@legco.gov.hk

### 4.4 Recent Articles by These Reporters on LegCo

**Jeffie Lam:**
- Covered 2025 Legco election extensively
- Profiled key political figures (Regina Ip's career, Emily Lau biography)
- Co-edited "Rebel City: Hong Kong's Year of Water and Fire" (SCMP/World Scientific)

**Matthew Cheng:**
- [Starry Lee secures Hong Kong Legco presidency](https://www.scmp.com/news/hong-kong/politics/article/3339124/hong-kongs-starry-lee-secures-legco-presidency-after-5-vote-win-over-ronick-chan)
- Beijing confidence in HK ability to handle Legco election
- Coverage of new Legco composition and presidency race

**Willa Wu:**
- [Tight race for Hong Kong's Legco presidency](https://www.scmp.com/news/hong-kong/politics/article/3339081/tight-race-hong-kongs-legco-presidency-parties-allow-free-vote)
- Legco election hopefuls scaling back campaigning after Tai Po fire
- Post-election coverage of new lawmakers

**Emily Hung:**
- [Hong Kong lawmakers urge clarity on fee waivers under new healthcare charges](https://scmp.com/news/hong-kong/health-environment/article/3306480/hong-kong-lawmakers-urge-clarity-fee-waivers-under-new-healthcare-charges)
- Hong Kong set to add hospital charges but widen safety net
- Coverage of medical fee reform and healthcare panel discussions

---

## 5. LegCo Open Data API Endpoints (for reference)

| API/Database | URL | Format | Status |
|---|---|---|---|
| **Voting Results OData** | [app.legco.gov.hk/vrdb/odata/vVotingResult](https://app.legco.gov.hk/vrdb/odata/vVotingResult?$top=10&$format=json) | OData/JSON | Working |
| **Hansard Database API** | [legco.gov.hk/en/open-legco/open-data/hansard-database.html](https://www.legco.gov.hk/en/open-legco/open-data/hansard-database.html) | JSON/XML | Working |
| **Bills Database API** | [legco.gov.hk/en/open-legco/open-data/bills-database.html](https://www.legco.gov.hk/en/open-legco/open-data/bills-database.html) | JSON | Working |
| **Webcast API** | [legco.gov.hk/en/open-legco/open-data/webcast-api.html](https://www.legco.gov.hk/en/open-legco/open-data/webcast-api.html) | OData | Working |
| **Questions at Council** | [legco.gov.hk/en/open-legco/open-data/questions-at-council-meetings.html](https://www.legco.gov.hk/en/open-legco/open-data/questions-at-council-meetings.html) | JSON/XML | Working |
| **Members Reference DB** | [data.gov.hk LegCo Members](https://data.gov.hk/en-data/dataset/legco-refdb-reference-database/resource/20b2d1d2-8b48-46e3-ab88-ba2ba1cab5a3) | JSON | Working |
| **DATA.GOV.HK (LegCo)** | [data.gov.hk/en-datasets/provider/legco](https://data.gov.hk/en-datasets/provider/legco) | REST/JSON | Working |
| **LegCo Topics Page (SCMP)** | [scmp.com/topics/legislative-council-hong-kong](https://www.scmp.com/topics/legislative-council-hong-kong) | Web | Active |

---

## 6. Suggestions for Contacting Reporters

1. **Prioritise Emily Hung** — She covers health policy AND LegCo panel discussions; directly relevant to the project's healthcare + data access angle
2. **Reach out to Jeffie Lam** — As politics editor, she can speak to the broader data access challenges journalists face when covering LegCo
3. **Use Twitter/X for initial contact** — Professional reporters are often more responsive to DMs on Twitter than cold emails
4. **Prepare a clear pitch** — Frame the project as "how can LegCo data be made more useful for journalists covering healthcare policy?" rather than a generic student request
5. **Reference specific articles** — Mention their published articles when reaching out to demonstrate you've done your homework

---

*Research conducted on 12 February 2026 using web search and SCMP topics page review.*
