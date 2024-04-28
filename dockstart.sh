#!/bin/bash

# Builds the discord bot imagae
docker build -t discord-bot .
# Creates a network to have a discord bot container and a redis container be able to communicate with each other
docker network create dnet
# Creates a redis container in the network
docker run --name redis --network dnet -d redis

