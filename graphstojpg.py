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

        self.all_champions_score = modifydata.get_all_champs_score(summoner)
        self.all_champions_score_modified = [self.all_champions_score - sum(self.best_three_scores)]

        self.donut_chart_data_scores = self.all_champions_score_modified + self.best_three_scores[::-1]
        self.donut_chart_data_names = ["Rest"] + self.best_three_names[::-1]
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


def champions_distribiution_graph(graph_data):
    names = graph_data.donut_chart_data_names
    scores = graph_data.donut_chart_data_scores

    plt.pie(scores, labels=names, startangle=90, colors=['#ce0404', 'green', 'blue', 'purple'])
    my_circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.savefig('{}_mastery_distribution.png'.format(gaph_data.summoner.summoner), transparent=False)

if __name__ == "__main__":
    gaph_data = GraphData(NewUser("binq661", "eune"))
    champions_distribiution_graph(gaph_data)

