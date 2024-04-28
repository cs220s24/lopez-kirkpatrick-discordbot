#!/bin/bash 

# Copies service file to system directory
sudo cp discordbot.service /etc/systemd/system
# Creates VM
python3 -m venv .venv
# Installs the requirements for the bot
.venv/bin/pip install -r requirements.txt
# Enables the required service files
sudo systemctl enable redis6
sudo systemctl enable discordbot.service
