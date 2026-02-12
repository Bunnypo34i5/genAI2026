"""
Crawler for Hong Kong Fire Services Department (FSD) Government Telephone Directory
URL: https://tel.directory.gov.hk/index_FSD_ENG.html

Purpose: Identify specific FSD teams relevant to:
1. Fire safety education and community engagement
2. Fire alarm / fire service installations inspection
3. Fire investigation
4. Building improvement / fire safety compliance
5. Licensing and certification of fire services contractors

Output: Structured list of FSD teams, their contact details, and relevance assessment
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import re

BASE_URL = "https://tel.directory.gov.hk"

def fetch_page(url):
    """Fetch a page and return BeautifulSoup object."""
    try:
        resp = requests.get(url, timeout=15)
        resp.encoding = 'utf-8'
        return BeautifulSoup(resp.text, 'html.parser')
    except Exception as e:
        print(f"  Error fetching {url}: {e}")
        return None

def parse_main_directory():
    """Parse the main FSD directory page to get all office/division links."""
    url = f"{BASE_URL}/index_FSD_ENG.html"
    print(f"Fetching main FSD directory: {url}")
    soup = fetch_page(url)
    if not soup:
        return []

    offices = []
    # Find the select dropdown with office links
    select = soup.find('select')
    if select:
        for option in select.find_all('option'):
            value = option.get('value', '')
            name = option.text.strip()
            if value and name and 'select' not in name.lower():
                office_url = f"{BASE_URL}/{value}" if not value.startswith('http') else value
                offices.append({
                    'name': name,
                    'url': office_url
                })
    
    # Also parse from links in the page
    for link in soup.find_all('a'):
        href = link.get('href', '')
        text = link.text.strip()
        if '_ENG.html' in href and 'FSD' not in href and text:
            full_url = f"{BASE_URL}/{href}" if not href.startswith('http') else href
            # Avoid duplicates
            if not any(o['url'] == full_url for o in offices):
                offices.append({
                    'name': text,
                    'url': full_url
                })

    return offices

def parse_office_page(office_url, office_name):
    """Parse an individual office page to get staff details."""
    print(f"  Fetching: {office_name}")
    soup = fetch_page(office_url)
    if not soup:
        return []

    staff = []
    # Look for staff entries - they typically have name, post title, phone, email
    rows = soup.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 2:
            entry = {}
            for cell in cells:
                text = cell.get_text(strip=True)
                # Try to identify field type
                links = cell.find_all('a')
                for link in links:
                    href = link.get('href', '')
                    link_text = link.get_text(strip=True)
                    if 'mailto:' in href:
                        entry['email'] = href.replace('mailto:', '')
                    elif 'tel:' in href:
                        if 'phone' not in entry:
                            entry['phone'] = link_text
                        else:
                            entry['phone'] += f", {link_text}"
                    elif 'details.jsp' in href:
                        entry['name'] = link_text

            if entry:
                staff.append(entry)

    # Also look for links to sub-offices
    links_found = []
    for link in soup.find_all('a'):
        href = link.get('href', '')
        text = link.text.strip()
        if '_ENG.html' in href and text and 'Back' not in text:
            full_url = f"{BASE_URL}/{href}" if not href.startswith('http') else href
            links_found.append({'name': text, 'url': full_url})

    return staff, links_found

def assess_relevance(office_name):
    """Assess the relevance of an FSD office to our project topics."""
    name_lower = office_name.lower()

    # High relevance keywords
    high_keywords = [
        'fire safety', 'education', 'community', 'public safety',
        'building improvement', 'fire protection', 'licensing',
        'certification', 'inspection', 'investigation',
        'communication', 'information', 'complaints',
        'prosecution', 'policy', 'dangerous goods'
    ]

    # Medium relevance keywords
    medium_keywords = [
        'new territories', 'training', 'academy', 'operational support',
        'planning', 'development', 'corporate', 'ventilat'
    ]

    # Low relevance keywords
    low_keywords = [
        'ambulance', 'marine', 'diving', 'airport', 'transport',
        'workshop', 'driving', 'breathing apparatus', 'registry',
        'personnel', 'finance', 'procurement', 'logistics'
    ]

    for kw in high_keywords:
        if kw in name_lower:
            return 'HIGH'
    for kw in medium_keywords:
        if kw in name_lower:
            return 'MEDIUM'
    for kw in low_keywords:
        if kw in name_lower:
            return 'LOW'

    return 'MEDIUM'

def main():
    print("=" * 70)
    print("FSD Government Directory Crawler")
    print("=" * 70)
    print()

    # Parse main directory
    offices = parse_main_directory()
    print(f"\nFound {len(offices)} offices/divisions\n")

    results = []

    for office in offices:
        relevance = assess_relevance(office['name'])
        result = {
            'name': office['name'],
            'url': office['url'],
            'relevance': relevance,
            'staff': [],
            'sub_offices': []
        }

        # Fetch details for HIGH and MEDIUM relevance offices
        if relevance in ['HIGH', 'MEDIUM']:
            try:
                staff, sub_offices = parse_office_page(office['url'], office['name'])
                result['staff'] = staff
                result['sub_offices'] = [s['name'] for s in sub_offices]
                time.sleep(0.3)  # Be polite
            except Exception as e:
                print(f"    Error: {e}")

        results.append(result)

    # Generate report
    print("\n" + "=" * 70)
    print("RESULTS")
    print("=" * 70)

    # Sort by relevance
    order = {'HIGH': 0, 'MEDIUM': 1, 'LOW': 2}
    results.sort(key=lambda x: order.get(x['relevance'], 3))

    # Print summary
    high_rel = [r for r in results if r['relevance'] == 'HIGH']
    med_rel = [r for r in results if r['relevance'] == 'MEDIUM']
    low_rel = [r for r in results if r['relevance'] == 'LOW']

    print(f"\nHIGH relevance: {len(high_rel)} offices")
    print(f"MEDIUM relevance: {len(med_rel)} offices")
    print(f"LOW relevance: {len(low_rel)} offices")

    # Generate markdown report
    report = []
    report.append("# FSD Directory — Teams to Contact\n")
    report.append(f"**Generated:** {time.strftime('%Y-%m-%d %H:%M')}\n")
    report.append(f"**Source:** https://tel.directory.gov.hk/index_FSD_ENG.html\n")
    report.append("---\n")

    report.append("## HIGH Relevance Teams\n")
    report.append("These teams are most relevant to our project on fire safety education, alert systems, and the Tai Po fire investigation.\n")

    for r in high_rel:
        report.append(f"### {r['name']}")
        report.append(f"- **Relevance:** {r['relevance']}")
        report.append(f"- **URL:** {r['url']}")
        if r['staff']:
            report.append("- **Contacts:**")
            for s in r['staff']:
                parts = []
                if 'name' in s:
                    parts.append(s['name'])
                if 'phone' in s:
                    parts.append(f"Tel: {s['phone']}")
                if 'email' in s:
                    parts.append(f"Email: {s['email']}")
                if parts:
                    report.append(f"  - {' | '.join(parts)}")
        if r['sub_offices']:
            report.append("- **Sub-offices:** " + ", ".join(r['sub_offices']))
        report.append("")

    report.append("\n## MEDIUM Relevance Teams\n")
    for r in med_rel:
        report.append(f"### {r['name']}")
        report.append(f"- **Relevance:** {r['relevance']}")
        report.append(f"- **URL:** {r['url']}")
        if r['staff']:
            report.append("- **Contacts:**")
            for s in r['staff'][:3]:  # Limit to top 3
                parts = []
                if 'name' in s:
                    parts.append(s['name'])
                if 'phone' in s:
                    parts.append(f"Tel: {s['phone']}")
                if 'email' in s:
                    parts.append(f"Email: {s['email']}")
                if parts:
                    report.append(f"  - {' | '.join(parts)}")
        report.append("")

    report.append("\n## LOW Relevance Teams\n")
    report.append("These teams are less directly relevant but listed for completeness.\n")
    for r in low_rel:
        report.append(f"- {r['name']}")

    # Write report
    report_text = "\n".join(report)
    with open("fsd_directory_results.md", "w") as f:
        f.write(report_text)
    print(f"\nReport written to fsd_directory_results.md")

    # Also save raw JSON
    with open("fsd_directory_raw.json", "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Raw data written to fsd_directory_raw.json")

    print("\n" + "=" * 70)
    print("KEY TEAMS TO CONTACT:")
    print("=" * 70)
    for r in high_rel:
        print(f"\n  [{r['relevance']}] {r['name']}")
        for s in r['staff'][:2]:
            info = []
            if 'name' in s:
                info.append(s['name'])
            if 'phone' in s:
                info.append(f"Tel: {s['phone']}")
            if 'email' in s:
                info.append(f"Email: {s['email']}")
            if info:
                print(f"         {' | '.join(info)}")

if __name__ == "__main__":
    main()
