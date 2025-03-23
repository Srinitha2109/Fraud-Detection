import joblib
import pandas as pd

# Load trained model
model = joblib.load("backend/xgb_model.pkl")

# Sample new transaction
new_transaction = pd.DataFrame({
    "user_id": [2],
    "amount": [12000],
    "transaction_type": [1],  # Encoded category
    "location": [2]  # Encoded location
})

# Predict Fraud
prediction = model.predict(new_transaction)

if prediction[0] == 1:
    print("🚨 Fraud Detected!")
else:
    print("✅ Transaction is Safe.")
