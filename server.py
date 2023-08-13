from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    content = "Hello world!"
    return Response(content, status=200)

@app.route("/calculator/add", methods=['POST'])
def add():
    nums = request.get_json()
    num1 = nums["first"]
    num2 = nums["second"]
    sum = int(num1) + int(num2)
    content = {"result": sum}
    return jsonify(content), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    nums = request.get_json()
    num1 = nums["first"]
    num2 = nums["second"]
    sub = int(num1) - int(num2)
    content = {"result": sub}
    return jsonify(content), 200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
