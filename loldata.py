import requests
import constants
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


class NewUser:

    def __init__(self, summoner, region, api_key=constants.api_key):
        self.api_key = api_key
        self.summoner = summoner
        self.region = constants.regions[region]
        self.region_op_gg = region
        self.summoner_info = self.get_summoner_info()
        #print(self.summoner_info)
        self.ID = self.summoner_info["id"]
        print(self.ID)
        self.league_info = self.get_summoner_league_info()
        #print(self.league_info)
        self.champions_info = self.get_summoner_champions_info()
        #print(self.champions_info)
        self.all_masteries = self.get_masteries_info()
        self.driver = None
        self.options = None
        self.mmr = None

    def get_summoner_info(self):
        """ Get summoner info json using his nickname"""
        return requests.get(constants.urls["summoner_id"].format(
                            self.region, self.summoner, self.api_key)).json()

    def get_summoner_league_info(self):
        """ Get info about summoners league json"""
        return requests.get(constants.urls["league"].format(
                            self.region, self.ID, self.api_key)).json()

    def get_masteries_info(self):
        """ Get info about all champions masteries json"""
        return requests.get(constants.urls["mastery"].format(
                            self.region, self.ID, self.api_key)).json()

    def get_summoner_champions_info(self):
        """ Get info about all champions json"""
        return requests.get(constants.urls["champions"].format(
                            self.region, self.ID, self.api_key)).json()

    def get_mmr_from_opgg(self):
        """ Get mmr from op.gg using selenium"""
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.get(constants.urls["opgg"].format(self.region_op_gg, self.summoner))
        sleep(2)
        try:
            elem = self.driver.find_element_by_xpath("//button[@class='banner_save--3Xnwp']")
        except:
            sleep(2)
            elem = self.driver.find_element_by_xpath("//button[@class='banner_save--3Xnwp']")
        self.driver.execute_script("arguments[0].click();", elem)
        sleep(2)

        try:
            elem = self.driver.find_element_by_xpath("//button[@class='Button SemiRound LightGreen']")
        except:
            sleep(2)
            elem = self.driver.find_element_by_xpath("//button[@class='Button SemiRound LightGreen']")
        self.driver.execute_script("arguments[0].click();", elem)

        try:
            self.mmr = self.driver.find_element_by_xpath("//td[@class='MMR']").text
        except:
            sleep(2)
            self.mmr = self.driver.find_element_by_xpath("//td[@class='MMR']").text
        self.driver.close()
        return self.mmr

if __name__ == "__main__":
    user = NewUser("binq661", "eune")
    #user.get_mmr_from_opgg()