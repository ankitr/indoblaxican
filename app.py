from flask import Flask

from flask import render_template

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/black')
def black():
    return render_template('black.html')

@app.route('/indo')
def indo():
    return render_template('indo.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)