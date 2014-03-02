from flask import Flask

from flask import render_template

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route("/")
def hello():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)