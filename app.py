from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(
            dbname=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD"),
            host=os.environ.get("DB_HOST"),
            port="5432"
        )
        return "Connected to the database successfully!"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)