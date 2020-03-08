from flask import Flask
app = Flask(__name__)

@app.route("/test")
def hello():
    print("Outp")
    return "Hello World! Amit new123!!"