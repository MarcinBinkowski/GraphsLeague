import matplotlib.pyplot as plt
from loldata import NewUser
import constants
import modifydata


class GraphData:
    """
    This class is used for generating objects which keep all data needed for generating charts for summoner
    """
    def __init__(self, summoner):
        self.summoner = summoner
        self.masteries = modifydata.modify_masteries_data(self.summoner)
        self.best_three_scores = [x[1] for x in self.masteries[0]]
        self.best_three_ids = [x[0] for x in self.masteries[0]]
        self.best_three_names = self.get_champions_names(self.best_three_ids)

        self.worst_score = [self.masteries[1][0][1]]
        self.worst_id = [self.masteries[1][0][0]]
        self.worst_name = [self.get_champion_name(str(self.worst_id[0]))]

        self.all_champions_score = modifydata.get_all_champs_score(summoner)
        self.all_champions_score_modified = [self.all_champions_score - sum(self.best_three_scores) - self.worst_score[0]]

        self.donut_chart_data_scores = self.best_three_scores + self.all_champions_score_modified + self.worst_score
        self.donut_chart_data_names = self.best_three_names + ["Rest"] + self.worst_name
        print(self.donut_chart_data_scores)
        print(self.donut_chart_data_names)

    def get_champion_name(self, id):
        """
        This method returnes name of champion with given id
        """
        for name in constants.all_about_champions_json["data"]:
            if constants.all_about_champions_json["data"][name]["key"] == id:
                return name

    def get_champions_names(self, ids_list):
        """
        This method returnes list containing names of champions with given ids from list
        """
        temp = []
        for i in ids_list:
            temp.append(self.get_champion_name(str(i)))
        return temp






if __name__ == "__main__":
    gaph_data = GraphData(NewUser("binq661", "eune"))
    names = gaph_data.donut_chart_data_names
    scores = gaph_data.donut_chart_data_scores

    plt.pie(scores)
    my_circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(my_circle)

    plt.show()