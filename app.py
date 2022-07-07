from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def home():
    return 'Hello World From Me!'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
