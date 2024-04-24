docker build -t discordbot .
docker network create net
docker run --name redis --netowrk net -d redis

