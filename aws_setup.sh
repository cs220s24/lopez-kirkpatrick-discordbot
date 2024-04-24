sudo cp discordbot.service /etc/systemd/system
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
sudo systemctl enable redis6
sudo systemctl enable discordbot.service
