from fastapi import FastAPI, HTTPException
from .routers import users, messages
from .services import util
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse, JSONResponse, HTMLResponse

app = FastAPI()

# This is only really for serving test files. We would probably serve static
# files from S3 directly.
app.mount("/static", StaticFiles(directory="/vue/dist"), name="static")

app.include_router(users.router, prefix="/api/users")
app.include_router(messages.router, prefix="/api/messages")


@app.get("/.*", include_in_schema=False)
def root():
    with open('/vue/dist/index.html') as f:
        return HTMLResponse(content=f.read(), status_code=200)


@app.get("/log-output-test")
def log_output_test():
    util.logger.debug("logging debug")
    util.logger.info("logging info")
    util.logger.warn("logging warning")
    util.logger.error("logging error")
    return {"msg": "Logging output"}