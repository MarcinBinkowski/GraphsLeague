from loldata import NewUser

def modify_masteries_data(summoner):
    all_masteries = summoner.all_masteries
    masteries_list = []

    for i in range(len(summoner.champions_info)):
        champion_id = summoner.champions_info[i]["championId"]
        champion_points = summoner.champions_info[i]["championPoints"]
        masteries_list.append((champion_id, champion_points))

    masteries_list.sort(key=lambda item: (item[1], item[0]), reverse=True)
    three_most_played_champions = masteries_list[:3]
    least_played_champion = masteries_list[-1:]
    return all_masteries, three_most_played_champions, least_played_champion,

def top_three_champions_who_can_earn_chests(summoner):
    chests = []
    for i in range(len(summoner.champions_info)):
        champion_id = summoner.champions_info[i]["championId"]
        champion_points = summoner.champions_info[i]["championPoints"]
        chest_available = summoner.champions_info[i]["chestGranted"]
        chests.append((champion_id, champion_points, chest_available))

    chests.sort(key=lambda item: (item[1], item[0], item[2]), reverse=True)
    chests = [x for x in chests if x[2] != True][:3]
    return chests

def win_rate(summoner):
    number_of_wins_solo_duo = summoner.league_info[1]["wins"]
    number_of_loses_solo_duo = summoner.league_info[1]["losses"]
    number_of_wins_flex = summoner.league_info[0]["wins"]
    number_of_losses_flex = summoner.league_info[0]["losses"]
    win_rate_solo_duo =  number_of_wins_solo_duo / (number_of_wins_solo_duo + number_of_loses_solo_duo)
    win_rate_flex =  number_of_wins_flex / (number_of_wins_flex + number_of_losses_flex)
    return ((number_of_wins_solo_duo, number_of_loses_solo_duo, round(win_rate_solo_duo, 2)),
    (number_of_wins_flex, number_of_losses_flex, round(win_rate_flex, 2)))



if __name__ == "__main__":
    my_summoner = NewUser("binq661", "eune")
    modify_masteries_data(my_summoner)
    top_three_champions_who_can_earn_chests(my_summoner)
    win_rate(my_summoner)