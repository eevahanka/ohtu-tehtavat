from player import Player
import requests


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        if player_dict["nationality"] == "FIN":
            player = Player(player_dict)
            players.append(player)

    #print by stats
    sorted_players = sorted(players, key=lambda x: x.points, reverse=True)
    for player in sorted_players:
        print(f"{player.name} {player.team} {player.points}")

    #print("Oliot:")


    #for player in players:
    #    print(player)


if __name__ == "__main__":
    main()
