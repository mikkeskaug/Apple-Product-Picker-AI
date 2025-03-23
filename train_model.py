import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Last inn opprinnelig datasett
data = {
    "budget": [16000, 15000, 14000, 13000, 12000, 18000, 35000, 9000, 8000, 13000],
    "performance": [10, 10, 7, 7, 6, 9, 10, 6, 5, 7],
    "battery": [9, 8, 9, 8, 7, 9, 10, 7, 6, 9],
    "size": [1, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    "camera": [9, 9, 7, 7, 6, 9, 10, 5, 4, 7],
    "storage": [256, 256, 128, 128, 128, 512, 1024, 128, 128, 128],
    "device": [
        "iPhone 16 Pro Max", "iPhone 16 Pro", "iPhone 16", "iPhone 16e",
        "MacBook Air 15\" (M4)", "MacBook Pro 16\" (M4 Max)",
        "iPad Air 11\" (M3)", "iPad 11th Gen", "iPhone 16 Plus"
    ]
}

df = pd.DataFrame(data)

# ✅ Hvis vi har brukerfeedback, legg den til
USER_FEEDBACK_FILE = "user_feedback.csv"
if os.path.exists(USER_FEEDBACK_FILE):
    user_df = pd.read_csv(USER_FEEDBACK_FILE)
    df = pd.concat([df, user_df], ignore_index=True)

# Tren AI-en med både original + brukerdata
X = df.drop(columns=["device"])
y = df["device"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Lagre den oppdaterte AI-modellen
with open("device_recommendation_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("✅ AI er nå oppdatert med ny brukerdata!")
