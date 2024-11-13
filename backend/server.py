from flask import Flask, jsonify
import products_dao
from sql_connection import get_sql_connection  # Import the get_sql_connection function

app = Flask(__name__)

# Initialize the database connection
connection = get_sql_connection()

@app.route('/getProducts', methods=['GET'])
def get_products():
    # Fetch products from the database using products_dao
    products = products_dao.get_all_products(connection)
    return jsonify(products)  # Return the products as a JSON response

if __name__ == "__main__":
    print("Testing MySQL connection...")
    app.run(port=5000)
