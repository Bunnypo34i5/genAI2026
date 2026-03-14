#!/usr/bin/env python3
"""
Enhanced eHealth Scraper - Focus on Subsidy Schemes and Amendment Bill Info
Extracts detailed information relevant to Group 3's project
"""

import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime

class eHealthDetailedScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept-Language': 'zh-HK,zh;q=0.9,en;q=0.8'
        })
        self.findings = {
            'timestamp': datetime.now().isoformat(),
            'subsidy_scheme': {},
            'connectivity_support': {},
            'amendment_bill': {},
            'key_pages': []
        }
    
    def fetch_page(self, url):
        try:
            print(f"  Fetching: {url}")
            response = self.session.get(url, timeout=10)
            response.encoding = 'utf-8'
            if response.status_code == 200:
                return BeautifulSoup(response.content, 'html.parser')
            else:
                print(f"    ⚠ HTTP {response.status_code}")
                return None
        except Exception as e:
            print(f"    ❌ Error: {e}")
            return None
    
    def extract_text_sections(self, soup):
        """Extract all meaningful text sections"""
        sections = []
        for element in soup.find_all(['h1', 'h2', 'h3', 'p', 'li', 'td', 'th']):
            text = element.get_text(strip=True)
            if text and len(text) > 10:
                sections.append(text)
        return sections
    
    def scrape_connectivity_support_scheme(self):
        """Scrape details on eHealth+ Connectivity Support Scheme"""
        print("\n💰 Scraping eHealth+ Connectivity Support Scheme...")
        
        url = "https://www.ehealth.gov.hk/tc/healthcare-provider-and-professional/resources/ehealth-plus-connectivity-support-scheme/index.html"
        soup = self.fetch_page(url)
        
        if soup:
            text_content = soup.get_text()
            self.findings['connectivity_support'] = {
                'url': url,
                'content_length': len(text_content),
                'content_preview': text_content[:500],
                'full_content': text_content
            }
            
            # Look for key information
            keywords = {
                'subsidy_amount': ['HK$', '元', '補貼', '每月', 'monthly', '月'],
                'duration': ['月', 'months', '年', 'year', '期間'],
                'eligibility': ['資格', '條件', 'eligible', '合資格'],
                'application': ['申請', 'application', '期限', 'deadline']
            }
            
            for category, terms in keywords.items():
                for term in terms:
                    if term in text_content:
                        print(f"    ✓ Found keyword: {term}")
            
            return True
        return False
    
    def scrape_amendment_bill_info(self):
        """Scrape information related to Amendment Bill 2025"""
        print("\n📋 Scraping Amendment Bill Information...")
        
        # Try multiple potential URLs
        urls = [
            "https://www.ehealth.gov.hk/tc/index.html",
            "https://www.ehealth.gov.hk/tc/healthcare-provider-and-professional/index.html",
            "https://www.ehealth.gov.hk/tc/faq/index.html"
        ]
        
        all_content = ""
        for url in urls:
            soup = self.fetch_page(url)
            if soup:
                content = soup.get_text()
                all_content += content + "\n\n"
        
        # Search for amendment-related keywords
        keywords_to_find = [
            '修訂', '條例', '法案', '2025', '強制', '數據存放',
            '醫護專業人員', '指明健康數據', '過敏', '藥物', '化驗報告'
        ]
        
        found_keywords = {}
        for keyword in keywords_to_find:
            if keyword in all_content:
                found_keywords[keyword] = True
                print(f"    ✓ Found: {keyword}")
        
        self.findings['amendment_bill'] = {
            'keywords_found': found_keywords,
            'summary': 'Information on Amendment Bill needs to be gathered from government sources'
        }
        
        return True
    
    def scrape_faq_section(self):
        """Scrape FAQ page for detailed information"""
        print("\n❓ Scraping FAQ Section...")
        
        url = "https://www.ehealth.gov.hk/tc/faq/index.html"
        soup = self.fetch_page(url)
        
        if soup:
            # Extract FAQ items
            faqs = []
            faq_items = soup.find_all(['dt', 'dd', 'div'])  # Common FAQ structures
            
            current_question = ""
            for item in faq_items:
                text = item.get_text(strip=True)
                if len(text) > 20:
                    faqs.append(text[:200])
            
            self.findings['key_pages'].append({
                'page': 'FAQ',
                'url': url,
                'items_found': len(faqs),
                'sample': faqs[:5]
            })
            
            print(f"    ✓ Found {len(faqs)} FAQ items")
            return True
        return False
    
    def extract_key_statistics(self):
        """Extract key statistics and numbers from content"""
        print("\n📊 Extracting Key Statistics...")
        
        stats = {}
        
        # Common patterns for statistics
        patterns = {
            'hk_dollar': r'HK\$[\d,]+',
            'percentages': r'\d+%',
            'years': r'202\d',
            'dates': r'\d{1,2}\s+(January|February|March|April|May|June|July|August|September|October|November|December)',
            'registration': r'[0-9,]+\s*(registered|登記)',
        }
        
        all_text = ""
        urls_to_check = [
            "https://www.ehealth.gov.hk/tc/index.html",
            "https://www.ehealth.gov.hk/tc/faq/index.html"
        ]
        
        for url in urls_to_check:
            soup = self.fetch_page(url)
            if soup:
                all_text += soup.get_text() + "\n"
        
        for pattern_name, pattern in patterns.items():
            matches = re.findall(pattern, all_text)
            if matches:
                stats[pattern_name] = list(set(matches))[:5]  # Top 5 unique matches
                print(f"    ✓ {pattern_name}: {len(set(matches))} unique values found")
        
        self.findings['key_statistics'] = stats
        return True
    
    def generate_report(self):
        """Generate detailed report"""
        print("\n" + "="*70)
        print("📊 EHEALTH DETAILED SCRAPER REPORT")
        print("="*70)
        
        print(f"\n⏰ Timestamp: {self.findings['timestamp']}")
        
        print("\n💰 CONNECTIVITY SUPPORT SCHEME:")
        if self.findings['connectivity_support']:
            print(f"  ✓ URL: {self.findings['connectivity_support'].get('url', 'N/A')}")
            print(f"  ✓ Content Size: {self.findings['connectivity_support'].get('content_length', 0)} characters")
            preview = self.findings['connectivity_support'].get('content_preview', '')
            if preview:
                print(f"  Preview: {preview[:200]}...")
        
        print("\n📋 AMENDMENT BILL INFO:")
        if self.findings['amendment_bill'].get('keywords_found'):
            keywords = self.findings['amendment_bill']['keywords_found']
            for keyword in keywords:
                if keywords[keyword]:
                    print(f"  ✓ Found: {keyword}")
        
        print("\n📊 KEY STATISTICS FOUND:")
        stats = self.findings.get('key_statistics', {})
        for stat_type, values in stats.items():
            print(f"  {stat_type}:")
            for value in values[:3]:
                print(f"    • {value}")
        
        print("\n" + "="*70)
    
    def save_findings(self):
        """Save all findings to file"""
        output_file = 'ehealth_detailed_findings.json'
        
        # Clean up for JSON serialization
        cleaned_findings = {}
        for key, value in self.findings.items():
            if isinstance(value, dict):
                # Limit size of content fields
                if 'full_content' in value and len(str(value['full_content'])) > 10000:
                    value['full_content'] = value['full_content'][:5000]
            cleaned_findings[key] = value
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(cleaned_findings, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Findings saved to: {output_file}")
    
    def run(self):
        print("🚀 Enhanced eHealth Scraper - Detailed Analysis\n")
        
        # Run all scraping tasks
        self.scrape_connectivity_support_scheme()
        self.scrape_amendment_bill_info()
        self.scrape_faq_section()
        self.extract_key_statistics()
        
        # Generate and save results
        self.generate_report()
        self.save_findings()

if __name__ == "__main__":
    scraper = eHealthDetailedScraper()
    scraper.run()
