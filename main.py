from fastapi import FastAPI
from yt_dlp import YoutubeDL

app = FastAPI()

@app.get("/yt")
def fetch(url: str):
    ydl_opts = {"quiet": True, "skip_download": True}

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return info
