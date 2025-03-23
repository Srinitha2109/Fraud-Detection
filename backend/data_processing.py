import pandas as pd

# Load dataset
df = pd.read_csv("data/transactions.csv")

# Convert categorical columns to numeric
df["transaction_type"] = df["transaction_type"].astype("category").cat.codes
df["location"] = df["location"].astype("category").cat.codes

# Save processed data
df.to_csv("data/processed_transactions.csv", index=False)
print("✅ Data preprocessing complete!")
