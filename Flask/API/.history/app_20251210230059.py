from flask import Flask

app = Flask(__name__)

books = []

@app.route('/', methods= ['GET'])
def get_books():
    return books

@app.route('/', methods = ['GET','POST'])
def add_books(book):
    return book.push(book)

if __name__ == "__main__":
    app.run(debug=True)