import datetime
from typing import List

from tinydb import TinyDB

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

    def __str__(self) -> str:
        return f"{self.name} - {self.location}"

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "description": self.description,
            "date_start": self.date_start.strftime("%d-%m-%Y"),
            "date_end": self.date_end.strftime("%d-%m-%Y"),
            "number_of_round": self.number_of_round,
            "number_of_current_round": self.number_of_current_round,
            "rounds": self.rounds,
            "players": self.players,
        }


class TournamentManager:
    def __init__(self, db_path="data/tournaments/tournaments.json"):
        self.db = TinyDB(db_path, indent=4)
        self.tournaments_table = self.db.table("tournaments")

    def create_tournament(
        self,
        name: str,
        location: str,
        description: str,
        date_start: datetime,
        date_end: datetime,
    ):
        new_tournament = Tournament(
            name,
            location,
            description,
            date_start,
            date_end,
        )

        self.tournaments_table.insert(new_tournament.to_dict())

        print(f"Tournoi '{new_tournament.name}' enregistré avec succès !")

    def get_tournaments(self):
        tournaments = self.tournaments_table.all()
        return tournaments

    def get_last_tournament(self):
        tournament_data = self.tournaments_table.all()
        if not tournament_data:
            return None
        last_tournament = tournament_data[-1]
        return last_tournament
