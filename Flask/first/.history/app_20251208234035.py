from flask import Flask # type: ignore

app = Flask(__name__)

books = ["Think big", "Gifted Hands"]

@app.route("/")
def index():
    return "Hello World"

@app.route("/books", method="GET")
def books():
    return books