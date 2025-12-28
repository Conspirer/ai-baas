import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="ai_baas",
        user="postgres",
        password="admin",
        host="localhost",
        port=5432
    )