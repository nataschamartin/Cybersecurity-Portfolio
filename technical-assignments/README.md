Technical Assignments – Course Submissions \& Exercises
This folder contains various technical exercises, written assignments, and documentation completed across multiple cybersecurity and tech-related courses. These artifacts demonstrate practical application of theoretical knowledge in areas such as system administration, GRC, Python, incident response, and compliance.

📄 Contents Overview
Written assignments and risk registers

Lab documentation and ticket responses

Python practice and troubleshooting logs

Supplemental worksheets or reflection prompts

🎯 Purpose
The files here reflect:

Hands-on application of course concepts

Scenario-based problem solving

Drafts of professional documentation commonly used in cybersecurity roles (e.g., risk registers, policy outlines, lab reports)

🧩 Skills Represented
Analytical thinking and troubleshooting

Technical writing and documentation

Command-line familiarity (depending on assignment)

Python basics and error handling

Security policy evaluation and risk assessment





Lab 1: Google Dorking

This lab introduced foundational reconnaissance techniques using Google Dorking, a method of leveraging advanced Google search operators to uncover publicly accessible data that may pose security risks. The activity demonstrated how attackers can identify misconfigured files, exposed login portals, sensitive documents, and vulnerable devices indexed by search engines.



Key Skills Practiced:



Use of advanced search operators (intitle:, inurl:, filetype:, site:)



Understanding how OSINT (Open Source Intelligence) supports penetration testing



Ethical implications of data exposure and responsible disclosure



This exercise marks the beginning of the hands-on penetration testing portion of my cybersecurity training. All tests were conducted in an educational environment using public-facing content.



Lab 2: In this lab, I performed a basic penetration test using publicly available tools and safe targets, including Scanme and Google's Gruyere web app. The objective was to simulate real-world reconnaissance and vulnerability discovery while following ethical hacking principles. I used methods such as Google Dorking, port scanning, and web application analysis to identify exposed services, security misconfigurations, and common web vulnerabilities. This lab demonstrates foundational skills in ethical penetration testing and supports my understanding of the reconnaissance and discovery phases in the cybersecurity kill chain.



Penetration Testing Lab: Google Dorking, Port \& Website Scanning

This lab focused on foundational penetration testing techniques using publicly available tools. The tasks included:



Port Scanning: Using Pentest-Tools' Port Scanner to examine scanme.nmap.org for open, closed, or filtered ports. Results provided insight into service names, versions, and port states, useful for mapping exposed services.



Website Scanning: Targeted google-gruyere.appspot.com to identify web vulnerabilities like missing security headers, weak configurations, or exposed .txt files. Results helped simulate what real-world testing could reveal in insecure web environments.



⚠️ All scans were conducted on explicitly authorized training targets. No unauthorized systems were tested.



Lab 3: Port Scanning with NMap with Kali Linux



This lab demonstrates the use of Nmap, a powerful network scanning tool, within a Kali Linux Docker container. The purpose was to practice scanning public targets, understand different types of Nmap scans (including SYN scans), and observe how user privilege levels affect scan capabilities.



🧪 Lab Environment

Platform: Kali Linux (via Docker)



Tools Installed: nmap, nano, ccrypt



Target Host: scanme.nmap.org



User Accounts:



root (administrator)



John (non-root user created during the lab)



🔧 Key Commands Used

bash

Copy

Edit

sudo apt-get update

sudo apt-get install nmap

nmap scanme.nmap.org

nmap -p22,113,139 scanme.nmap.org

nmap -sS -p22,113,139 scanme.nmap.org

nmap --packet-trace -p22,113,139 scanme.nmap.org

nmap -d5 --packet-trace -p22,113,139 scanme.nmap.org

useradd John

su John

exit

🔐 Privilege Demonstration – Expected Output

As part of the lab, a non-root user (John) attempted to perform a SYN scan using:



bash

Copy

Edit

nmap -sS -p22,113,139 scanme.nmap.org

This returned the expected error:



vbnet

Copy

Edit

Couldn't open a raw socket. Error: Operation not permitted (1)

✅ This behavior is intentional — SYN scans require raw socket access, which only the root user possesses. This reinforced the importance of user privileges when performing low-level packet-based scans.



📦 Additional Scan Practice

As instructed, I also ran scans against google.com:



bash

Copy

Edit

nmap google.com

nmap -sS -p80,443 google.com

nmap --packet-trace -p80,443 google.com

This provided insight into real-world target responses and how firewalls and public services often restrict or filter port scanning.



📝 Key Takeaways

SYN scans (-sS) are fast and stealthy but require root privileges.



Non-root users are limited in the types of scans they can perform due to raw socket restrictions.



Packet tracing and debug levels in Nmap (--packet-trace, -d5) offer deep visibility into how Nmap operates behind the scenes.



Using Docker for Kali Linux is an effective and isolated way to test scanning tools safely.



Lab 3 - Zenmap Network Scanning Lab – GUI-based Nmap Exploration

This lab focused on using Zenmap, the graphical user interface (GUI) for Nmap, to conduct various types of scans against both local and public targets. It served as an introduction to performing network reconnaissance using a point-and-click environment, while still understanding the command-line options being executed under the hood.



🖥️ Scans Performed

Quick Scan of localhost (127.0.0.1)



Quick Scan of scanme.nmap.org



Quick Scan of cloud.ibm.com



Each scan displayed port status (open, closed, filtered), IP address info, and basic host details.



⚠️ Temporary XML Output Error (Known Behavior)

After each scan completed, Zenmap displayed the following non-blocking error:



bash

Copy

Edit

Error building command

\[Errno 2] No such file or directory: ...\\zenmap-xxxx.xml

This occurred because Zenmap attempted to write temporary .xml output files to a system temp directory that did not exist or was inaccessible in the current environment. Despite the error, all scans completed successfully and results were shown in the Zenmap interface.



📘 Key Takeaways

Zenmap mirrors Nmap CLI options and helps visualize results in an easier format.



GUI tools can introduce unexpected behavior related to file paths and permissions, especially in Windows-based or sandboxed lab environments.



The scan results confirmed expected behavior from earlier Nmap CLI exercises (e.g., visible ports, latency, and NSE script output).



Lab 4



Wireshark Packet Capture Lab

This lab introduced the use of Wireshark, a widely used network protocol analyzer, to capture and inspect live packet traffic on a system. The focus was on installing the tool, performing a capture session, and reviewing packet-level details for analysis.



🎯 Lab Objectives

✅ Install Wireshark

Successfully installed the application on the local system. (Basic installation steps not documented, as they were standard and did not require extensive walkthrough.)



✅ Capture packets using Wireshark

Launched a live capture session and monitored traffic in real time using default interface settings.



✅ Review capture results

Inspected individual packets, reviewed protocol types, examined source and destination IP addresses, and verified port usage and flags.



🔍 Key Takeaways

Wireshark provides deep visibility into packet-level traffic, making it useful for network troubleshooting, security analysis, and protocol inspection.



Real-time filtering (e.g., by IP, port, or protocol) enables targeted analysis of relevant traffic.



Even simple browsing or ping activity can reveal valuable patterns in HTTP, DNS, ICMP, and TCP behavior.



Lab: Getting Started with GitHub (Optional)

This lab was completed as a prerequisite for the upcoming “Scanning for Code Vulnerabilities with Snyk” lab. I skipped Task 1 since I already had an active GitHub account. I began with Task 2 by creating a private test repository with a README file.



In Task 3, I created a basic Python file (helloworld.py), committed it to the repository, and practiced editing it directly from the GitHub interface. In Task 4, I forked a public repository from Bitnami to explore how GitHub manages code duplication and collaboration workflows.



Note: No screenshots were included for this lab because all actions were completed directly within my GitHub account and are already reflected in my repositories.

