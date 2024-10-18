import mysql.connector

def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  # No password
            database='gs'  # Your database name
        )
        return conn
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

def fetch_products():
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                SELECT products.product_id, products.name, products.uom_id, 
                       products.price_per_unit, uom.uom_name 
                FROM products 
                INNER JOIN uom ON products.uom_id = uom.uom_id
            """
            cursor.execute(query)
            products = cursor.fetchall()

            # Print the table headers
            print("Product ID, Name, UOM ID, Price per Unit, UOM Name")
            for product in products:
                print(product)

            cursor.close()
        except Exception as e:
            print(f"Error fetching products: {e}")
        finally:
            conn.close()

def add_product(name, uom_id, price_per_unit):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO products (name, uom_id, price_per_unit) 
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (name, uom_id, price_per_unit))
            conn.commit()
            print("Product added successfully!")

            cursor.close()
        except Exception as e:
            print(f"Error adding product: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    print("Testing MySQL connection...")
    conn = connect_to_db()
    if conn:
        print("Connection successful!")
        conn.close()

        # Fetch and display existing products
        fetch_products()

        # Input details for the new product
        name = input("Enter product name: ")
        uom_id = int(input("Enter UOM ID (1 or 2): "))
        price_per_unit = float(input("Enter price per unit: "))

        # Add the new product
        add_product(name, uom_id, price_per_unit)

        # Fetch and display updated products list
        fetch_products()
    else:
        print("Could not connect to the database.")
