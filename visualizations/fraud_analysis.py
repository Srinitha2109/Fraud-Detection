import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/processed_transactions.csv")

# Fraud vs. Non-Fraud Count
plt.figure(figsize=(6, 4))
sns.countplot(x="is_fraud", data=df, palette="coolwarm")
plt.title("Fraudulent vs. Non-Fraudulent Transactions")
plt.xlabel("Fraud (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.savefig("visualizations/fraud_vs_nonfraud.png")
plt.show()

# Amount Distribution by Fraud
plt.figure(figsize=(8, 5))
sns.boxplot(x="is_fraud", y="amount", data=df, palette="coolwarm")
plt.title("Transaction Amounts: Fraud vs. Non-Fraud")
plt.xlabel("Fraud (0 = No, 1 = Yes)")
plt.ylabel("Transaction Amount")
plt.ylim(0, df["amount"].quantile(0.99))  # Remove extreme outliers
plt.savefig("visualizations/amount_distribution.png")
plt.show()

# Fraud Transactions by Location
plt.figure(figsize=(10, 6))
sns.countplot(y="location", hue="is_fraud", data=df, palette="coolwarm")
plt.title("Fraud Transactions by Location")
plt.xlabel("Count")
plt.ylabel("Location")
plt.savefig("visualizations/fraud_by_location.png")
plt.show()
