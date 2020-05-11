# Docker + FastAPI + Vue

Technologies:
- Docker
- Python FastAPI
- Vue JS

docker build . --tag dockerfastapivue
docker run \
    --rm --name app \
    -p 5000:80 \
    -v ${PWD}/vue:/vue \
    -v ${PWD}/data/sqlite.db:/data/sqlite.db \
    --env-file .env \
    dockerfastapivue

docker exec -it app sqlite3 /data/sqlite.db