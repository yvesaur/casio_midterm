from flask import Flask
from flask import request
import math

app = Flask(__name__)

@app.route("/result", methods= ["POST", "GET"])

def result():
    output = request.get_json()

    if len(output.keys()) < 2:
        return {"Status": "Input error"}

    num1 = int(output["num1"])
    num2 = int(output["num2"])

    cals = {}

    cals['sine'] = math.sin(num1)
    cals['cosine'] = math.sin(num2)
    cals['tangent'] = math.tan(num1/num2)

    return (cals)

if __name__ == '__main__':
    app.run(debug=True, port=2000)   