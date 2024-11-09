import psycopg

def test_connection():
    try:
        conn = psycopg.connect(
            dbname="<DatabaseName>",
            user="<UserName>",
            password="<Password>",
            host="<Host>",
            port=5432
        )
        print("Connection successful!")
        print(conn.cursor().execute("SELECT * FROM users").fetchall())
        conn.close()
    except Exception as e:
        print(f"Connection failed: {e}")

test_connection()