#!/bin/bash

docker build --tag signal:latest .
docker stop signal-server
docker rm signal-server
docker run -v $(pwd)/db:/SeverForMobile/db -v $(pwd)/media:/SeverForMobile/media -d --name signal-server --restart unless-stopped --network lan signal:latest
