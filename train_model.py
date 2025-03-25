import pandas as pd
import json
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

USER_FEEDBACK_FILE = "user_feedback.csv"
PRODUCT_FILE = "apple_products.json"

# 🚀 Last inn produkter
with open(PRODUCT_FILE, "r", encoding="utf-8") as f:
    apple_data = json.load(f)

# 🔄 Bygg treningsdata
rows = []

for kategori, produkter in apple_data.items():
    for produkt in produkter:
        rows.append({
            "budget": int(produkt["pris"]),
            "performance": 8 if "Pro" in produkt["produktnavn"] else 5,
            "battery": 8,
            "size": 1 if "Max" in produkt["produktnavn"] or "15" in produkt["produktnavn"] else 0,
            "camera": 9 if "Pro" in produkt["produktnavn"] else 6,
            "storage": 256,
            "device": produkt["produktnavn"]
        })

df = pd.DataFrame(rows)

# ➕ Legg til feedback hvis det finnes
if os.path.exists(USER_FEEDBACK_FILE):
    feedback = pd.read_csv(USER_FEEDBACK_FILE)
    df = pd.concat([df, feedback], ignore_index=True)

# 🧹 Fjern rader med manglende data
df = df.dropna()

# ✅ Sjekk datatyper
print("📊 Datatyper før trening:")
print(df.dtypes)

# 🔁 Trening
X = df.drop(columns=["device"])
y = df["device"]

print("🔍 Trener modellen på følgende antall rader:", len(df))
print("📈 Produkter:", df["device"].unique())

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 💾 Lagre modell
with open("device_recommendation_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Modell trent og lagret.")

