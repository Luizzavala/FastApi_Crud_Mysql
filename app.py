from fastapi import FastAPI
from starlette.responses import RedirectResponse
from routes.user import user


## create instance for FastApi
app = FastAPI()
app.include_router(user)


## path operation for redirect to documentation
@app.get(path="/",
         tags=["index"])
def index():
    return RedirectResponse("/docs")