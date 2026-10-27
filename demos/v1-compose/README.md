# FastAPI and PostgreSQL

Start the application:

```sh
docker compose up -d --build
```

Visit http://localhost:8000/docs to use the API, or run:

```sh
curl -X POST http://localhost:8000/messages -H 'Content-Type: application/json' -d '{"text":"Hello, Docker!"}'
curl http://localhost:8000/messages
```

Recreate the containers and check that the message is still there:

```sh
docker compose down
docker compose up -d
curl http://localhost:8000/messages
```

`docker compose down` keeps the database volume. Use `docker compose down -v` to remove it and its data when finished. The credentials in this example are for the lecture only.
