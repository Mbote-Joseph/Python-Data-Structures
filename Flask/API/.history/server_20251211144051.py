from flask import Flask, jsonify, request

app = Flask("__name__")

incomes = [
    {'description': 'salary', 'amount': 5000}
]

@app.route('/')
def server():
    return "Income Server API"

@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_incomes():
    incomes.append(request.get_json())
    return request.get_json()

@app.route('/incomes/<int:id>', methods=['GET','POST'])
def update_income(id):
    income_to_update = filter(lambda x : x.id == id)
    incomes.append(request.get_json(), income_to_update)
    return request.get_json()

if __name__ == "__main__":
    app.run(debug=True)