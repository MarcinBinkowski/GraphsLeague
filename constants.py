api_key = "RGAPI-6cf3057e-f4fb-4eb1-9fc6-af707a0a044a"

urls = {
    "summoner_id": "https://{}.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}",
    "league": "https://{}.api.riotgames.com/lol/league/v3/positions/by-summoner/{}?api_key={}",
    "champions": "https://{}.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/{}?api_key={}",
    "mastery": "https://{}.api.riotgames.com/lol/champion-mastery/v3/scores/by-summoner/{}?api_key={}",
    "opgg": "http://{}.op.gg/summoner/userName={}",
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