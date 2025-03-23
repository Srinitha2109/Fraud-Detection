import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import xgboost as xgb

# Load processed data
df = pd.read_csv("data/processed_transactions.csv")

# Define features and target variable
X = df.drop(columns=["is_fraud"])  
y = df["is_fraud"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Save Random Forest model
joblib.dump(rf_model, "backend/model.pkl")

# Train XGBoost Model
xgb_model = xgb.XGBClassifier(n_estimators=200, learning_rate=0.05, random_state=42)
xgb_model.fit(X_train, y_train)

# Save XGBoost model
joblib.dump(xgb_model, "backend/xgb_model.pkl")

# Evaluate models
y_pred_rf = rf_model.predict(X_test)
y_pred_xgb = xgb_model.predict(X_test)

print("✅ Random Forest Accuracy:", accuracy_score(y_test, y_pred_rf))
print("✅ XGBoost Accuracy:", accuracy_score(y_test, y_pred_xgb))
print("\nRandom Forest Report:\n", classification_report(y_test, y_pred_rf))
print("\nXGBoost Report:\n", classification_report(y_test, y_pred_xgb))
