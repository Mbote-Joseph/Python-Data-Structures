from flask import Flask, render_template

app = Flask(__name__)

books = ["Think big", "Gifted Hands"]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def books(books):
    return f"the books are : {books[0]}"