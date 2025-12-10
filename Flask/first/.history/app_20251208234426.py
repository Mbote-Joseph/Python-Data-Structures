from flask import Flask # type: ignore

app = Flask(__name__)

books = ["Think big", "Gifted Hands"]

@app.route("/")
def index():
    return '<h1>Hello World</h1>'


