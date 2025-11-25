#!/bin/bash

echo "🔄 Uninstalling Node.js..."

# Remove Node + NPM
sudo apt remove -y nodejs npm
sudo apt purge -y nodejs npm
sudo apt autoremove -y

echo "✔ Node.js removed successfully."

echo "🔄 Reinstalling Node.js (LTS version)..."

# Add NodeSource repo for latest LTS (e.g., 20.x or latest available)
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -

# Install Node.js
sudo apt install -y nodejs

echo "✔ Node.js reinstalled successfully."

echo "Node version: $(node -v)"
echo "NPM version:  $(npm -v)"
