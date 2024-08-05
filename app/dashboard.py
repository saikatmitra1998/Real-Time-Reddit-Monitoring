import os
import psycopg2
import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection
def get_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT")
    )

# Fetch data from the database
def fetch_data():
    conn = get_connection()
    query = "SELECT * FROM reddit_data"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Create Dash application
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define layout
app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("Reddit Data Dashboard"), className="mb-4")),
    dbc.Row(dbc.Col(dcc.Graph(id='bar-chart'))),
    dcc.Interval(id='interval-component', interval=60*1000, n_intervals=0)  # Refresh data every minute
])

# Update the bar chart based on the data
@app.callback(
    dash.dependencies.Output('bar-chart', 'figure'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_chart(n):
    df = fetch_data()
    fig = px.bar(df, x='subreddit', y='num_comments', color='subreddit',
                 title="Number of Comments per Subreddit")
    return fig

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')