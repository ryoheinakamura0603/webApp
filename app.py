from flask import Flask
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/")
def hello_world():
    return "HELLO WORLD!"


if __name__ == "__main__":
    app.debug = True
    app.run(host="192.168.1.13", port=1234)
