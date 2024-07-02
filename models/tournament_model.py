import datetime
from typing import List

from models.player_model import Player
from models.round_model import Round


class Tournament:
    def __init__(
        self,
        name: str,
        location: str,
        description: str,
        date_start: datetime,
        date_end: datetime,
    ):
        self.name = name
        self.location = location
        self.description = description
        self.date_start = date_start
        self.date_end = date_end

        self.number_of_round: int = 4
        self.number_of_current_round: int = 1
        self.rounds: List[Round] = []
        self.players: List[Player] = []
