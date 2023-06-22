from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "HELLO WORLD!"


if __name__ == "__main__":
    app.debug = True
    app.run(host="192.168.1.13", port=1234)
