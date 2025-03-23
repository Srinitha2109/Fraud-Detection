
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("backend/xgb_model.pkl")

# Define categorical mapping for transaction type
transaction_mapping = {
    "online": 0, "offline": 1, "wire_transfer": 2, "UPI": 3, "debit_card": 4, "credit_card": 5
}

@app.route('/')
def home():
    return "Fraud Detection API is running! Use the `/predict` endpoint to make predictions."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Ensure input is in the correct format
        if not isinstance(data, list):
            return jsonify({"error": "Invalid input format, expected a list of transactions"}), 400

        df = pd.DataFrame(data)

        # Encode transaction type using fixed mapping
        df["transaction_type"] = df["transaction_type"].map(transaction_mapping).fillna(-1)

        # Dynamically encode location
        if "location" in df.columns:
            df["location"] = df["location"].astype("category").cat.codes

        # Ensure no null values exist after mapping
        if df.isnull().values.any():
            return jsonify({"error": "Invalid input detected"}), 400

        # Predict fraud
        prediction = model.predict(df)

        return jsonify([{"fraud_detected": bool(pred)} for pred in prediction])

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
