from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def checkPostData(postData, functionname):
    if (functionname in ["add", "subtract", "multiply"]):
        if "x" not in postData:
            return "X is Missing",301
        elif "y" not in postData:
            return "Y is Missing",302
        else:
            return "Numbers " + functionname+"ed" + " Successfully! ",200
    else:
        if "x" not in postData:
            return "X is Missing",301
        if "y" not in postData:
            return "Y is Missing",302
        elif postData["y"] == 0:
            return "Y is Zero, Hence cannot be divided by zero!", 303
        else:
            return "Numbers divided Successfully!",200


class Add(Resource):
    def post(self):
        postData = request.get_json()

        message, statuscode = checkPostData(postData,"add")
        if (statuscode!=200):
            retJson = {
                "Message" : message,
                "Status Code" : statuscode
            }
            return jsonify(retJson)
        x = postData["x"]
        y = postData["y"]
        x, y = int(x), int(y)
        ret = x + y
        retMap = {
            "Message" : message,
            "Value" : ret,
            "Status Code" : statuscode
        }
        return jsonify(retMap)


class Subtract(Resource):
    def post(self):
        postData = request.get_json()

        message, statuscode = checkPostData(postData,"subtract")
        if (statuscode!=200):
            retJson = {
                "Message" : message,
                "Status Code" : statuscode
            }
            return jsonify(retJson)
        x = postData["x"]
        y = postData["y"]
        x, y = int(x), int(y)
        ret = x - y
        retMap = {
            "Message" : message,
            "Value" : ret,
            "Status Code" : statuscode
        }
        return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        postData = request.get_json()

        message, statuscode = checkPostData(postData,"multiply")
        if (statuscode!=200):
            retJson = {
                "Message" : message,
                "Status Code" : statuscode
            }
            return jsonify(retJson)
        x = postData["x"]
        y = postData["y"]
        x, y = int(x), int(y)
        ret = x * y
        retMap = {
            "Message" : message,
            "Value" : ret,
            "Status Code" : statuscode
        }
        return jsonify(retMap)

class Divide(Resource):
    def post(self):
        postData = request.get_json()

        message, statuscode = checkPostData(postData,"divide")
        if (statuscode!=200):
            retJson = {
                "Message" : message,
                "Status Code" : statuscode
            }
            return jsonify(retJson)
        x = postData["x"]
        y = postData["y"]
        x, y = int(x), int(y)
        ret = x / y
        retMap = {
            "Message" : message,
            "Value" : ret,
            "Status Code" : statuscode
        }
        return jsonify(retMap)


api.add_resource(Add,"/add")
api.add_resource(Subtract,"/subtract")
api.add_resource(Multiply,"/multiply")
api.add_resource(Divide,"/divide")


@app.route('/')
def hello_world():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)