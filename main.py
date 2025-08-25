from fastapi import FastAPI, Query
from selenium_bot import find_m3u8_url

app = FastAPI()

@app.get("/scrape")
def scrape(url: str = Query(..., description="L'URL del film da cui estrarre l'm3u8")):
    m3u8_url = find_m3u8_url(url)
    if m3u8_url:
        return {"m3u8_url": m3u8_url}
    else:
        return {"error": "404"}
