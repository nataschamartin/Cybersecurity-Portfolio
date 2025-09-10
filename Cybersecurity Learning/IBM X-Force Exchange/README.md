# IBM X-Force Exchange Lab

This lab explores the IBM X-Force Exchange threat intelligence platform. The activity focused on navigating the site, searching for real-world CVEs, analyzing IP reports, and understanding the structure of vulnerability data shared with the global cybersecurity community.

## 🧠 Learning Objectives

- Explore the IBM X-Force Exchange interface and threat intelligence features
- Understand how to search and interpret reports on malware, IPs, and vulnerabilities
- Identify and analyze a recent CVE using the platform’s threat data
- Recognize the value of CVE entries in organizational security posture and mitigation

## 🔍 Activity Overview

- **IP Search Performed**: `185.225.73.244`  
  - Categorized as “Unsuspicious”
  - Linked to Open Fiber S.P.A. in Italy
  - Timeline includes regional internet registry events from 2023–2024

- **Malware Search Performed**: `"DarkGate"`  
  - Returned various CVE vulnerability results, including:
    - **CVE-2025-32119**  
      - Vulnerability in WordPress CardGate Payments for WooCommerce <= 3.2.1  
      - **CVSS Score**: 8.2 (High)  
      - Type: Blind SQL Injection  
      - **Remediation**: Update plugin to 3.2.2 or higher

## 📸 Screenshots

- `1-ip-report.png`: IP lookup result  
- `2-cve-search.png`: DarkGate malware search result  
- `3-cve-details.png`: CVE-2025-32119 full report with remediation details  

## 🧩 Key Takeaways

- CVE entries provide standardized identifiers for known vulnerabilities
- Threat reports help analysts evaluate risk severity and mitigation steps
- Public threat intel platforms like IBM X-Force Exchange support proactive security by offering access to real-time data on emerging threats

---

**Date Completed:** August 7, 2025  
**Tool Used:** IBM X-Force Exchange (https://exchange.xforce.ibmcloud.com/)
