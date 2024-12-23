from flask import Flask, request, jsonify
from sql_connection import get_sql_connection


import products_dao
import orders_dao
import uom_dao

app = Flask(__name__)

# Initialize the database connection
connection = get_sql_connection()

# Route to fetch all UOMs (units of measurement)
@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Route to fetch all products
@app.route('/getProducts', methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Route to insert a new product
@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = request.get_json()
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Route to fetch all orders
@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Route to insert a new order
@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = request.get_json()
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Route to delete a product by product_id
@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    product_id = request.get_json().get('product_id')
    return_id = products_dao.delete_product(connection, product_id)
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)
