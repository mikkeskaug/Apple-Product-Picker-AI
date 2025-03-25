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

```
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
```

---

## 🚀 Kom i gang

### 1. Installer avhengigheter

```bash
pip install flask flask-cors pandas scikit-learn
```

👉 Hvis du bruker web scraping:
```bash
pip install beautifulsoup4 requests selenium webdriver-manager
```

---

### 2. Lag produktfil

Bruk `apple_products.json` (lagret manuelt eller hentet med script).  
Eksempel finnes i prosjektet allerede.

---

### 3. Tren modellen

```bash
python3 train_model.py
```

Dette genererer `device_recommendation_model.pkl`.

---

### 4. Start backend

```bash
python3 app.py
```

Flask starter på: `http://127.0.0.1:5000`

---

### 5. Åpne frontend

Bruk en lokal webserver (for å unngå CORS-feil):

```bash
python3 -m http.server 8000
```

Åpne i nettleser:

```
http://localhost:8000/index.html
```

---

## 📦 API-endepunkter

### `POST /anbefal`

Gir anbefaling basert på brukerinput.

### `POST /feedback`

Brukes når bruker sender tilbakemelding. AI-en trenes automatisk på nytt.

---

## 💡 Videreutvikling

- Vis pris på anbefalt produkt i frontend
- Legg til flere preferanser (USB-C, Face ID, Touch ID)
- Bruk mer avansert ML (GridSearchCV, SVM, etc.)
- Lagre anbefalingshistorikk
- Deploy på Heroku / AWS

---

## 👨‍💻 Laget av

Mikkeskaug  
📬 mikkeskaug@bitbuddy.com  
🐍 Python-entusiast & Apple-bruker
