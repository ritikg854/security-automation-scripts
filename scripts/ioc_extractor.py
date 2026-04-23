"""
Simple IOC extractor for analyst-support workflows.

This script reads a text file and extracts possible IP addresses, email
addresses, URLs, and domains that may be useful during basic security
triage and investigation tasks.
"""

import re
import sys
from pathlib import Path


def extract_iocs(text):
    """Extract IPs, email addresses, URLs, and domains from input text."""
    ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    url_pattern = r"https?://[^\s]+"
    domain_pattern = r"\b(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}\b"

    ips = sorted(set(re.findall(ip_pattern, text)))
    emails = sorted(set(re.findall(email_pattern, text)))
    urls = sorted(set(re.findall(url_pattern, text)))
    domains = sorted(
        set(domain for domain in re.findall(domain_pattern, text) if domain not in emails)
    )

    return ips, emails, urls, domains


def print_section(title, items):
    """Print a section only when matching items are present."""
    if not items:
        return

    print(f"\n{title}:")
    for item in items:
        print(f"- {item}")


def main():
    """Load input text from a file, extract IOCs, and print the results."""
    if len(sys.argv) != 2:
        print("Usage: python scripts/ioc_extractor.py <input_file>")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"Error: file not found - {input_path}")
        sys.exit(1)

    text = input_path.read_text(encoding="utf-8")
    ips, emails, urls, domains = extract_iocs(text)

    print("Extracted IOCs")
    print("-" * 20)

    print_section("IP Addresses", ips)
    print_section("Email Addresses", emails)
    print_section("URLs", urls)
    print_section("Domains", domains)


if __name__ == "__main__":
    main()
