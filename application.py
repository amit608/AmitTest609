from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("Outp")
    return "Hello World! Amit new123!!"