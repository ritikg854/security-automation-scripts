import re

sample_text = """
User received a suspicious email from alert@micr0soft-support.com asking them to visit
http://secure-login-check.com/reset and confirm their credentials.
Another link included was https://portal-security.example.org/verify.
The email also mentioned contacting admin@security-team.co.uk.
Possible source IPs observed: 192.168.1.10, 45.88.120.4
"""

ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
url_pattern = r"https?://[^\s]+"
domain_pattern = r"\b(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}\b"

ips = sorted(set(re.findall(ip_pattern, sample_text)))
emails = sorted(set(re.findall(email_pattern, sample_text)))
urls = sorted(set(re.findall(url_pattern, sample_text)))
domains = sorted(
    set(domain for domain in re.findall(domain_pattern, sample_text) if domain not in emails)
)

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
