import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def konfigurer_driver():
    options = Options()
    options.add_argument("--headless")  # Usynlig nettleser
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def hent_produkter(url):
    driver.get(url)
    try:
        # Vent på at prisene vises på siden
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.as-price-currentprice"))
        )
    except:
        print(f"⚠️ Kunne ikke hente produkter fra: {url}")
        return []

    soup = BeautifulSoup(driver.page_source, "html.parser")
    produkter = []

    for tile in soup.select("div.as-price-currentprice"):
        tittel = tile.find_previous("h3")
        pris = tile.get_text(strip=True)
        if tittel and pris:
            produkter.append({
                "produktnavn": tittel.get_text(strip=True),
                "pris": pris
            })
    return produkter

# Kategorier og URL-er fra Apple Store Norge
urls = {
    "iphone": "https://www.apple.com/no/shop/buy-iphone",
    "macbook": "https://www.apple.com/no/shop/buy-mac",
    "ipad": "https://www.apple.com/no/shop/buy-ipad"
}

resultater = {}
driver = konfigurer_driver()

for kategori, url in urls.items():
    print(f"🔄 Henter {kategori}...")
    resultater[kategori] = hent_produkter(url)
    print(f"✅ Fant {len(resultater[kategori])} produkter for {kategori}")

driver.quit()

# Lagre til JSON
with open("apple_products.json", "w", encoding="utf-8") as f:
    json.dump(resultater, f, indent=2, ensure_ascii=False)

print("✅ Produktene er lagret i apple_products.json")