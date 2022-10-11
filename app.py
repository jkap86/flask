from urllib import request
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    leagues = requests.get('https://api.sleeper.app/v1/user/424024949334740992/leagues/nfl/2022', timeout=3).json()
    return leagues