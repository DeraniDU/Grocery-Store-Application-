# products_dao.py
from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    # Fetch product details with unit of measurement
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
