import mysql.connector

print("Testing MySQL connection...")
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # No password
        database='gs'  # Your database name
    )
    print("Connection successful!")

    # Optionally, you can run a simple query to test
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")  # This will list all tables in the database
    tables = cursor.fetchall()
    print("Tables in the database:", tables)

    cursor.close()
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")
