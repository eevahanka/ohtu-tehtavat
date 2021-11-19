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

    print("Oliot:")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()