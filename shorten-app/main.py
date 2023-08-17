import os.path
import src.data as data
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.responses import RedirectResponse
from src.config import host
from src.shorten import shorten_token

app = FastAPI()

@app.get("/")
async def read_index():
    return FileResponse('public/index.html',media_type='text/html')

@app.get("/url/short")
async def shorten_URL(url):
    token = shorten_token()
    data.set(token,url)
    short_url = os.path.join(host,token)
    return {"message": "success","url":short_url}

@app.get("/{shorten_token}")
async def redirect(shorten_token):
    origin_url = data.get(shorten_token)
    if origin_url is None:
        origin_url = "/"
    return RedirectResponse(url=origin_url)

app.mount("/", StaticFiles(directory="public"), name="static")