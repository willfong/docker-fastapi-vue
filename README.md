# Docker + FastAPI + Vue

Technologies:
- Docker
- Python FastAPI
- Vue JS

## Docker Build Commands

Create image locally:
```
docker build . --tag dockerfastapivue
```

Run an instance:
```
docker run \
    --rm --name app \
    -p 5000:80 \
    -v ${PWD}/vue:/vue \
    -v ${PWD}/data/sqlite.db:/data/sqlite.db \
    --env-file .env \
    dockerfastapivue
```

Access the database directly:
```
docker exec -it app sqlite3 /data/sqlite.db
```

## GitHub Auth Flow

https://developer.github.com/v3/users/#get-the-authenticated-user
