from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

stores = []

@app.route('/')
def home():
    return 'Hello World From Me!'


@app.route('/store', methods=['POST'])
def create_store():
    global stores
    data = request.get_json()
    stores.append({'name': data['name'], 'items': []})
    return jsonify({'message': 'created store', 'name': data['name']})

@app.route('/store/<string:name>')
def get_store(name):
    return jsonify({'name': name})

@app.route('/stores')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    data = request.get_json()
    stores.append({'name': name, 'items':{'name': data['name'], 'price':data['price']}})
    return jsonify({'message': 'item added to the store'})

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass



if __name__ == '__main__':
    app.run(port=5000, debug=True)
