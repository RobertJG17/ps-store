from flask import Flask, render_template, Markup

app = Flask(__name__)


@app.route('/')
def index():
    svg = open("radar.svg").read()

    return svg


if __name__ == '__main__':
    app.run()
