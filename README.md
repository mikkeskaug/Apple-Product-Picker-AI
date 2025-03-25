# 🍏 Apple AI-Anbefaler

Et selv-lærende anbefalingssystem som hjelper brukere å finne riktig Apple-produkt (iPhone, Mac, iPad) basert på behov, budsjett og preferanser.

## 🔥 Funksjoner

✅ Gir anbefaling basert på:
- Budsjett
- Ønsket enhetstype (iPhone, Mac, iPad)
- Ytelse, batteri, skjermstørrelse, kamera, lagring

✅ AI-modell trent med ekte Apple-produkter og priser

✅ Bruker kan gi tilbakemelding (bra/dårlig) – og modellen trener seg automatisk videre

✅ HTML-grensesnitt med moderne design (Bootstrap)

✅ Full frontend-backend-integrasjon med Flask og `fetch`

---

## 🏗 Mappestruktur

/project-folder/
│
├── app.py                   # Flask backend med /anbefal og /feedback
├── train_model.py           # Trener og lagrer AI-modellen
├── apple_products.json      # Liste over Apple-produkter og priser
├── user_feedback.csv        # Tilbakemeldinger fra brukere
├── device_recommendation_model.pkl   # Trenet AI-modell
├── index.html               # Frontend-grensesnitt
├── update_products.py       # (valgfritt) Script for å oppdatere produkter
└── README.md                # Denne filen

---

## 🚀 Kom i gang

### 1. Installer avhengigheter

```bash
pip install flask flask-cors pandas scikit-learn

## WebScraping
pip install beautifulsoup4 requests selenium webdriver-manager

### 2. Lag produktfil

Bruk apple_products.json (lagret manuelt eller hentet med script).
Eksempel finnes i prosjektet allerede.

### 3. Tren modellen

python3 train_model.py


