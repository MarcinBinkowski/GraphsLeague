import requests

api_key = "RGAPI-660e2555-0e73-4b42-9169-1f9fb1ff0679"

urls = {
    "summoner_id": "https://{}.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}",
    "league": "https://{}.api.riotgames.com/lol/league/v3/positions/by-summoner/{}?api_key={}",
    "champions": "https://{}.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/{}?api_key={}",
    "mastery": "https://{}.api.riotgames.com/lol/champion-mastery/v3/scores/by-summoner/{}?api_key={}",
    "opgg": "http://{}.op.gg/summoner/userName={}",
    "icons": "http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/{}.png",
}

regions = {
    "ru": "ru",
    "kr": "kr",
    "br": "br1",
    "oc": "oc1",
    "jp": "jp1",
    "na": "na1",
    "eune": "eun1",
    "euw": "euw1",
    "tr": "tr1",
    "lan": "la1",
    "las": "la2",
    "pbe": "pbe1"
}

all_about_champions_json = requests.get("http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json").json()