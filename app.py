import pickle
import pandas as pd
import os
import subprocess
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

USER_FEEDBACK_FILE = "user_feedback.csv"
MODEL_FILE = "device_recommendation_model.pkl"

# 🔄 Laster AI-modellen (hvis den finnes)
def load_model():
    if os.path.exists(MODEL_FILE):
        with open(MODEL_FILE, "rb") as file:
            return pickle.load(file)
    return None

model = load_model()

@app.route("/anbefal", methods=["POST"])
def anbefal():
    global model
    if model is None:
        model = load_model()
        if model is None:
            return jsonify({"error": "Modellen er ikke trent enda."}), 500

    data = request.json
    print("🔍 Forespørsel mottatt:", data)

    try:
        input_data = pd.DataFrame([{
            "budget": int(data["budsjett"]),
            "performance": 10 if data["ytelse"] == "yes" else 5,
            "battery": 10 if data["batteri"] == "yes" else 5,
            "size": 1 if data["størrelse"] == "stor" else 0,
            "camera": 10 if data["kamera"] == "yes" else 5,
            "storage": int(data["lagring"])
        }])

        prediction = model.predict(input_data)[0]
        return jsonify({"anbefalt_enhet": prediction})

    except Exception as e:
        print("❌ Feil under anbefaling:", e)
        return jsonify({"error": "Kunne ikke behandle forespørselen."}), 400

@app.route("/feedback", methods=["POST", "OPTIONS"])
def feedback():
    if request.method == "OPTIONS":
        return '', 200

    data = request.json
    print("\n🔍 Mottatt feedback:", data)

    if data is None:
        return jsonify({"error": "Ingen JSON-data mottatt"}), 400

    required_fields = ["budsjett", "enhetstype", "ytelse", "batteri", "størrelse", "kamera", "lagring", "feedback"]
    manglende_felt = [field for field in required_fields if field not in data]
    if manglende_felt:
        return jsonify({"error": f"Mangler felt: {', '.join(manglende_felt)}"}), 400

    if data["feedback"] == "bad" and "riktigEnhet" not in data:
        return jsonify({"error": "Mangler riktig enhet i tilbakemelding!"}), 400

    if data["feedback"] == "bad":
        feedback_data = pd.DataFrame([{
            "budget": int(data["budsjett"]),
            "performance": 10 if data["ytelse"] == "yes" else 5,
            "battery": 10 if data["batteri"] == "yes" else 5,
            "size": 1 if data["størrelse"] == "stor" else 0,
            "camera": 10 if data["kamera"] == "yes" else 5,
            "storage": int(data["lagring"]),
            "device": data["riktigEnhet"]
        }])

        if not os.path.exists(USER_FEEDBACK_FILE):
            feedback_data.to_csv(USER_FEEDBACK_FILE, index=False)
        else:
            feedback_data.to_csv(USER_FEEDBACK_FILE, mode="a", header=False, index=False)

        print("🔄 Trener AI-modellen på nytt med ny tilbakemelding...")
        subprocess.run(["python3", "train_model.py"])
        model = load_model()

    return jsonify({"message": "Takk for tilbakemeldingen! AI er nå smartere!"}), 200

@app.route("/apple_products.json")
def send_apple_products():
    return send_from_directory(".", "apple_products.json")

if __name__ == "__main__":
    app.run(debug=True)
