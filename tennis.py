# -*- coding: utf-8 -*-

class TennisGame1:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1

        elif playerName == self.player2Name:
            self.p2points += 1

    def score(self):
        result = ""
        tempScore = 0
        if self.p1points == self.p2points:
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")
        elif self.p1points >= 4 or self.p2points >= 4:
            minusResult = self.p1points - self.p2points
            if minusResult == 1:
                result = "Advantage " + self.player1Name
            elif minusResult == -1:
                result = "Advantage " + self.player2Name
            elif minusResult >= 2:
                result = "Win for " + self.player1Name
            else:
                result = "Win for " + self.player2Name
        else:
            for i in range(1, 3):
                if i == 1:
                    tempScore = self.p1points
                else:
                    result += "-"
                    tempScore = self.p2points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[tempScore]
        return result


class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        elif playerName == self.player2Name:
            self.p2points += 1

    def score(self):
        result = ""
        if self.p1points == self.p2points and self.p1points < 3:
            if self.p1points == 0:
                result = "Love"
            elif self.p1points == 1:
                result = "Fifteen"
            elif self.p1points == 2:
                result = "Thirty"
            result += "-All"
        if self.p1points == self.p2points and self.p1points > 2:
            result = "Deuce"

        P1res = ""
        P2res = ""
        if self.p1points > 0 and self.p2points == 0:
            if self.p1points == 1:
                P1res = "Fifteen"
            elif self.p1points == 2:
                P1res = "Thirty"
            elif self.p1points == 3:
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if self.p2points > 0 and self.p1points == 0:
            if self.p2points == 1:
                P2res = "Fifteen"
            elif self.p2points == 2:
                P2res = "Thirty"
            elif self.p2points == 3:
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res

        if self.p1points > self.p2points and self.p1points < 4:
            if self.p1points == 2:
                P1res = "Thirty"
            elif self.p1points == 3:
                P1res = "Forty"
            if self.p2points == 1:
                P2res = "Fifteen"
            elif self.p2points == 2:
                P2res = "Thirty"
            result = P1res + "-" + P2res
        if self.p2points > self.p1points and self.p2points < 4:
            if self.p2points == 2:
                P2res = "Thirty"
            elif self.p2points == 3:
                P2res = "Forty"
            if self.p1points == 1:
                P1res = "Fifteen"
            elif self.p1points == 2:
                P1res = "Thirty"
            result = P1res + "-" + P2res

        if self.p1points > self.p2points and self.p2points >= 3:
            result = "Advantage " + self.player1Name

        if self.p2points > self.p1points and self.p1points >= 3:
            result = "Advantage " + self.player2Name

        if (
            self.p1points >= 4
            and self.p2points >= 0
            and (self.p1points - self.p2points) >= 2
        ):
            result = "Win for " + self.player1Name
        if (
            self.p2points >= 4
            and self.p1points >= 0
            and (self.p2points - self.p1points) >= 2
        ):
            result = "Win for " + self.player2Name
        return result


class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.p1_name = player1_name
        self.p2_name = player2_name
        self.p1__ = 0
        self.p2__ = 0

    def won_point(self, name):
        if name == self.p1_name:
            self.p1__ += 1
        elif name == self.p1_name:
            self.p2__ += 1

    def score(self):
        if (self.p1__ < 4 and self.p2__ < 4) and (self.p1__ + self.p2__ < 6):
            type_of_point = ["Love", "Fifteen", "Thirty", "Forty"]
            score = type_of_point[self.p1__]
            return score + "-All" if (self.p1__ == self.p2__) else score + "-" + type_of_point[self.p2__]
        else:
            if self.p1__ == self.p2__:
                return "Deuce"
            score = self.p1_name if self.p1__ > self.p2__ else self.p2_name
            return (
                "Advantage " + score
                if ((self.p1__ - self.p2__) * (self.p1__ - self.p2__) == 1)
                else "Win for " + score
            )
