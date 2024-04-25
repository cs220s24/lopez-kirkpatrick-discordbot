docker build -t discord-bot .
docker network create dnet
docker run --name redis --network dnet -d redis

