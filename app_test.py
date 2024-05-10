from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/hithere')
def hi_there_me():
    return "Hello to the New Slash"


@app.route('/add',methods=["POST"])
def add_numbers():
    dataDict = request.get_json()
    x = dataDict["x"]
    y = dataDict["y"]
    z = x + y
    retJson = {
        "z": z
    }
    return jsonify(retJson), 200

@app.route('/bye')
def hello_world_bye():
    st = {
        "abc" : "def",
        "qwe" : "fre" 
    } 
    return jsonify(st)


if __name__=="__main__":
    app.run(debug=True)

