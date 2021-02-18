FROM node:latest AS build
COPY ./vue /vue
WORKDIR /vue
RUN npm install && npm run build

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY --from=build /vue/dist /vue/dist
COPY ./app /app/app
