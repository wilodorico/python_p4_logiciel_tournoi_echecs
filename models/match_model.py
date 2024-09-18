from typing import List, Tuple


class Match:
    """
    A class representing a match between two players in a tournament.

    Attributes:
        players (Tuple[List[str, float], List[str, float]]): A tuple of two lists, where each list contains a player's
        name (str) and score (float). The first list represents the first player and the second list represents the
        second player.

    Methods:
        __repr__: Returns a string representation of the match, primarily for debugging.
        __str__: Returns a human-readable string representation of the match, showing player names and scores.
    """

    def __init__(self, player1_name: str, player1_score: float, player2_name: str, player2_score: float):
        self.players: Tuple[List[str, float], List[str, float]] = (
            [player1_name, player1_score],
            [player2_name, player2_score],
        )

    def __repr__(self):
        return f"Match({self.players})"

    def __str__(self):
        return f"{self.player1} - {self.score1} vs {self.player2} - {self.score2}"
