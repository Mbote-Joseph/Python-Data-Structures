from flask import Flask # type: ignore

app = Flask(__name__)

books = ["Think big", "Gifted Hands"]

@app.route("/b")
def index():
    return "Hello World"

@app.route("/books")
def books():
    return books