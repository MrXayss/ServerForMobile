#!/bin/bash
tar -czRf`date +%d-%m-%Y`.tgz db
docker build --tag signal:latest .
docker stop signal-server
docker rm signal-server
docker run -v $(pwd)/db:/Server/db -v $(pwd)/media:/Server/media -d --name signal-server --restart unless-stopped --network lan signal:latest
