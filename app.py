from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to the future home of the Indoblaxican."

if __name__ == "__main__":
    app.run(port=80)