# lopez-kirkpatrick-discordbot

# Overview

<img width="882" alt="Screenshot 2024-04-25 at 9 54 22 AM" src="https://github.com/cs220s24/lopez-kirkpatrick-discordbot/assets/109396828/6e5fb82a-945b-43d7-923c-913514cbd185">


This is a simple discord bot that can tell jokes. This Discord bot gets jokes from a redis database. There are commands to add a joke to the data base, get a random joke from the data base, and get a specific joke from the data base. You can also say hello to the bot, and it will greet you back!


# Setup

## **To run Locally**

1. Clone the repository
2. add .env file with DISCORD_TOKEN="bot token"
3. Run `./deploy.sh`


## **To run on EC2 instance**

1. Start an EC2 instance
2. `sudo yum install -y git`
3. `sudo yum install -y redis6`
4. Clone the repo
5. Add a .env file with DISCORD_TOKEN="bot token"
6. Run `./aws_setup.sh`
7. Run `./aws_launch.sh`
8. To stop the Discord bot, run `./aws_stop.sh`

## **To run on EC2 with Docker**

1. Start an EC2 instance
2. `sudo yum install -y git`
3. `sudo yum install -y redis6`
4. Clone the repo
5. Run `./aws_docker.sh`
6. Log out and log back in to the EC2 Instance
7. Add a .env file with DISCORD_TOKEN=bot token AND REDIS_HOST=redis (NOTE: Do not put quotations around the bot token) 
8. Run `./dockstart.sh`
9. Run `docker run --name discord-bot -d --network dnet --env-file ./.env discord-bot`
10. To stop the Discord bot, run `./dockstop.sh`

# Technologies Used 

- Python - https://www.python.org
- Redis - https://redis.io
- Amazon Linux - https://aws.amazon.com/linux/amazon-linux-2023/
- Discord - https://discord.com
- Discord Developer Portal - https://discord.com/developers/docs/intro
- Docker - https://www.docker.com


# Background

https://builtin.com/software-engineering-perspectives/discord-bot-python

# Developer Workflow

<img width="778" alt="Screenshot 2024-04-29 at 6 04 38 PM" src="https://github.com/cs220s24/lopez-kirkpatrick-discordbot/assets/109396828/32b36256-6c99-4aac-9c3d-4ce554357bb7">


# Project Contributers
- Braden Kirkpatrick
- Angel Lopez
