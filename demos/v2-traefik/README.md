# FastAPI, PostgreSQL and Traefik

Requires Docker Compose 5.3.0 or later. Start the stack:

```sh
docker compose up -d --build
```

Before Traefik starts, its `pre_start` init container generates a self-signed certificate in a shared volume. Visit https://localhost:8443/docs. The browser will warn that the certificate is not trusted.

Copy the public certificate and explicitly trust it for these requests:

```sh
docker compose cp proxy:/certs/localhost.crt /tmp/docker-lecture-localhost.crt
curl --cacert /tmp/docker-lecture-localhost.crt https://localhost:8443/
curl --cacert /tmp/docker-lecture-localhost.crt -X POST https://localhost:8443/messages -H 'Content-Type: application/json' -d '{"text":"Hello through Traefik!"}'
curl --cacert /tmp/docker-lecture-localhost.crt https://localhost:8443/messages
```

Traefik discovers the API from its Docker labels. The Docker socket gives Traefik access to the Docker daemon; a read-only socket mount does not restrict Docker API operations to read-only. The database and API are not published directly to the host.

Stop the stack with `docker compose down`. Add `-v` to remove the database and certificate volumes. The certificate can be regenerated on service recreation; copy the public certificate again if needed.
