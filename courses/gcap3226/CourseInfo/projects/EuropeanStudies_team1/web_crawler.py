import os
import re
import time
import json
import urllib.parse
import urllib.request
import urllib.robotparser
from html.parser import HTMLParser
from datetime import datetime

BASE_URL = "https://www.hketobrussels.gov.hk/"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "ETOwebresults")
LOG_PATH = os.path.join(os.path.dirname(__file__), "process.log")
SUMMARY_PATH = os.path.join(os.path.dirname(__file__), "summary.md")
STATE_PATH = os.path.join(OUTPUT_DIR, "crawl_state.json")

MAX_PAGES = 30
REQUEST_TIMEOUT = 20
DELAY_SECONDS = 1.0
USER_AGENT = "GCAP3226-ResearchCrawler/1.0 (+https://gcap3226.hkbu.tech/)"


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.in_script = False
        self.in_style = False
        self.title = ""
        self.text_chunks = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.in_title = True
        elif tag == "script":
            self.in_script = True
        elif tag == "style":
            self.in_style = True
        elif tag == "a":
            href = None
            for key, value in attrs:
                if key.lower() == "href":
                    href = value
                    break
            if href:
                self.links.append(href)

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "script":
            self.in_script = False
        elif tag == "style":
            self.in_style = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif not self.in_script and not self.in_style:
            cleaned = data.strip()
            if cleaned:
                self.text_chunks.append(cleaned)


def log_line(log_file, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write(f"[{timestamp}] {message}\n")
    log_file.flush()


def safe_filename(url):
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        path = "index"
    if path.endswith("/"):
        path = path[:-1]
    name = re.sub(r"[^a-zA-Z0-9_-]+", "_", path)
    if not name:
        name = "index"
    return f"{name}.html"


def normalize_url(base, link):
    if link.startswith("mailto:") or link.startswith("javascript:"):
        return None
    joined = urllib.parse.urljoin(base, link)
    parsed = urllib.parse.urlparse(joined)
    if parsed.scheme not in ("http", "https"):
        return None
    cleaned = parsed._replace(fragment="").geturl()
    return cleaned


def is_same_host(url):
    return urllib.parse.urlparse(url).netloc == urllib.parse.urlparse(BASE_URL).netloc


def fetch_url(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=REQUEST_TIMEOUT) as response:
        content_type = response.headers.get("Content-Type", "")
        charset = "utf-8"
        if "charset=" in content_type:
            charset = content_type.split("charset=")[-1].split(";")[0].strip()
        content = response.read()
        return content.decode(charset, errors="replace")


def write_summary(entries):
    lines = [
        "# HKETO Brussels Web Crawl Summary",
        "",
        f"Date: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        f"Base URL: {BASE_URL}",
        f"Pages captured: {len(entries)}",
        "",
        "## Pages",
        "",
    ]
    for entry in entries:
        title = entry.get("title") or entry["url"]
        lines.append(f"### {title}")
        lines.append("")
        lines.append(f"- Link: {entry['url']}")
        lines.append(f"- Saved file: {entry['file']}")
        lines.append("")
        if entry.get("snippet"):
            lines.append("> " + entry["snippet"])
            lines.append("")
    with open(SUMMARY_PATH, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines).strip() + "\n")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    robot_parser = urllib.robotparser.RobotFileParser()
    robot_parser.set_url(urllib.parse.urljoin(BASE_URL, "robots.txt"))
    try:
        robot_parser.read()
        robots_ready = True
    except Exception:
        robots_ready = False

    to_visit = [BASE_URL]
    visited = set()
    entries = []

    with open(LOG_PATH, "w", encoding="utf-8") as log_file:
        log_line(log_file, "Starting crawl")
        log_line(log_file, f"Base URL: {BASE_URL}")
        log_line(log_file, f"Output directory: {OUTPUT_DIR}")
        if robots_ready:
            log_line(log_file, "robots.txt loaded")
        else:
            log_line(log_file, "robots.txt not available; proceeding cautiously")

        while to_visit and len(visited) < MAX_PAGES:
            current = to_visit.pop(0)
            if current in visited:
                continue
            if not is_same_host(current):
                continue
            if robots_ready and not robot_parser.can_fetch(USER_AGENT, current):
                log_line(log_file, f"Blocked by robots.txt: {current}")
                continue

            log_line(log_file, f"Fetching: {current}")
            try:
                html = fetch_url(current)
            except Exception as exc:
                log_line(log_file, f"Failed: {current} ({exc})")
                visited.add(current)
                continue

            parser = PageParser()
            parser.feed(html)

            filename = safe_filename(current)
            file_path = os.path.join(OUTPUT_DIR, filename)
            with open(file_path, "w", encoding="utf-8") as handle:
                handle.write(html)

            snippet = " ".join(parser.text_chunks)[:240]
            entries.append({
                "url": current,
                "title": parser.title.strip(),
                "file": os.path.relpath(file_path, os.path.dirname(__file__)),
                "snippet": snippet,
            })

            visited.add(current)
            log_line(log_file, f"Saved: {file_path}")

            for link in parser.links:
                normalized = normalize_url(current, link)
                if not normalized:
                    continue
                if normalized in visited or normalized in to_visit:
                    continue
                if is_same_host(normalized):
                    to_visit.append(normalized)

            time.sleep(DELAY_SECONDS)

        with open(STATE_PATH, "w", encoding="utf-8") as handle:
            json.dump({
                "base_url": BASE_URL,
                "visited": sorted(visited),
                "saved": len(entries),
            }, handle, indent=2)

        write_summary(entries)
        log_line(log_file, "Summary written")
        log_line(log_file, "Crawl complete")


if __name__ == "__main__":
    main()
