from flask import Flask, request, jsonify
import calculator

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    result = calculator.add(data['a'], data['b'])
    return jsonify({"result": result})

# Similar endpoints for subtract, multiply, and divide.

if __name__ == "__main__":
    app.run(debug=True)