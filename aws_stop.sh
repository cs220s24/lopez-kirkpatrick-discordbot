#!/bin/bash 

# stops the service files to close the redis server and discord bot
sudo systemctl stop redis6
sudo systemctl stop discordbot.service
