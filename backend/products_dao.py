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

    # Create a cursor
    cursor = conn.cursor()

    # Query to select specific columns from products
    query = "SELECT products.product_id,products.name,products.uom_id,products.price_per_unit,uom.uom_name FROM products inner join uom on products.uom_id=uom.uom_id"
    cursor.execute(query)

    # Fetch all results
    products = cursor.fetchall()

    # Print the table headers
    print("Product ID, Name, UOM ID, Price per Unit,Uom Name")

    # Print each product's details
    for product in products:
        print(product)

    # Close the cursor and connection
    cursor.close()
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")
