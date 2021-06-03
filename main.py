from flask import Flask, request
from flask_cors import CORS, cross_origin
import requests
import ast
# from current_track import curr_song_svg


app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


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
    print(token['access_token'])
    #redirect user back to http://localhost:3000/ with token
    return 'yeet code'


@app.route('/spider', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def spider():

    with open("radar.svg", "r") as img:
        svg = img.read()

    return svg


# @app.route('/current-song-analysis', methods=['GET'])
# @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
# def analysis():

#     with open(curr_song_svg, "r") as img:
#         svg = img.read()

#     return svg


if __name__ == '__main__':
    app.run()
