from typing import List, Tuple


class Match:
    def __init__(self, player1_name: str, player1_score: float, player2_name: str, player2_score: float):
        self.players: Tuple[List[str, float], List[str, float]] = (
            [player1_name, player1_score],
            [player2_name, player2_score],
        )

    def __repr__(self):
        return f"Match({self.players})"

    def __str__(self):
        return f"{self.player1} - {self.score1} vs {self.player2} - {self.score2}"
