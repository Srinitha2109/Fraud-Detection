import mysql.connector
import pandas as pd

def fetch_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sql@1234",
        database="fraud_detection"
    )
    cursor = conn.cursor(dictionary=True)

    query = "SELECT user_id, amount, transaction_type, location, is_fraud FROM Transactions"
    cursor.execute(query)
    data = cursor.fetchall()

    df = pd.DataFrame(data)
    df.to_csv("data/transactions.csv", index=False)

    print("✅ Data exported successfully!")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    fetch_data()
