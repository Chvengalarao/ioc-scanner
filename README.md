IOC Scanner (Indicator of Compromise Scanner)

Overview

IOC Scanner is a Python-based cybersecurity tool that scans log files and detects known malicious indicators such as suspicious IP addresses and domains.

The tool compares log entries with a list of known Indicators of Compromise (IOC) and generates an alert when a match is found.

This simulates how SOC analysts perform threat hunting and incident investigation.

---

Features

- Scans log files for malicious indicators
- Detects suspicious IP addresses
- Detects malicious domains
- Generates a simple IOC detection report

---

Project Files

ioc_scanner.py → Python script that performs IOC scanning
logs.txt → Sample log file used for testing
iocs.txt → List of known malicious indicators

---

Example Log File

logs.txt

User login from 192.168.1.5
Connection from 185.234.72.10
Downloaded file from malware-site.com

---

Example Output

=== IOC Scan Report ===

IOC DETECTED
Indicator : 185.234.72.10
Log Entry : Connection from 185.234.72.10

IOC DETECTED
Indicator : malware-site.com
Log Entry : Downloaded file from malware-site.com

---

How to Run

Run the scanner using Python:

python ioc_scanner.py

---

Use Case

This project demonstrates basic log analysis and threat hunting techniques used in a Security Operations Center (SOC). Analysts use IOC scanning to identify malicious activity in logs during security investigations.

---

Author

Cybersecurity learning project for SOC Analyst practice.
