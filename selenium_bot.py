from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import m3u8
import requests

def find_m3u8_url(url: str):
    # Configurazione Chrome headless
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Avvia Chrome con Selenium-Wire
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    link = ""

    try:
        driver.get(url)
        print("[*] Caricamento pagina...")
        time.sleep(8)  # Aspetta che il player carichi

        print("[*] Cerco URL .m3u8...")
        for request in driver.requests:
            if request.response and "https://vixsrc.to/playlist/" in request.url:
                link = request.url
                break  # Prendi il primo URL trovato

    finally:
        driver.quit()

    return link
