from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes.user import user


## create instance for FastApi
app = FastAPI()
app.include_router(user)


## path operation for redirect to documentation
@app.get(path="/",
         tags=["index"])
def index():
    return RedirectResponse("/docs")