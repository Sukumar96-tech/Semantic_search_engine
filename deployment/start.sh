#!/usr/bin/env bash
set -e
echo "Starting services with docker-compose..."
docker-compose -f deployment/docker-compose.yml up --build
