# C++ hello world: three builds

Run from this directory on Linux with a C++ compiler and static libraries installed.

## 1. Compile locally

```sh
g++ -static -o local/hello hello.cpp
docker compose -f local/compose.yaml up --build
```

## 2. Compile inside the final image

```sh
docker compose -f compiler/compose.yaml up --build
```

The final image includes the compiler and build tools.

## 3. Multi-stage build

```sh
docker compose -f multistage/compose.yaml up --build
docker image ls hello
```

The final stage copies the executable into `scratch`, leaving the compiler behind. The container builds need the `gcc:14` image. The generated `local/hello` executable is not committed.
