from typing import Tuple


class Match:
    def __init__(self, player1: str, score1: float, player2: str, score2: float):
        self.player1 = player1
        self.score1 = score1
        self.player2 = player2
        self.score2 = score2

    def to_tuple(self) -> Tuple[Tuple[str, float], Tuple[str, float]]:
        return (self.player1, self.score1), (self.player2, self.score2)

    def to_dict(self):
        return {"player1": self.player1, "score1": self.score1, "player2": self.player2, "score2": self.score2}

    def __str__(self):
        return f"{self.player1} - {self.score1} vs {self.player2} - {self.score2}"
