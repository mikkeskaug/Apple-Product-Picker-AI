import pickle
import pandas as pd
import os
import subprocess  # 🚀 Lar oss kjøre `train_model.py` automatisk
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

USER_FEEDBACK_FILE = "user_feedback.csv"

@app.route("/feedback", methods=["POST", "OPTIONS"])
def feedback():
    if request.method == "OPTIONS":
        return '', 200  # ✅ Løser OPTIONS-feilen

    data = request.json
    print("\n🔍 Mottatt JSON-data:", data)

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

        # 🚀 **Tren AI-modellen etter hver tilbakemelding**
        print("🔄 Trener AI-en med ny tilbakemelding...")
        subprocess.run(["python3", "train_model.py"])  # Kjører `train_model.py`

    return jsonify({"message": "Takk for tilbakemeldingen! AI er nå smartere!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
