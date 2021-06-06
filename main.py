from flask import Flask, request, redirect
from flask_cors import CORS, cross_origin
import requests
import ast
# from current_track import curr_song_svg


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return 'yeet'

@app.route('/callback', methods=['GET'])
def getCode():
    code = request.args.get('code')
    #code/token exchange
    data = {"grant_type":"authorization_code", "code": code, "redirect_uri":"http://127.0.0.1:5000/callback", "client_id":"474793580c424c75871ceae58caa9a06", "client_secret":"0110454a3aa24e4099e05ce2abfe745a"}
    response = requests.post("https://accounts.spotify.com/api/token", data=data)
    tokenStr = response.content
    dict_str = tokenStr.decode("UTF-8")
    token = ast.literal_eval(dict_str)
    print(token)
    #redirect user back to http://localhost:3000/ with token
    return redirect(f"http://localhost:3000/?token={token['access_token']}&refresh_token={token['refresh_token']}&expires_in={token['expires_in']}", code=302)


@app.route('/spider', methods=['GET'])
def spider():

    with open("radar.svg", "r") as img:
        svg = img.read()

    return svg


# @app.route('/current-song-analysis', methods=['GET'])
# def analysis():

#     with open(curr_song_svg, "r") as img:
#         svg = img.read()

#     return svg


if __name__ == '__main__':
    app.run()
