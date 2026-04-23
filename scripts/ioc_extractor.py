import re
import sys
from pathlib import Path


def extract_iocs(text):
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


def main():
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

    print("\nIP Addresses:")
    for ip in ips:
        print(f"- {ip}")

    print("\nEmail Addresses:")
    for email in emails:
        print(f"- {email}")

    print("\nURLs:")
    for url in urls:
        print(f"- {url}")

    print("\nDomains:")
    for domain in domains:
        print(f"- {domain}")


if __name__ == "__main__":
    main()
