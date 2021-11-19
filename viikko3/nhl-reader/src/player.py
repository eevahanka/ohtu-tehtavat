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

#{'name': 'Travis Zajac', 'nationality': 'CAN', 'assists': 12, 'goals': 8, 'penalties': 6, 'team': 'NYI', 'games': 46
#Sami Vatanen team CAR  goals 5 assists 18
    def __str__(self):
        return f"{self.name} team {self.team} goals {self.goals} assists {self.assists}"


