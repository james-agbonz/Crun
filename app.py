from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

app.config["DEBUG"]=os.environ.get("FLASK_DEBUG")


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

