<h1 align="center">🎉 TLD-ALL Scanner V1.0</h1>
<p> A simple scanner where you just give keyword and based on that keyword it will fetch all domain ,if you give keyword "test" then it will load TLD's like test.com...test.us etc and that too with latest IANA domains list so no need to worry about updating this tool again and again.</p>


<p align="center">
  <a href="https://shravanprojects.github.io/tld-scanner-all/tld-scanner-all.gif" target="_blank">
    <img src="https://img.shields.io/badge/🎬%20Watch%20Live%20TLD%20Scanner%20Demo-Click%20Here-critical?style=for-the-badge&logo=playstation&logoColor=white&color=red" alt="Watch TLD Scanner GIF Demo"/>
  </a>
</p>




<p align="center">
  <!-- GitHub Release Version -->
  <img src="https://img.shields.io/github/v/release/shravankumaruk/tld-all-scanner?style=for-the-badge&label=Latest%20Release&color=brightgreen&logo=github" alt="Latest Release">

  <!-- GitHub Total Downloads -->
  <img src="https://img.shields.io/github/downloads/shravankumaruk/tld-all-scanner/total?style=for-the-badge&color=blue&logo=github" alt="Total Downloads">

  <!-- GitHub Release Date -->
  <img src="https://img.shields.io/github/release-date/shravankumaruk/tld-all-scanner?style=for-the-badge&label=Released&logo=calendar&color=purple" alt="Release Date">
  </p>



<p align="center">
  <!-- 15 Code‑Related Shields -->
  
  <img src="https://img.shields.io/github/stars/shravankumaruk/tld-all-scanner?style=for-the-badge&logo=github" alt="GitHub Stars" />
  <img src="https://img.shields.io/github/forks/shravankumaruk/tld-all-scanner?style=for-the-badge&logo=github" alt="GitHub Forks" />
  <img src="https://img.shields.io/github/watchers/shravankumaruk/tld-all-scanner?style=for-the-badge&logo=github" alt="GitHub Watchers" />
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python version" />
  <img src="https://img.shields.io/badge/Version-1.0-yellow?style=for-the-badge" alt="Version 1.0.0" />
  <img src="https://img.shields.io/github/issues/shravankumaruk/tld-all-scanner?style=for-the-badge&logo=github" alt="Open Issues" />
  <img src="https://img.shields.io/github/issues-closed/shravankumaruk/tld-all-scanner?style=for-the-badge&logo=github" alt="Closed Issues" />
  <img src="https://img.shields.io/github/issues-pr/shravankumaruk/tld-all-scanner?style=for-the-badge&logo=github" alt="Open Pull Requests" />
  <img src="https://img.shields.io/github/issues-pr-closed/shravankumaruk/tld-all-scanner?style=for-the-badge&logo=github" alt="Closed Pull Requests" />
  <img src="https://img.shields.io/github/contributors/shravankumaruk/tld-all-scanner?style=for-the-badge&logo=github" alt="Contributors" />
  <img src="https://img.shields.io/github/commit-activity/m/shravankumaruk/tld-all-scanner?style=for-the-badge&logo=github" alt="Monthly Commit Activity" />
  <img src="https://img.shields.io/github/last-commit/shravankumaruk/tld-all-scanner?style=for-the-badge&logo=github" alt="Last Commit" />
  <img src="https://img.shields.io/github/repo-size/shravankumaruk/tld-all-scanner?style=for-the-badge&logo=github" alt="Repository Size" />
  <img src="https://img.shields.io/github/languages/top/shravankumaruk/tld-all-scanner?style=for-the-badge&logo=github" alt="Top Language" />
  <img src="https://img.shields.io/github/v/release/shravankumaruk/tld-all-scanner?style=for-the-badge&logo=github" alt="Latest Release" />
  <img src="https://img.shields.io/github/license/shravankumaruk/tld-all-scanner?style=for-the-badge&logo=gnu" alt="License" />
    <img src="https://img.shields.io/badge/Issues-Welcome-lightgrey?style=for-the-badge&logo=github" alt="Issues Welcome" />
  <img src="https://img.shields.io/badge/Platform-Ubuntu-blue?style=for-the-badge&logo=ubuntu" alt="Ubuntu Compatible" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/bash_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white" alt="Bash Script"/>
  <img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" alt="Ubuntu"/>
  <img src="https://img.shields.io/badge/Kali-268BEE?style=for-the-badge&logo=kalilinux&logoColor=white" alt="Kali Linux"/>
  <img src="https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green" alt="PyCharm"/>
</p>





> **Scan every IANA TLD in one pass, right from your terminal!**

---

## 🔥 Features

* **🌐 Full TLD Coverage**: Fetches the live IANA list (1,500+ TLDs).
* **⚡ High-Speed**: Multi-threaded scanning with configurable workers.
* **💾 Auto-Save**: Results saved on completion and Ctrl+C interruption.
* **🎨 Colorful UI**: Figlet + Boxes + Lolcat ASCII art; Colorama prompts.
* **🔍 Flexible Output**: Filter AVAILABLE, TAKEN, or BOTH.
* **🔧 Easy Install**: One-shot `install.sh` for all dependencies.

---

## 🛠️ Installation Guide

1. **Clone**:

   ```bash
   git clone https://github.com/shravankumaruk/tld-all-scanner.git
   cd tld-all-scanner
   ```
2. **Make Scripts Executable**:

   ```bash
   chmod +x install.sh domains.py
   ```
3. **Run Installer**:

   ```bash
   sudo bash install.sh
   ```

   * Installs Python3, venv, Boxes, Figlet, Lolcat.
   * Creates `venv/` and installs Python packages.
4. **Activate & Launch**:

   ```bash
   source venv/bin/activate
   ./domains.py
   ```

---

## ⏳ Screenshots

<p align="center">
  <img src="https://github.com/user-attachments/assets/7e822de4-dec4-4f50-8431-4ce059d2446f" alt="TLD Scanner Output" width="700" />
</p>

<p align="center">
  <strong>Figure 1:</strong> Output of TLD Scanner banner with date when fetched (always fetches latest)
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/d4344c56-e2b6-4a9a-9b32-f5644c29706f" alt="Options Menu" width="700" />
</p>

<p align="center">
  <strong>Figure 2:</strong> Showing multiple options and output of 3rd option when you want both AVAILABLE and TAKEN domains list.
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/ec0e4327-5487-4760-9565-a2c064e7ac56" alt="JSON Output" width="700" />
</p>

<p align="center">
  <strong>Figure 3:</strong> Output of JSON created on interrupt or scan completion
</p>

---

## 🎬 Watch Tutorial Video (ASCII CINEMA)
<p align="center">
  <a href="https://shravanprojects.github.io/tld-scanner-all/tld-scanner-all.gif" target="_blank">
    <img src="https://img.shields.io/badge/🎬%20Watch%20Live%20TLD%20Scanner%20Demo-Click%20Here-critical?style=for-the-badge&logo=playstation&logoColor=white&color=red" alt="Watch TLD Scanner GIF Demo"/>
  </a>
</p>



Coming Soon...


---

## 📝 Usage Example

```bash
shravan@shravan-pc:~/tld-all-scanner$ source venv/bin/activate
./domains.py
/*       _\|/_
         (o o)
 +----oOO-{_}-OOo-----------------------------+
 | _____ _     ____          _    _     _     |
 ||_   _| |   |  _ \        / \  | |   | |    |
 |  | | | |   | | | |_____ / _ \ | |   | |    |
 |  | | | |___| |_| |_____/ ___ \| |___| |___ |
 |  |_| |_____|____/     /_/   \_\_____|_____||
 |                                            |
 | ____                                       |
 |/ ___|  ___ __ _ _ __  _ __   ___ _ __      |
 |\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|     |
 | ___) | (_| (_| | | | | | | |  __/ |        |
 ||____/ \___\__,_|_| |_|_| |_|\___|_|        |
 |                                            |
 +-------------------------------------------*/
╔══════════════════════════════╗
║ Developed by @shravankumaruk ║
╚══════════════════════════════╝

[+] Enter base name to scan (e.g., type "example" to check example.com, example.us, example.tlds): google
[*] Threads [5]: 
[+] Fetching Latest TLDs : 2025-07-01 13:21:41
[+] Total TLDs: 1440

Select output:
 1) AVAILABLE only
 2) TAKEN only
 3) BOTH
▶ Choice [3]: 3
[1/1440] google.abbvie                  AVAILABLE
[2/1440] google.abbott                  AVAILABLE
[3/1440] google.abb                     AVAILABLE
[4/1440] google.able                    AVAILABLE
[5/1440] google.aarp                    AVAILABLE
[6/1440] google.aaa                     AVAILABLE
[7/1440] google.abudhabi                AVAILABLE
[8/1440] google.abogado                 AVAILABLE
[9/1440] google.abc                     AVAILABLE
[10/1440] google.accenture               AVAILABLE
[11/1440] google.ac                      TAKEN
[12/1440] google.academy                 AVAILABLE
[13/1440] google.accountant              AVAILABLE
[14/1440] google.ads                     AVAILABLE
[15/1440] google.aco                     AVAILABLE
[16/1440] google.accountants             AVAILABLE
[17/1440] google.actor                   AVAILABLE
[18/1440] google.ae                      TAKEN
[19/1440] google.aeg                     AVAILABLE
[20/1440] google.aetna                   AVAILABLE
[21/1440] google.aero                    AVAILABLE
^C
[!] Interrupted! Saving progress...
[+] Partial results saved to google_partial.json


```



## 🛠️ Maintenance & Support

If you encounter any bugs, issues, or discover a potential vulnerability 🐞🔐, please help us improve by opening an issue.

Click the button below to report it directly:

<p align="center">
  <a href="https://github.com/shravankumaruk/tld-all-scanner/issues" target="_blank">
    <img src="https://img.shields.io/badge/Report%20an%20Issue-GitHub-blue?style=for-the-badge&logo=github" alt="Report an Issue"/>
  </a>
</p>

We have **custom labels** like `bug`, `security`, `enhancement`, and `question` to categorize and speed up triage.  
Your feedback keeps this project secure and strong 💪!





---


## 📄 License & Credits

<p align="center">
  <img src="https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge&logo=gnu" alt="GPL 3.0 License" />
</p>

© 2025 Shravan Kumar UK

This project is licensed under **GNU GPL v3.0**. See [LICENSE](LICENSE) for details.
