from flask import Flask 

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world"


@app.route("/support")
def support():
    return "<hl style = 'color: red'>Support Team email is a support@example.com<hl>"

@app.route("/calculate/<int:x>/<int:y>")
def calculate(x,y):
    return f'<html><body><h1>Addition<h1>Sum of {x} and {y} is {x + y}<body><html>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 30000, debug = False)