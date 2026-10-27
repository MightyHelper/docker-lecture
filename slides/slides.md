---
theme: default
title: Docker
colorSchema: dark
transition: fade
---

# Docker

## Operating Systems

---

# Hello, Docker

```sh
docker run hello-world
```

```sh
docker run --rm -p 8000:8000 ghcr.io/mightyhelper/docker-lecture:v0
```

`localhost:8000` · `localhost:8000/docs`

---

# Containerization

<div class="timeline">
  <div><strong>1982</strong><span>chroot</span></div>
  <div><strong>2002</strong><span>namespaces</span></div>
  <div><strong>2008</strong><span>cgroups · LXC</span></div>
  <div><strong>2013</strong><span>Docker</span></div>
</div>

---

# Namespaces

PID · network · mount · UTS

IPC · user · cgroup · time

---

# Containers & virtual machines

Linux kernel · Windows containers · WSL 2

<div class="flow">CLI <b>→</b> daemon <b>→</b> container</div>

---

# Images & containers

<div class="flow">Registry <b>→</b> image <b>→</b> container</div>

```sh
docker version
docker info
```

---

# Container lifecycle

```sh
docker run -d --name api -p 8000:8000 ghcr.io/mightyhelper/docker-lecture:v0
```

`ps` · `start` · `stop` · `rm`

---

# Observe & interact

`logs` · `inspect` · `exec` · `attach`

`-i` · `-t` · `--help`

---

# Data & access

Ports · bind mounts · volumes · environment

```sh
docker run --rm -v "$PWD/demo-data:/data" python:3.13-slim cat /data/message.txt
```

---

# Build an image

Dockerfile · build context · `.dockerignore`

```sh
docker build -t api:v0 .
docker run --rm -p 8000:8000 api:v0
```

---

# Dockerfile

`FROM` · `WORKDIR` · `RUN` · `COPY`

`EXPOSE` · `CMD` · `ENTRYPOINT` · `USER`

---

# Layers & build cache

```sh
docker image history api:v0
```

BuildKit · Buildx

---

# Docker Compose

<div class="flow">FastAPI <b>→</b> PostgreSQL <b>→</b> volume</div>

```sh
docker compose up -d --build
docker compose ps
```

---

# Compose services

DNS · `.env` · environment

Health checks · startup order · restart policies

---

# Traefik & TLS

<div class="flow">Client <b>→</b> Traefik <b>→</b> FastAPI <b>→</b> PostgreSQL</div>

Labels · Docker socket · `pre_start` · certificates

---

# Host systemd

<div class="flow">systemd <b>→</b> Docker Compose</div>

---

# Identity & security

Users · rootless · user namespaces

Capabilities · privileged · seccomp · AppArmor · SELinux

Devices · sockets · Docker-in-Docker

---

# Images & registries

Docker Hub · GHCR · Harbor

<div class="flow">Repository <b>→</b> tag <b>→</b> index <b>→</b> manifest</div>

---

# Image identity

Tags · digests · platforms · layers

```sh
docker buildx imagetools inspect ghcr.io/mightyhelper/docker-lecture:v0
```

---

# Attestations

Provenance · SBOM · signatures · verification

```sh
docker buildx build --provenance=mode=max --sbom=true \
  -t ghcr.io/mightyhelper/docker-lecture:v0 --push demos/v0-fastapi
```

---

# Vulnerability analysis

SBOM · scanner · advisories · CI

---

# Image archives

```sh
docker save -o api.tar ghcr.io/mightyhelper/docker-lecture:v0
docker load -i api.tar
```

---

# C++ & scratch

1. Local compiler → scratch
2. Compiler image → compiler image
3. Builder stage → scratch

---

# Namespaces & cgroups

Process IDs · network · mounts

CPU · memory · resource limits

```sh
docker stats
```

---

# PID 1

Signals · child processes · `--init`

---

# Storage internals

Layers · writable layer · overlay

Copy-on-write · copy-up · volumes

```sh
docker diff CONTAINER
```

---

# Networking

<div class="flow">Container <b>→</b> veth <b>→</b> bridge <b>→</b> host</div>

DNS · ports · network namespaces

---

# Performance

CPU · memory · storage · network · virtualization

---

# Runtimes

containerd · runc · crun · youki

CRI-O · gVisor · Kata Containers · OCI

---

# NVIDIA GPUs

```sh
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

NVIDIA Container Toolkit

---

# Back to the beginning

```sh
docker run --rm -p 8000:8000 ghcr.io/mightyhelper/docker-lecture:v0
```

<div class="flow">CLI <b>→</b> daemon <b>→</b> containerd <b>→</b> shim <b>→</b> runtime <b>→</b> process</div>

---

# Keep exploring

Contexts · plugins · dev containers
