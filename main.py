from flask import Flask
from flask_cors import CORS, cross_origin
from current_track import curr_song_svg


app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def index():
    return 'yeet'


@app.route('/spider', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def spider():

    with open("radar.svg", "r") as img:
        svg = img.read()

    return svg


@app.route('/current-song-analysis', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def analysis():

    with open(curr_song_svg, "r") as img:
        svg = img.read()

    return svg


if __name__ == '__main__':
    app.run()
