import requests
import constants


class NewUser:

    def __init__(self, api_key, summoner, region):
        self.api_key = api_key
        self.summoner = summoner
        self.region = constants.regions[region]
        self.summoner_info = self.get_summoner_info()
        self.ID = str(self.summoner_info["id"])
        self.lvl = self.summoner_info["summonerLevel"]
        self.summoner_league_info = self.get_summoner_league_info()
        self.summoner_division_solo = "{} {}".format(self.summoner_league_info[0]["tier"],
                                                     self.summoner_league_info[0]["rank"])
        print(self.summoner_division)

    def get_summoner_info(self):
        return requests.get(constants.urls["summoner_id"].format(
                            self.region, self.summoner, self.api_key)).json()

    def get_summoner_league_info(self):
        return requests.get(constants.urls["league"].format(
                            self.region, self.summoner, self.api_key)).json()

if __name__ == "__main__":
    user = NewUser("RGAPI-6cf3057e-f4fb-4eb1-9fc6-af707a0a044a", "binq661", "eune")


