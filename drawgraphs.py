import matplotlib.pyplot as plt
from loldata import NewUser
import constants
import modifydata
import requests


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

        self.all_champions_score = modifydata.get_all_champs_score(summoner)
        self.all_champions_score_modified = [self.all_champions_score - sum(self.best_three_scores)]

        self.donut_chart_data_scores = self.all_champions_score_modified + self.best_three_scores[::-1]
        self.donut_chart_data_names = ["Rest"] + self.best_three_names[::-1]


        self.win_data = modifydata.win_rate(summoner)

    def get_champion_name(self, id_number):
        """
        This method returnes name of champion with given id
        """
        for name in constants.all_about_champions_json["data"]:
            if constants.all_about_champions_json["data"][name]["key"] == id_number:
                return name

    def get_champions_names(self, ids_list):
        """
        This method returnes list containing names of champions with given ids from list
        """
        temp = []
        for i in ids_list:
            temp.append(self.get_champion_name(str(i)))
        return temp


def champions_distribiution_graph(graph_data):
    names = graph_data.donut_chart_data_names
    scores = graph_data.donut_chart_data_scores

    plt.pie(scores, labels=names, startangle=90, colors=['#e6194B', '#f58231', '#ffe119', "#bfef45", "#3cb44b", "#aaffc3"],
            textprops={'fontsize': 14, "weight": "bold"})
    my_circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.title("Top champions", fontsize=30, weight="bold")
    plt.savefig('src/temporary/{}_mastery_distribution.png'.format(graph_data.summoner.summoner), transparent=True)
    plt.clf()


def solo_win_ratio_graph(graph_data):
    wins = graph_data.win_data[0][0]
    losses = graph_data.win_data[0][1]
    names = ["losses: {}".format(losses), "wins: {}".format(wins)]
    wins_lossses = [losses, wins]

    plt.pie(wins_lossses, labels=names, startangle=90, colors=['#D6464F', '#388FE2'],
            textprops={'fontsize': 14, "weight": "bold"})
    my_circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.title("solo/duo wins", fontsize=30, weight="bold")
    plt.text(0, 0, f"{graph_data.win_data[0][2]*100}%", fontsize=12, ha="center", va="center", size=24)
    plt.savefig('src/temporary/{}_solo_duo.png'.format(graph_data.summoner.summoner), transparent=True)
    plt.clf()


def flex_win_ratio_graph(graph_data):
    wins = graph_data.win_data[1][0]
    losses = graph_data.win_data[1][1]
    names = ["losses: {}".format(losses), "wins: {}".format(wins)]
    wins_lossses = [losses, wins]

    plt.pie(wins_lossses, labels=names, startangle=90, colors=['#D6464F', '#388FE2'],
            textprops={'fontsize': 14, "weight": "bold"})
    my_circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.title("flex wins", fontsize=30, weight="bold")
    plt.text(0, 0, f"{graph_data.win_data[1][2]*100}%", fontsize=12, ha="center", va="center", size=24)
    plt.savefig('src/temporary/{}_flex.png'.format(graph_data.summoner.summoner), transparent=True)
    plt.clf()



if __name__ == "__main__":
    graph_data = GraphData(NewUser("binq661", "eune"))
    champions_distribiution_graph(graph_data)
    solo_win_ratio_graph(graph_data)
    flex_win_ratio_graph(graph_data)
