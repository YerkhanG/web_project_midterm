# Game Scores API

REST API for storing game scores (player, game, points). The backend is written with Django REST Framework, the database is PostgreSQL, and the whole project runs in Docker using Docker Compose.

## Technologies

- Python 3.12, Django, Django REST Framework, gunicorn
- PostgreSQL 16
- Docker, Docker Compose

## Architecture

The project has two containers:

- `backend` - the API. It is built from `backend/Dockerfile` and its port 8000 is published to the host.
- `db` - PostgreSQL, built from the official `postgres:16-alpine` image. Its port is not published, so it can only be reached from inside Docker.

Both containers are in one network, `app-net`. The backend connects to the database using the service name `db` as the host.

The database files are stored in the named volume `pgdata`, so the data is still there after the containers are removed.

## Running the project

A `.env` file is needed in the project root. The variable names are in `.env.example`.

```
docker compose up --build
```

The API is then available at http://localhost:8000/api/scores/

The tables are created automatically when the backend starts (`python manage.py migrate` in the Dockerfile `CMD`).

To stop the containers:

```
docker compose down
```

This keeps the data. To delete the data as well: `docker compose down -v`.

## Environment variables

| Variable | Description |
|----------|-------------|
| DJANGO_SECRET_KEY | secret key of Django |
| DJANGO_DEBUG | 1 for debug mode, 0 to turn it off |
| DB_NAME | name of the database |
| DB_USER | database user |
| DB_PASSWORD | database password |

## API

| Method | URL | Description |
|--------|-----|-------------|
| GET | /api/scores/ | list all scores |
| POST | /api/scores/ | create a score |
| GET | /api/scores/{id}/ | get a score by id |
| PUT | /api/scores/{id}/ | update a score |
| PATCH | /api/scores/{id}/ | update some fields of a score |
| DELETE | /api/scores/{id}/ | delete a score |


## Postman

The collection is in `postman/Game_Scores_API.postman_collection.json`. It has one request for each endpoint. The requests should be run in order, because the create request saves the new id in a variable and the next requests use it.

## Project structure

```
compose.yaml          services, network and volume
.env.example          names of the environment variables
backend/
    Dockerfile
    requirements.txt
    manage.py
    config/           Django settings and main urls
    hub/              model, serializer, view and urls of the scores
docs/API.md           API documentation
postman/              Postman collection
```