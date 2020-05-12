# Docker + FastAPI + Vue

Technologies:
- Docker
- Python FastAPI
- Vue JS

## Getting Started

This guide assumes basic understanding of Docker, Python, and Javascript. 

**Getting the demo application up and running:**

1. Create a new repo using this as a template: https://github.com/willfong/docker-fastapi-vue/generate
1. Clone the new repo locally: `git clone git@github.com:willfong/test-repo.git`
1. Change to the new repo: `cd test-repo`
1. Create a `.env` file and add session secret:

   ```
   JWT_SIGNING_TOKEN=SOME_SECRET_HERE
1. Build the Docker image: `docker build --tag dockerfastapivue .`
1. Start a container named `app` from the image created above: 

   ```
   docker run \
     --rm -d \
     --name app \
     -p 5000:80 \
     -v ${PWD}/data:/data \
     --env-file .env \
     dockerfastapivue
1. Check to make sure the `app` container is still running: `docker ps`
1. Create the SQLite datafile: `docker exec -it app sqlite3 /data/sqlite.db ".read /data/schema.sql"`
1. Check the SQLite datafile to ensure there are tables: `docker exec -it app sqlite3 /data/sqlite.db .schema`
1. Open a web browser to: http://localhost:5000/
1. Click "Login" in the top right corner
1. Click "Test Account Login" and enter in any username.
1. Add a new message and see the message displayed.

**Make changes to the backend system:**

1. Check the logs from the backend: `docker logs app`
1. In `app/main.py` on line 16, add: 

   ```
   @app.get("/echo/:message")
   def echo(message: str):
     util.logger.warning(f"Message: {message}")
     return {"msg": message}
1. Stop the Docker container: `docker stop app`
1. Rebuild Docker image: `docker build --tag dockerfastapivue .`
1. Start a new container with the new image: 

   ```
   docker run \
     --rm -d \
     --name app \
     -p 5000:80 \
     -v ${PWD}/data:/data \
     dockerfastapivue
1. Test the new endpoint: `curl localhost:5000/echo/hello-world`
1. Check the Docker logs for your test message: `docker logs app`

**Make changes to the frontend system:**

1. Change to the `vue` directory: `cd vue`
1. Install the Javascript dependencies: `npm install`
1. In `src/components/navbar.vue`, change: `<h1 class="title">Example App</h1>` to `<h1 class="title">Hello App!</h1>` 
1. Build the production distribution: `npm run build`
1. Stop the existing Docker container: `docker stop app`
1. Start a new container with the new image: 

   ```
   docker run \
     --rm -d \
     --name app \
     -p 5000:80 \
     -v ${PWD}:/vue \
     -v ${PWD}/data:/data \
     dockerfastapivue
1. Open a web browser to: http://localhost:5000 and verify 


## Docker Commands

Create image locally:
```
docker build --tag dockerfastapivue .
```

Run an instance:
```
docker run \
    --rm -d \
    --name app \
    -p 5000:80 \
    -v ${PWD}/vue:/vue \
    -v ${PWD}/data:/data \
    
    dockerfastapivue
```

Access the database directly:
```
docker exec -it app sqlite3 /data/sqlite.db
```

## GitHub Auth Flow

GitHub OAuth is a bit easier to enable than Facebook and Google OAuth. 

1. Create a GitHub OAuth Application: https://github.com/settings/applications/new
1. Application Name and Homepage URL are just for display. Set Authorization callback URL to `http://localhost:5000/oauth/github`
1. Add the following to the `.env` file:

   ```
   GITHUB_CLIENT_ID=626...1d2
   GITHUB_CLIENT_SECRET=cc3...350
1. Pass the `.env` file to Docker when you create the instance:

   ```
   docker run \
     --rm -d \
     --name app \
     -p 5000:80 \
     -v ${PWD}/vue:/vue \
     -v ${PWD}/data:/data \
     --env-file .env \
     dockerfastapivue
1. You can use the GitHub login button now. 

Details about the user profile passed back from GitHub: https://developer.github.com/v3/users/#get-the-authenticated-user
