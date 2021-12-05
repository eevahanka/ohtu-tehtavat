class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2= player2
        self.score1 = 0
        self.score2 = 0
        self.score_names = ["Love", "Fifteen",  "Thirty", "Forty"]

    def won_point(self, player):
        if player == "player1":
            self.score1 = self.score1 + 1
        else:
            self.score2 = self.score2 + 1

    def get_score(self):
        score = ""
        if self.score1 == self.score2:
            if self.score1 > 3:
                score = "Deuce"
            else:
                score = self.score_names[self.score1] + "-All"
        elif self.score1 >= 4 or self.score2 >= 4:
            winning_player = max((self.score1, "player1"), (self.score2, "player2"))
            losing_player = min((self.score1, "player1"), (self.score2, "player2"))
            if winning_player[0] - losing_player[0] > 1:
                score = "Win for " + winning_player[1]
            else:
                score = "Advantage " + winning_player[1]
        else:
            score = self.score_names[self.score1] +  "-" + self.score_names[self.score2]
            
        return score
