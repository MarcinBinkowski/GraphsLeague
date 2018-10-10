import matplotlib.pyplot as plt
import requests
import constants
from loldata import NewUser
import drawgraphs
from raportgenerator import generate_raport
import modifydata

class Main:

    def __init__(self):
        self.nick = "binq661"             # input("Your summoner name: ")
        self.server = "eune"      # input("Server: ")
        self.summoner = NewUser(self.nick, self.server)
        self.league_solo_duo = modifydata.get_leagues(self.summoner)[0][0].lower()
        self.league_flex = modifydata.get_leagues(self.summoner)[1][0].lower()
        self.graph_data = drawgraphs.GraphData(self.summoner)
        self.best_three_names = self.graph_data.best_names[:3]
        self.champs_with_chest = self.graph_data.best_with_chests_names

        self.download_icon(self.summoner.profile_icon_id, self.best_three_names)
        self.champions_distribiution_graph()
        self.solo_win_ratio_graph()
        self.flex_win_ratio_graph()

        generate_raport(self.summoner.summoner, self.league_solo_duo,self.league_flex,
                        self.server, "90", self.champs_with_chest)
        print("Raport generated :D")
        print("Autor Marcin Binkowski, https://www.github.com/marcinbinkowski")

    def champions_distribiution_graph(self):
        names = self.graph_data.donut_chart_data_names
        scores = self.graph_data.donut_chart_data_scores

        plt.pie(scores, labels=names, startangle=90,
                colors=['#e6194B', '#f58231', '#ffe119', "#bfef45", "#3cb44b", "#aaffc3"],
                textprops={'fontsize': 14, "weight": "bold"})
        my_circle = plt.Circle((0, 0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        plt.title("Top champions", fontsize=30, weight="bold")
        plt.savefig('src/temporary/{}_mastery_distribution.png'.format(self.graph_data.summoner.summoner), transparent=True)
        plt.clf()

    def solo_win_ratio_graph(self):
        wins = self.graph_data.win_data[0][0]
        losses = self.graph_data.win_data[0][1]
        names = ["losses: {}".format(losses), "wins: {}".format(wins)]
        wins_lossses = [losses, wins]

        plt.pie(wins_lossses, labels=names, startangle=90, colors=['#D6464F', '#388FE2'],
                textprops={'fontsize': 14, "weight": "bold"})
        my_circle = plt.Circle((0, 0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        plt.title("solo/duo wins", fontsize=30, weight="bold")
        plt.text(0, 0, f"{self.graph_data.win_data[0][2]*100}%", fontsize=12, ha="center", va="center", size=24)
        plt.savefig('src/temporary/{}_solo_duo.png'.format(self.graph_data.summoner.summoner), transparent=True)
        plt.clf()

    def flex_win_ratio_graph(self):
        wins = self.graph_data.win_data[1][0]
        losses = self.graph_data.win_data[1][1]
        names = ["losses: {}".format(losses), "wins: {}".format(wins)]
        wins_lossses = [losses, wins]

        plt.pie(wins_lossses, labels=names, startangle=90, colors=['#D6464F', '#388FE2'],
                textprops={'fontsize': 14, "weight": "bold"})
        my_circle = plt.Circle((0, 0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        plt.title("flex wins", fontsize=30, weight="bold")
        plt.text(0, 0, f"{self.graph_data.win_data[1][2]*100}%", fontsize=12, ha="center", va="center", size=24)
        plt.savefig('src/temporary/{}_flex.png'.format(self.graph_data.summoner.summoner), transparent=True)
        plt.clf()

    def download_icon(self, icon_id, top_champs):
        icon = requests.get("http://ddragon.leagueoflegends.com/cdn/6.24.1/img/profileicon/{}.png".format(icon_id))
        if icon.status_code == 200:
            with open("src/temporary/icon.png", 'wb') as f:
                f.write(icon.content)
            f.close()
        else:
            print("Profile icon not in data base...")
            icon = requests.get("http://ddragon.leagueoflegends.com/cdn/6.24.1/img/profileicon/588.png".format(icon_id))
            if icon.status_code == 200:
                with open("src/temporary/icon.png", 'wb') as f:
                    f.write(icon.content)
                f.close()

        for i in range(3):
            icon = requests.get(constants.urls["icons"].format(top_champs[i]))
            if icon.status_code == 200:
                with open("src/temporary/top_champ{}.png".format(i + 1), 'wb') as f:
                    f.write(icon.content)
                f.close()


if __name__ == "__main__":
    main = Main()


"""
        #modifydata functions
        self.most_and_least_played_champions = modifydata.modify_masteries_data(self.summoner)
        self.all_champs_score = modifydata.get_all_champs_score(self.summoner)
        self.three_champs_for_chests = modifydata.top_three_champions_who_can_earn_chests(self.summoner)
        self.win_rate = modifydata.win_rate(self.summoner)
        self.leagues = modifydata.get_leagues(self.summoner)


"""