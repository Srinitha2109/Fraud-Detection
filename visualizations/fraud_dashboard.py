import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html

# Load dataset
df = pd.read_csv("data/processed_transactions.csv")

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Fraud Detection Dashboard", style={"textAlign": "center"}),

    # Fraud vs Non-Fraud Pie Chart
    dcc.Graph(
        figure=px.pie(df, names="is_fraud", title="Fraudulent vs. Non-Fraudulent Transactions",
                      color_discrete_sequence=["blue", "red"])
    ),

    # Transaction Amount Distribution
    dcc.Graph(
        figure=px.box(df, x="is_fraud", y="amount", title="Transaction Amounts: Fraud vs. Non-Fraud",
                      color="is_fraud", color_discrete_sequence=["green", "red"])
    ),

    # Fraud Count by Location
    dcc.Graph(
        figure=px.histogram(df, x="location", color="is_fraud", barmode="group",
                            title="Fraud Count by Location", color_discrete_sequence=["green", "red"])
    )
])

if __name__ == '__main__':
    app.run(debug=True)
