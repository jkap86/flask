from asyncio import futures
from urllib import request
from flask import Flask
import requests
import concurrent.futures

app = Flask(__name__)


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


@app.route('/')
def index():
    leagues = requests.get(
        'https://api.sleeper.app/v1/user/424024949334740992/leagues/nfl/2022', timeout=3).json()

    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        results = executor.map(getLeagueInfo, leagues)

    return list(results)
