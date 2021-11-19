import requests


class Player:
    def __init__(self, dict):

        self.name = dict["name"]
        self.nationality = dict["nationality"]
        self.assists = dict["assists"]
        self.goals = dict["goals"]
        self.penalties = dict["penalties"]
        self.team = dict["team"]
        self.games = dict["games"]
        self.points = self.assists + self.goals

    def __str__(self):
        return f"{self.name} {self.team} {self.points}"


class PlayerReader:
    def __init__(self, url) -> None:
        response = requests.get(url).json()
        self.players = []
        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)


class PlayerStats:
    def __init__(self, reader) -> None:
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality):
        nationality_players = []
        for player in self.players:
            if player.nationality == nationality:
                nationality_players.append(player)
            sorted_players= sorted(nationality_players, key=lambda x: x.points, reverse=True)
        return sorted_players


