#!/usr/bin/env bash
set -euo pipefail

mkdir -p images
for version in v0 v1; do
    image="ghcr.io/mightyhelper/docker-lecture:$version"
    docker pull "$image"
    docker save -o "images/fastapi-$version.tar" "$image"
done
docker pull postgres:17
docker save -o images/postgres.tar postgres:17
docker pull traefik:v3.6
docker save -o images/traefik.tar traefik:v3.6
docker pull alpine/openssl:3.5.5
docker save -o images/openssl.tar alpine/openssl:3.5.5
