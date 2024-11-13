import mysql.connector

__cnx = None

def get_sql_connection():
    print("Opening MySQL connection")
    global __cnx

    if __cnx is None:
        try:
            __cnx = mysql.connector.connect(
                user='root', 
                password='',  # Add your MySQL password if required
                database='gs'
            )
            print("Connected to MySQL successfully!")
        except mysql.connector.Error as err:
            print(f"Error: Could not connect to MySQL. {err}")
            __cnx = None

    return __cnx



