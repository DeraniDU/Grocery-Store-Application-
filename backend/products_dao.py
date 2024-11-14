from sql_connection import get_sql_connection

def get_all_products(connection):
    # Fetch all products with their UOM name from the database
    cursor = connection.cursor()
    query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
             "FROM products INNER JOIN uom ON products.uom_id = uom.uom_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    cursor.close()
    return response

def insert_new_product(connection, product):
    # Insert a new product into the products table
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit) "
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    cursor.close()
    return cursor.lastrowid  # Return the ID of the inserted product

def delete_product(connection, product_id):
    # Delete a product from the products table by product_id
    cursor = connection.cursor()
    query = ("DELETE FROM products WHERE product_id = %s")
    data = (product_id,)

    cursor.execute(query, data)
    connection.commit()

    cursor.close()
    return product_id  # Return the ID of the deleted product

if __name__ == '__main__':
    connection = get_sql_connection()
    
    # Testing insert new product
    print(insert_new_product(connection, {
        'product_name': 'potatoes',
        'uom_id': 1,  # Assuming 1 is a valid UOM ID
        'price_per_unit': 10
    }))
    
    # Example of deleting a product (use a valid product_id for testing)
    # print(delete_product(connection, 1))  # Uncomment to test deletion
