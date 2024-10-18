from flask import Flask,request,jsonify

app=Flask(__name__)


@app.route('/hello')

def hello():
    return "Server implement sucessfully"

if __name__ == "__main__":
    print("Testing MySQL connection...")
    app.run(port=5000)