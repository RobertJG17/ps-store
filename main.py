from flask import Flask, render_template, Markup
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    svg = open("radar.svg").read()

    return svg


if __name__ == '__main__':
    app.run()
