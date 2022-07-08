from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def home():
    return 'Hello World From Me!'


@app.route('/store', methods=['POST'])
def create_store():
    data = request.get_json()
    print(data)
    return jsonify({'name': data['name']})

@app.route('/store/<string:name>')
def get_store(name):
    return jsonify({'name': name})



if __name__ == '__main__':
    app.run(port=5000, debug=True)
