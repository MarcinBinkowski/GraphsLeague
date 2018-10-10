#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import modifydata
import requests
import os
from loldata import NewUser
from raportgenerator import generate_raport
import constants
import dataforgraphs


class Main:
    """
    Class used to coordinate different functions from different files
    """
    def __init__(self):
        self.make_instance_of_summoner()

        self.lvl = self.summoner.lvl
        self.league_solo_duo = modifydata.get_leagues(self.summoner)[0][0].lower()
        self.league_flex = modifydata.get_leagues(self.summoner)[1][0].lower()
        self.graph_data = dataforgraphs.GraphData(self.summoner)
        self.best_three_names = self.graph_data.best_names[:3]
        self.champs_with_chest = self.graph_data.best_with_chests_names

        self.download_icons(self.summoner.profile_icon_id, self.best_three_names)
        self.champions_distribiution_graph()
        self.solo_win_ratio_graph()
        self.flex_win_ratio_graph()

        # generating raport
        generate_raport(self.summoner.summoner, self.league_solo_duo,self.league_flex,
                        self.server, self.lvl, self.champs_with_chest)

        self.remove_folder()

        print("\n**************************")
        print("Raport generated :D")
        print("Autor Marcin Binkowski, https://www.github.com/marcinbinkowski")
        print("**************************")

    def make_instance_of_summoner(self):
        self.nick = input("Your summoner name: ")
        self.server = input("Server: ")
        try:
            self.summoner = NewUser(self.nick, self.server)
        except:
            print("Wrong data... Please try again\n")
            self.make_instance_of_summoner()


    def champions_distribiution_graph(self):
        """
        Method returns donught graph presenting how many games u played with each of summoner 5 best champions
        comparing to all champions
        """
        names = self.graph_data.donut_chart_data_names
        scores = self.graph_data.donut_chart_data_scores

        plt.pie(scores, labels=names, startangle=90,
                colors=['#e6194B', '#f58231', '#ffe119', "#bfef45", "#3cb44b", "#aaffc3"],
                textprops={'fontsize': 14, "weight": "bold"})
        my_circle = plt.Circle((0, 0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        plt.title("Top champions", fontsize=30, weight="bold")
        plt.savefig('../src/temporary/{}_mastery_distribution.png'.format(self.graph_data.summoner.summoner),
                    transparent=True)
        plt.clf()

    def solo_win_ratio_graph(self):
        """
        Method returns graph comparing summoner wins to losses on solo queue
        """
        if self.league_solo_duo == "p":
            self.blank_graph()
            return None
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
        plt.savefig('../src/temporary/{}_solo_duo.png'.format(self.graph_data.summoner.summoner), transparent=True)
        plt.clf()

    def flex_win_ratio_graph(self):
        """
        Method returns graph comparing summoner wins to losses on flex queue
        """
        if self.league_flex == "p":
            self.blank_graph()
            return None
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
        plt.savefig('../src/temporary/{}_flex.png'.format(self.graph_data.summoner.summoner), transparent=True)
        plt.clf()

    def blank_graph(self):
        wins = [1, 0]

        plt.pie(wins, labels=["", ""], startangle=90, colors=['grey'],
                textprops={'fontsize': 14, "weight": "bold"})
        my_circle = plt.Circle((0, 0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        plt.title("You need to play more games", fontsize=18, weight="bold")
        plt.savefig('../src/temporary/blank_graph.png', transparent=True)
        plt.clf()

    def download_icons(self, icon_id, top_champs):
        """
        Method used to download profile icon and icons for top 3 champs
        """
        icon = requests.get("http://ddragon.leagueoflegends.com/cdn/6.24.1/img/profileicon/{}.png".format(icon_id))
        if icon.status_code == 200:
            with open("../src/temporary/icon.png", 'wb') as f:
                f.write(icon.content)
            f.close()
        else:
            print("Profile icon not in data base...") # in case sth goes wrong we get poro icon
            icon = requests.get("http://ddragon.leagueoflegends.com/cdn/6.24.1/img/profileicon/588.png")
            if icon.status_code == 200:
                with open("../src/temporary/icon.png", 'wb') as f:
                    f.write(icon.content)
                f.close()

        for i in range(3):
            icon = requests.get(constants.urls["icons"].format(top_champs[i]))
            if icon.status_code == 200:
                with open("../src/temporary/top_champ{}.png".format(i + 1), 'wb') as f:
                    f.write(icon.content)
                f.close()
            else:
                print("Problem downloading champion icon...")


    def remove_folder(self):
        """
        Method removing icons and graphs from src/temporary directorry
        """
        folder = '../src/temporary'
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    main = Main()
