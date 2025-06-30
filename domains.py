#!/usr/bin/env python3
"""
TLD-ALL Scanner V1.0

A terminal-based domain availability scanner across all IANA TLDs.

Usage:
  python3 domains.py

Dependencies:
  pip install python-whois dnspython requests pyfiglet colorama
  sudo apt install boxes lolcat figlet

Author: @shravankumaruk
"""

import sys
import json
import signal
import logging
import socket
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from datetime import datetime

import requests
import whois
import dns.resolver
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)
# Suppress noisy whois logs
logging.getLogger('whois').setLevel(logging.CRITICAL)
# Global socket timeout
socket.setdefaulttimeout(10)

DEFAULT_THREADS = 5
IANA_TLD_URL = 'https://data.iana.org/TLD/tlds-alpha-by-domain.txt'

# Shared state for progress
results = []
lock = Lock()
processed = 0


def fetch_tlds():
    r = requests.get(IANA_TLD_URL, timeout=10)
    r.raise_for_status()
    return [l.strip().lower() for l in r.text.splitlines() if l and not l.startswith('#')]


def check_availability(name, tld):
    domain = f"{name}.{tld}"
    available = False
    try:
        w = whois.whois(domain)
        if not w.domain_name:
            available = True
    except Exception:
        available = True
    if not available:
        try:
            res = dns.resolver.Resolver()
            res.timeout = 5; res.lifetime = 5
            res.resolve(domain, 'A')
            available = False
        except Exception:
            available = True
    return domain, available


def save_progress(name):
    fn = f"{name}_partial.json"
    with open(fn, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"{Fore.MAGENTA}[+] Partial results saved to {fn}{Style.RESET_ALL}")


def signal_handler(sig, frame):
    print(f"\n{Fore.YELLOW}[!] Interrupted! Saving progress...{Style.RESET_ALL}")
    save_progress(current_name)
    sys.exit(0)


def print_banner():
    try:
        # figlet -> boxes peek -> lolcat
        p1 = subprocess.Popen(['figlet', '-f', 'standard', 'TLD-ALL Scanner'], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['boxes', '-d', 'peek'], stdin=p1.stdout, stdout=subprocess.PIPE)
        p3 = subprocess.Popen(['lolcat'], stdin=p2.stdout)
        p3.communicate()
    except Exception:
        print(Fore.CYAN + '=== TLD-ALL Scanner V1.0 ===')
    # Author box
    author = ' Developed by @shravankumaruk '
    print(Fore.GREEN + '╔' + '═' * len(author) + '╗')
    print(Fore.GREEN + '║' + author + '║')
    print(Fore.GREEN + '╚' + '═' * len(author) + '╝')
    print()


def main():
    global processed, results, current_name
    signal.signal(signal.SIGINT, signal_handler)
    print_banner()

    prompt = f"[+] Enter base name to scan (e.g., type \"example\" to check example.com, example.us, example.tlds): "
    current_name = input(Fore.CYAN + prompt + Style.BRIGHT).strip().lower()
    if not current_name:
        print(Fore.RED + '[!] No input, exiting.')
        sys.exit(1)

    thr_input = input(Fore.YELLOW + f'[*] Threads [{DEFAULT_THREADS}]: ' + Style.BRIGHT).strip()
    try:
        threads = int(thr_input) if thr_input else DEFAULT_THREADS
    except ValueError:
        print(Fore.YELLOW + '[!] Invalid number, using default.')
        threads = DEFAULT_THREADS

    # Fetching with timestamp
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{Fore.CYAN}[+] Fetching Latest TLDs : {now}{Style.RESET_ALL}")
    tlds = fetch_tlds(); total = len(tlds)
    print(f"{Fore.CYAN}[+] Total TLDs: {total}{Style.RESET_ALL}\n")

    # Output choice
    print(Fore.MAGENTA + 'Select output:')
    print(Fore.GREEN + ' 1) AVAILABLE only')
    print(Fore.RED + ' 2) TAKEN only')
    print(Fore.CYAN + ' 3) BOTH')
    choice = input(Fore.MAGENTA + '▶ Choice [3]: ' + Style.BRIGHT).strip() or '3'
    if choice not in ('1','2','3'):
        choice = '3'

    # Scanning
    with ThreadPoolExecutor(max_workers=threads) as ex:
        futures = {ex.submit(check_availability, current_name, t): t for t in tlds}
        for fut in as_completed(futures):
            dom, avail = fut.result()
            with lock:
                processed += 1
                meta = f"[{processed}/{total}]"
            if choice == '1' and not avail: continue
            if choice == '2' and avail: continue
            tag = 'AVAILABLE' if avail else 'TAKEN'
            color = Fore.GREEN if avail else Fore.RED
            print(f"{Fore.YELLOW}{meta} {Fore.WHITE}{dom:30} {color}{tag}")
            results.append({'domain': dom, 'available': avail})

    # Save final
    fn = f"{current_name}.json"
    with open(fn, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n{Fore.MAGENTA}[+] Saved results to {fn}{Style.RESET_ALL}")

if __name__ == '__main__':
    main()
