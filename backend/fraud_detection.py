import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # 🔹 Replace with your MySQL username
    password="sql@1234",  # 🔹 Replace with your MySQL password
    database="fraud_detection"
)
cursor = conn.cursor(dictionary=True)

# Fetch all transactions
cursor.execute("SELECT * FROM Transactions")
transactions = cursor.fetchall()

# Fraud detection function
def is_fraudulent(transaction):
    high_risk_countries = ["Russia", "Nigeria", "Hong Kong"]
    
    if transaction["amount"] > 10000:  # Rule 1: High-value transaction
        return True
    if transaction["location"] in high_risk_countries:  # Rule 2: Suspicious location
        return True
    if transaction["transaction_type"] == "Wire Transfer" and transaction["location"] not in ["New York", "Los Angeles"]:
        return True  # Rule 3: Wire transfers from unusual locations
    return False

# Apply fraud detection
fraudulent_transactions = [t for t in transactions if is_fraudulent(t)]

# Print results
if fraudulent_transactions:
    print("🚨 Fraudulent Transactions Detected:")
    for t in fraudulent_transactions:
        print(f"Transaction ID: {t['transaction_id']}, Amount: {t['amount']}, Location: {t['location']}")
else:
    print("✅ No fraudulent transactions detected.")

# Close connection
cursor.close()
conn.close()
