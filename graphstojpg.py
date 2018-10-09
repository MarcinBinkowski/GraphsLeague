import matplotlib.pyplot as plt
import requests
from loldata import NewUser
import constants
import modifydata


class GraphData:
    def __init__(self, summoner):
        self.summoner = summoner
        self.masteries = modifydata.modify_masteries_data(self.summoner)
        self.best_three_scores = [x[1] for x in self.masteries[0]]
        self.best_three_ids = [x[0] for x in self.masteries[0]]
        self.best_three_names = self.get_champions_names(self.best_three_ids)

        self.worst_score = [self.masteries[1][0][1]]
        self.worst_id = [self.masteries[1][0][0]]
        self.worst_name = [self.get_champion_name(str(self.worst_id[0]))]

    def get_champion_name(self, id):
        for name in constants.all_about_champions_json["data"]:
            if constants.all_about_champions_json["data"][name]["key"] == id:
                return name

    def get_champions_names(self, ids_list):
        temp = []
        for i in ids_list:
            temp.append(self.get_champion_name(str(i)))
        return temp






if __name__ == "__main__":
    gaph_data = GraphData(NewUser("binq661", "eune"))

