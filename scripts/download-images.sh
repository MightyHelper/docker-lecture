#!/usr/bin/env bash
set -euo pipefail

mkdir -p images
docker pull ghcr.io/mightyhelper/docker-lecture/fastapi:latest
docker save -o images/fastapi.tar ghcr.io/mightyhelper/docker-lecture/fastapi:latest
