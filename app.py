from urllib import request
from flask import Flask
import requests
import concurrent.futures

app = Flask(__name__)


@app.route('/')
def index():
    leagues = requests.get(
        'https://api.sleeper.app/v1/user/424024949334740992/leagues/nfl/2022', timeout=3).json()

    def getLeagueInfo(league):
        users = requests.get(
            'https://api.sleeper.app/v1/league/' + str(league['league_id']) + '/users', timeout=3).json()

        rosters = requests.get(
            'https://api.sleeper.app/v1/league/' + str(league['league_id']) + '/rosters').json()

        league_detail = {
            'users': users,
            'rosters': rosters
        }

        return league_detail

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        leagues_detailed = list(executor.map(getLeagueInfo, leagues))

    return leagues_detailed
