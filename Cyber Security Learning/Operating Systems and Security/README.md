Operating Systems and Security

This folder contains practical lab work completed as part of an introductory Operating Systems and Security course. It includes foundational concepts and applied exercises across system administration, user and permission management, firewall configurations, antivirus use, and file system navigation. These exercises were completed in a hands-on environment using ticket-based tasks to simulate real-world system administration scenarios.

📁 Folder Contents

Ticketed Lab Exercises

Each "ticket" represents a specific task or system troubleshooting scenario. Screenshots and documentation are provided for each.

Ticket 1: Folder creation, file structure organization, and basic directory commands

Ticket 2: User and group account creation, permissions configuration

Ticket 3: File permissions and access control settings (chmod, chown)

Ticket 4: Firewall and security settings, including port configuration and basic rules

Ticket 5: Antivirus and malware scanning commands

Ticket 6: System settings verification and summary (hostname, OS version, etc.)

General CLI Utilities

Includes commands used for system navigation, user/group management, permissions, and antivirus scanning

Practical application of Linux terminal commands within an emulated or live lab

🔐 Skills Demonstrated

Command-line interface (CLI) navigation and execution

File system structure creation and maintenance

User and group administration in Linux-based environments

Managing file and folder permissions securely

Firewall and antivirus utility configuration and use

Hands-on security and system hardening tasks

✅ Use Cases

This work supports baseline system administration knowledge essential for:

Cybersecurity compliance auditing

Digital forensics (e.g., verifying user access trails)

Incident response (understanding permission or firewall misconfigurations)

GRC-related policy testing (e.g., user least privilege enforcement)

Note: All screenshots and tasks were completed by Natascha Martin as part of hands-on training through a cybersecurity education platform. This folder supports her transition into cybersecurity roles with a foundation in secure system configuration.

📎 For detailed screenshots of commands and outputs, refer to the individual ticket folders inside this directory.
# Digital Forensics – Cowrie SSH Honeypot Lab

This lab explored log analysis and attacker simulation using **Cowrie**, an SSH and Telnet honeypot that mimics real systems to capture unauthorized access attempts and shell commands. The purpose of the exercise was to simulate a system compromise and investigate activity through log analysis — a core skill in digital forensics.

---

## 🧪 Lab Objectives

- Run Cowrie in a Docker container and redirect output to `honeypotLogs.txt`
- Connect via SSH to the honeypot and simulate an attack
- Create, read, and delete files from the terminal to simulate unauthorized actions
- Analyze Cowrie’s logs to identify:
  - Login attempts (`grep "login attempt"`)
  - Executed commands (`grep "CMD"`)
  - Session terminations (`grep "Connection lost after"`)

---

## ⚠️ Notes from My Attempt

Due to lab design, I mistakenly entered some commands in the main terminal instead of a new terminal as instructed. This caused some workflow issues. I used AI assistance to troubleshoot and recover from that mistake and was able to proceed with log analysis as intended.

---

## 🧠 Skills Practiced

- Honeypot deployment and log redirection
- SSH session simulation
- Forensic-style log extraction and filtering
- Container management with Docker

---

## 🗂️ Related File

- [`Lab environments and Final Project.pdf`](../Operating%20Systems%20and%20Security/Lab%20environments%20and%20Final%20Project.pdf) – broader OS lab overview  
- [`Cowrie Lab.docx`](./73a9c548-8d59-4a9b-9d61-d3d04366854b.docx) – raw lab notes (this file)

