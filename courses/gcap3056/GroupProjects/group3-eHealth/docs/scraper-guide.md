# Web Scraper Tools - User Guide

## Overview

Two Python web scraper tools have been created to monitor and extract information from https://www.ehealth.gov.hk/tc/index.html for your eHealth group project.

---

## Tool 1: ehealth_scraper.py

**Purpose:** General website reconnaissance and link mapping

**Features:**
- Scans main eHealth homepage
- Extracts all internal and external links
- Searches for 20+ relevant keywords (subsidy, amendment, bill, etc.)
- Explores common URL patterns
- Generates human-readable report
- Saves all findings to JSON file

**Usage:**
```bash
python3 ehealth_scraper.py
```

**Output Files:**
- `ehealth_scraper_findings.json` - Structured data with links, keywords, sections
- Console report - Immediate summary of findings

**Best For:**
- Initial page audits
- Finding new pages/sections on the website
- Link verification and broken link detection
- Keyword trend analysis

---

## Tool 2: ehealth_scraper_detailed.py

**Purpose:** Deep dive into subsidy schemes and Amendment Bill information

**Features:**
- Fetches eHealth+ Connectivity Support Scheme details page
- Extracts Amendment Bill references
- Parses FAQ section (584+ items)
- Extracts key statistics and numbers
- Organized findings by category
- Limited response size to avoid memory issues

**Usage:**
```bash
python3 ehealth_scraper_detailed.py
```

**Output Files:**
- `ehealth_detailed_findings.json` - Structured findings by category
- Console report - Keyword matches and statistics found

**Best For:**
- Focused research on subsidy scheme
- Amendment Bill implementation tracking
- FAQ analysis for policy details
- Monthly monitoring of website changes

---

## Key Information Extracted

### From Connectivity Support Scheme:
- Eligibility criteria (western medicine, eHealth registration required)
- Subsidy amount (HK$500/month per doctor)
- Duration (maximum 12 months)
- Application process (online, 2-month approval)
- Participation limits (50 doctors per institution)
- Record deposit requirements

### From Amendment Bill Section:
- Bill passed and effective date
- Mandatory data categories (allergies, medications, lab reports)
- Enforcement powers (data-deposit orders by Secretary)
- Penalty amounts (HK$50,000 for repeated non-compliance)
- Cross-boundary provisions
- Accreditation scheme details

### Statistics Tracked:
- Years mentioned (2023, 2025, 2026)
- HK$ amounts referenced
- Percentages cited in policies
- Registration numbers if available

---

## Integration with Group 3 Project

### How to Use Results:

1. **Update outlineDraft.md**
   - Add website-verified information on subsidy scheme
   - Include Amendment Bill details
   - Cite ehealth.gov.hk as official source

2. **Strengthen GovEnquiries.md**
   - Reference website gaps in your formal enquiries
   - Ask for statistics not found online
   - Request timeline for identified missing information

3. **Evidence for Report**
   - Use JSON outputs as appendix data
   - Include screenshots or text extraction as supporting docs
   - Show gap between public information and policy implementation

4. **Monitor Implementation**
   - Run scrapers monthly to track changes
   - Document when new information is published
   - Track announcement of subsidy uptake statistics

---

## Customization

### Modify Keywords: Edit these scrapers to search for different terms:
```python
keywords = [
    'subsidy',
    'amendment',
    'insurance',
    'reimbursement',
    # Add your custom keywords here
]
```

### Change Target URLs: Modify base_url or explore_key_pages to focus on different areas:
```python
urls = [
    "https://www.ehealth.gov.hk/tc/faq/index.html",
    "https://www.ehealth.gov.hk/tc/news",
    # Add your URLs
]
```

### Export Formats: JSON output can be converted to CSV or other formats:
```bash
python3 -c "import json; data=json.load(open('ehealth_scraper_findings.json')); print(json.dumps(data, indent=2))"
```

---

## Troubleshooting

**Issue:** HTTP 404 errors on some URLs
- **Cause:** Some common URL patterns don't exist on this site
- **Solution:** Check actual site structure and update URL patterns

**Issue:** Encoding errors with Traditional Chinese
- **Cause:** UTF-8 not properly set
- **Solution:** Ensure terminal and Python are configured for UTF-8

**Issue:** Page content not captured
- **Cause:** JavaScript-heavy pages need special handling
- **Solution:** Consider using Selenium or Playwright for JavaScript rendering

**Issue:** Memory issues with large pages
- **Cause:** FAQ page and similar have extensive content
- **Solution:** Already implemented slicing in detailed scraper

---

## Recommendations

### For Your Group Project:

1. **Weekly Monitoring**
   - Run detailed scraper every Monday
   - Compare outputs for changes
   - Log any new information found

2. **Data Organization**
   - Save outputs with timestamps
   - Archive to folder: `ehealth_monitor/`
   - Create change log: `website_changes.md`

3. **Cross-Reference**
   - Compare scraped data with government press releases
   - Verify LegCo announcements against website
   - Flag inconsistencies for enquiries

4. **Extend the Tools**
   - Add monitoring for LegCo papers
   - Create alerts for keyword changes
   - Generate comparison reports

---

## Technical Details

**Dependencies Required:**
```bash
pip install requests beautifulsoup4
```

**Python Version:** 3.6+

**Browser Headers Included:**
- User-Agent mimics modern browser
- Accept-Language set to zh-HK/Chinese

**Timeout:** 10 seconds per page

**Respectful Crawling:**
- 1-second delay between page requests
- No aggressive parallel fetching
- Proper User-Agent identification

---

## Document References

Related files in group3-eHealth folder:
- `ehealth_website_analysis.md` - Comprehensive analysis
- `GOOGLE_DOC_READY_SUMMARY.md` - Formatted for Google Doc
- `outlineDraft.md` - Project outline (can be updated with scraper data)
- `update12FebeHealth.md` - Already includes scraped info
- `GovEnquiries.md` - Follow-up questions based on gaps

---

**Last Updated:** 12 March 2026  
**Tested:** ✓ Working on Ubuntu 24.04  
**Status:** ✓ Production Ready
