# Docker + FastAPI + Vue

Technologies:
- Docker
- Python FastAPI
- Vue JS

docker build . --tag dockerfastapivue
docker run --rm --name app -p 5000:80 dockerfastapivue
docker run --rm --name app -p 5000:80 -v ${PWD}/vue:/vue -v data/sqlite.db:/data/sqlite.db dockerfastapivue
docker exec -it app sqlite3 /data/sqlite.db