import pickle
import xgboost as xgb

try:
    with open("backend/xgb_model.pkl", "rb") as file:
        model = pickle.load(file)
    print("Model loaded successfully!")
    print(model)
except Exception as e:
    print("Error loading model:", e)
