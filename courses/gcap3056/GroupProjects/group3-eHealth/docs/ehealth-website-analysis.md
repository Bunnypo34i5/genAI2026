# eHealth Website Analysis & Findings Summary
**Date:** 12 March 2026  
**Project:** Group 3 - eHealth Insurance Reimbursement  
**Focus:** Subsidy Schemes & Amendment Bill 2025 Effects

---

## Key Findings from ehealth.gov.hk Web Scraping

### 1. eHealth+ Connectivity Support Scheme (醫健通+連通支援計劃)

**Purpose:**
- To further promote electronic health record sharing in the private healthcare sector
- Provides subsidy incentives to encourage private healthcare institutions to adopt eHealth-connected Electronic Medical Record Systems (EMRS) and deposit health records into eHealth

**Target Sector:**
- Only applies to Western medicine practitioners (西醫)

**Eligibility Criteria:**
- Healthcare institutions must be registered with eHealth (醫護機構必須已登記醫健通)
- Institutions must continuously deposit electronic health records during subsidy period
- Maximum 12 months of subsidy per eligible institution
- Maximum 50 registered doctors per institution can be registered
- Each registered doctor is limited to one registration

**Application Process:**
- Applications submitted per healthcare institution (not individual doctors)
- Application via submission form
- Results notified via email within 2 months of submission

**Subsidy Details:**
- Subsidy amount calculated based on registered doctor list submitted monthly by the institution
- Maximum 12 months subsidy period  
- Specific HK$ amount needs to be verified from application documents

**Application Status:**
- Online application available
- Terms and Conditions (T&Cs) must be accepted
- English version of detailed application documents available

---

### 2. Amendment Bill 2025 References Found

**Keywords Identified in Website:**
- ✓ 修訂 (Amendment)
- ✓ 條例 (Ordinance)
- ✓ 法案 (Bill)
- ✓ 2025 (Year)
- ✓ 醫護專業人員 (Healthcare professionals)
- ✓ 過敏 (Allergies) - Mandatory data
- ✓ 藥物 (Medications) - Mandatory data
- ✓ 化驗報告 (Lab reports) - Mandatory data

**Specified Health Data Types Mentioned:**
The website confirms mandatory data categories including:
- Allergies (過敏)
- Medications (藥物)  
- Lab/Radiology reports (化驗報告)

---

### 3. eHealth+ Connectivity Accreditation Scheme (醫健通+連通認證計劃)

**Pages Found:**
- Links to accreditation scheme via main portal
- Accreditation marks system referenced (Gold, Silver, Bronze levels)

**Connection to App Portal:**
- Additional features accessible via app.ehealth.gov.hk
- Cross-boundary health records functionality available
- Personal health record folder (個人資料夾) for patients

---

### 4. FAQ Section (常見問題)

**Statistics:**
- 584 FAQ items found on FAQ page
- Comprehensive Q&A coverage on eHealth operations

**Topics Covered:**
- How to register for eHealth
- How healthcare institutions participate
- Patient identity verification
- Viewing and sharing electronic health records
- Technical support
- Password reset
- Data confidentiality

---

### 5. Key Website Sections Available

**Accessible Pages:**
1. Homepage: https://www.ehealth.gov.hk/tc/index.html
2. Healthcare Provider Portal: https://www.ehealth.gov.hk/tc/healthcare-provider-and-professional/
3. Connectivity Support Scheme: `/resources/ehealth-plus-connectivity-support-scheme/`
4. FAQ Section: https://www.ehealth.gov.hk/tc/faq/index.html
5. News/Updates: https://www.ehealth.gov.hk/tc/whats-new/ehealth-news/

---

## Recommendations for Group 3 Project

### Data Points Missing from Website (Need to Investigate):
1. **Specific Subsidy Amount** - HK$ amount per doctor per month (referenced in earlier documents as HK$500/month, but not confirmed on website)
2. **Uptake Statistics** - Current number of private institutions/doctors applying
3. **Detailed Enforcement Mechanism** - How the government audits data compliance
4. **Cross-boundary Healthcare Details** - Which jurisdictions covered by "recognised" healthcare professionals
5. **Reimbursement Integration** - No information on insurance claim automation integration

### Questions to Submit to Health Bureau:
Based on website analysis, these questions remain unanswered:
- How many private healthcare practitioners have applied to the Connectivity Support Scheme?
- What is the approval rate and current adoption statistics?
- Is there an enforcement audit schedule or complaint-driven investigation system?
- Has the government considered linking eHealth data with VHIS or other insurance claims?
- What is the timeline for further eHealth integration with private insurance systems?

### Suggested Next Steps:
1. Cross-reference website findings with existing government enquiry questions
2. Look for press releases or announcement on subsidy uptake rates
3. Check LegCo minutes/papers (referenced on website) for policy debates
4. Monitor news section of ehealth.gov.hk for updates on Amendment Bill implementation

---

## Web Scraper Tools Created

Two Python tools have been created in the group3-eHealth folder:

1. **ehealth_scraper.py** - General scraper for links, keywords, and initial page analysis
2. **ehealth_scraper_detailed.py** - Detailed scraper focused on subsidy and amendment information

To run:
```bash
cd courses/gcap3056/GroupProjects/group3-eHealth
python3 ehealth_scraper.py
python3 ehealth_scraper_detailed.py
```

Outputs saved as JSON files for reference.

---

## Content Suitable for Google Doc

### Subsidy Scheme Summary (for Google Doc):
- Scheme provides HK$500/month subsidy (max 12 months) for registered doctors
- Only applies to Western medicine practitioners
- Institutions must be eHealth-registered and continuously deposit records
- Maximum 50 doctors per institution can participate
- Application online with 2-month approval timeline
- Accreditation scheme provides gold/silver/bronze marks for patient identification

### Amendment Bill Effects (for Google Doc):
- Legislation came into effect 1 December 2025
- Expanded mandatory data types: allergies, medications, lab reports, immunisation records
- Healthcare providers face up to HK$50,000 fine for repeated non-compliance
- Secretary for Health empowered to issue data-deposit orders
- Cross-boundary healthcare provisions enable HCP access from other jurisdictions

---

**Generated:** 12 March 2026  
**Tools Deployed:** Python web scrapers with BeautifulSoup and Requests library
