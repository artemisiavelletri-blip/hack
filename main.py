from fastapi import FastAPI
from selenium_bot import run_bot

app = FastAPI()

@app.get("/get_url")
def scrape():
    title = run_bot()
    return {"url": url}
