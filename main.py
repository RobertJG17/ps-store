from flask import Flask, request, redirect
from flask_cors import CORS, cross_origin
import ast
import requests
import spotipy

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
spotty = spotipy.Spotify()


@app.route('/', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def index():
    return 'yeet'


@app.route('/callback', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def getCode():
    code = request.args.get('code')
    #code/token exchange
    data = {"grant_type":"authorization_code", "code": code, "redirect_uri":"http://127.0.0.1:5000/callback", "client_id":"474793580c424c75871ceae58caa9a06", "client_secret":"0110454a3aa24e4099e05ce2abfe745a"}
    response = requests.post("https://accounts.spotify.com/api/token", data=data)
    tokenStr = response.content
    dict_str = tokenStr.decode("UTF-8")
    token = ast.literal_eval(dict_str)
    acc_token = token['access_token']
    spotty.set_auth(auth=acc_token)

    song = spotty.currently_playing()['item']['id']
    print(song)
    #redirect user back to http://localhost:3000/ with token
    return redirect(f"http://localhost:3000/?token={token['access_token']}&refresh_token={token['refresh_token']}&expires_in={token['expires_in']}", code=302)


@app.route('/spider', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def spider():

    with open("radar.svg", "r") as img:
        svg = img.read()
    print('returned')
    return svg


@app.route('/current-song-analysis', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def analysis():
    with open("current_song.svg", "r") as img:
        svg = img.read()

    return svg


if __name__ == '__main__':
    app.run()
