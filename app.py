from urllib import response
from fastapi import FastAPI
from starlette.responses import RedirectResponse


## instancia app
app = FastAPI()

app.get(path="/")
def index():
    return RedirectResponse("/docs")