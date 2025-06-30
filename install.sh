#!/usr/bin/env bash
set -e

echo "🛠  Updating package lists…"
sudo apt-get update

echo "🐍  Installing Python3, venv support & full stdlib…"
sudo apt-get install -y python3 python3-full python3-venv

echo "📦  Installing system dependencies (boxes, figlet, lolcat)…"
sudo apt-get install -y boxes figlet lolcat

# Create & activate venv
if [ ! -d "venv" ]; then
  echo "📁  Creating virtual environment in ./venv…"
  python3 -m venv venv
fi

echo "🔑  Activating virtual environment…"
# shellcheck disable=SC1091
source venv/bin/activate

echo "🔄  Upgrading pip in venv…"
pip install --upgrade pip

echo "🔧  Installing required Python packages…"
pip install python-whois dnspython requests pyfiglet colorama

echo "✅  Setup complete!"
echo "👉  To start the scanner, run:"
echo "      source venv/bin/activate"
echo "      chmod +x domains.py"
echo "      ./domains.py"
