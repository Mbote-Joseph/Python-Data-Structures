from flask import Flask

app = Flask(__name__)

books = []

@app.route('/', methods= ['GET'])
def get_books():
    return books