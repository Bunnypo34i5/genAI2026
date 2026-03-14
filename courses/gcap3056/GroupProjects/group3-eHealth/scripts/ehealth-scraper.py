#!/usr/bin/env python3
"""
eHealth Website Scraper Tool
Purpose: Extract information on subsidy schemes and Amendment Bill 2025 effects
Target: https://www.ehealth.gov.hk/tc/index.html (Traditional Chinese)
"""

import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin, urlparse
import time
from datetime import datetime

class eHealthScraper:
    def __init__(self, base_url, timeout=10):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.findings = {
            'metadata': {
                'scraped_date': datetime.now().isoformat(),
                'base_url': base_url,
                'status': 'pending'
            },
            'subsidy_schemes': [],
            'amendment_bill_info': [],
            'connectivity_scheme': [],
            'key_statistics': [],
            'links_found': [],
            'raw_sections': []
        }
    
    def fetch_page(self, url):
        """Fetch a webpage and return BeautifulSoup object"""
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.encoding = 'utf-8'
            if response.status_code == 200:
                return BeautifulSoup(response.content, 'html.parser')
            else:
                print(f"⚠ HTTP {response.status_code} for {url}")
                return None
        except Exception as e:
            print(f"❌ Error fetching {url}: {e}")
            return None
    
    def extract_links(self, soup, base_url):
        """Extract all links from page"""
        links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag.get('href')
            full_url = urljoin(base_url, href)
            text = a_tag.get_text(strip=True)
            links.append({
                'text': text,
                'url': full_url,
                'is_internal': urlparse(full_url).netloc == urlparse(base_url).netloc
            })
        return links
    
    def search_keywords_in_text(self, soup, keywords):
        """Search for relevant keywords in page text"""
        findings = []
        text = soup.get_text().lower()
        
        for keyword in keywords:
            if keyword.lower() in text:
                # Find sentences containing keyword
                paragraphs = soup.find_all(['p', 'span', 'div', 'li'])
                for para in paragraphs:
                    para_text = para.get_text().lower()
                    if keyword.lower() in para_text:
                        findings.append({
                            'keyword': keyword,
                            'snippet': para.get_text(strip=True)[:200]
                        })
                        break
        return findings
    
    def scan_main_page(self):
        """Scan the main eHealth homepage"""
        print("🔍 Scanning main eHealth page...")
        soup = self.fetch_page(self.base_url)
        
        if not soup:
            return False
        
        # Extract all links
        links = self.extract_links(soup, self.base_url)
        self.findings['links_found'] = links
        print(f"  ✓ Found {len(links)} links")
        
        # Search for key information
        keywords = [
            'subsidy',
            'subsidy scheme',
            'eHealth+',
            'connectivity support',
            'amendment',
            '修訂',
            '補貼',
            '電子健康紀錄',
            '法案',
            'Bill 2025',
            '2025',
            'accreditation',
            '認可',
            'specified health data',
            'data deposit',
            'private healthcare',
            'healthcare provider'
        ]
        
        findings = self.search_keywords_in_text(soup, keywords)
        self.findings['key_statistics'].extend(findings)
        print(f"  ✓ Found {len(findings)} keyword matches")
        
        return True
    
    def explore_key_pages(self):
        """Explore key pages related to subsidy and infrastructure"""
        print("\n🔗 Exploring key navigation links...")
        
        # Common URL patterns for eHealth sites
        key_patterns = [
            '/tc/subsidy',
            '/tc/connectivity',
            '/tc/amendment',
            '/tc/healthcare-provider-and-professional',
            '/tc/patients',
            '/tc/faq',
            '/tc/news',
            '/whats-ehealth',
            '/ehealth-plus-development'
        ]
        
        for pattern in key_patterns:
            url_to_try = urljoin(self.base_url, pattern)
            print(f"  Trying: {url_to_try}")
            soup = self.fetch_page(url_to_try)
            
            if soup:
                text = soup.get_text()
                if len(text) > 100:  # Valid page
                    print(f"    ✓ Page found - {len(text)} characters")
                    
                    # Store section content
                    self.findings['raw_sections'].append({
                        'url': url_to_try,
                        'title': soup.title.string if soup.title else 'No title',
                        'content_length': len(text),
                        'preview': text[:300]
                    })
                    
                    # Search for subsidy and bill info
                    subsidy_keywords = ['subsidy', 'support scheme', 'HK$', 'fee', 'support']
                    bill_keywords = ['amendment', 'bill', '2025', 'ordinance', 'specified health data', 'mandatory']
                    
                    subsidy_matches = self.search_keywords_in_text(soup, subsidy_keywords)
                    bill_matches = self.search_keywords_in_text(soup, bill_keywords)
                    
                    if subsidy_matches:
                        self.findings['subsidy_schemes'].extend(subsidy_matches)
                    if bill_matches:
                        self.findings['amendment_bill_info'].extend(bill_matches)
                else:
                    print(f"    ✗ Page not found or empty")
            
            time.sleep(1)  # Be respectful to the server
    
    def generate_report(self):
        """Generate a summary report"""
        self.findings['metadata']['status'] = 'completed'
        
        print("\n" + "="*60)
        print("📊 EHEALTH SCRAPER REPORT")
        print("="*60)
        print(f"\n📅 Date: {self.findings['metadata']['scraped_date']}")
        print(f"🌐 Target: {self.findings['metadata']['base_url']}")
        
        print(f"\n🔗 Links Found: {len(self.findings['links_found'])}")
        for link in self.findings['links_found'][:10]:  # Show first 10
            marker = "🏠" if not link['is_internal'] else "📄"
            print(f"  {marker} {link['text'][:50]:50s} → {link['url'][:60]}")
        
        print(f"\n💰 Subsidy Scheme Findings: {len(self.findings['subsidy_schemes'])}")
        for finding in self.findings['subsidy_schemes'][:5]:
            print(f"  • {finding['keyword']}: {finding['snippet'][:80]}")
        
        print(f"\n📋 Amendment Bill Info: {len(self.findings['amendment_bill_info'])}")
        for finding in self.findings['amendment_bill_info'][:5]:
            print(f"  • {finding['keyword']}: {finding['snippet'][:80]}")
        
        print(f"\n📄 Pages Explored: {len(self.findings['raw_sections'])}")
        for section in self.findings['raw_sections']:
            print(f"  • {section['title'][:50]}")
            print(f"    URL: {section['url']}")
            print(f"    Size: {section['content_length']} chars")
        
        print("\n" + "="*60)
    
    def save_findings(self, output_file):
        """Save detailed findings to JSON file"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.findings, f, ensure_ascii=False, indent=2)
        print(f"\n✅ Detailed findings saved to: {output_file}")
    
    def run(self):
        """Execute full scraping workflow"""
        print("🚀 Starting eHealth Website Scraper\n")
        
        # Scan main page
        if self.scan_main_page():
            # Explore key pages
            self.explore_key_pages()
            
            # Generate report
            self.generate_report()
            
            # Save findings
            output_file = 'ehealth_scraper_findings.json'
            self.save_findings(output_file)
            
            print(f"\n✨ Scraping complete!")
            return True
        else:
            print("❌ Failed to reach main page")
            return False

def main():
    # Target URL: eHealth Hong Kong (Traditional Chinese)
    target_url = "https://www.ehealth.gov.hk/tc/index.html"
    
    # Initialize scraper
    scraper = eHealthScraper(target_url)
    
    # Run scraping
    scraper.run()

if __name__ == "__main__":
    main()
