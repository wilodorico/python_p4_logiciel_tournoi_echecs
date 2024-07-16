from models.match import Match
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

    def add_player(self, player: Player):
        self.players.append(player)
        print(f"Joueur {player.firstname} {player.lastname} ajouté avec succès !")

    # Pour le contoller de tournoi
    # Tournament.create_first_round()
    # Le round 1 est créé dans self.rounds

    # get_last_round()

    def create_first_round(self):
        self.rounds.append(Round(f"Round {self.number_of_current_round}"))
        # create first round()
        # create random match from list of players (Tournament.players)
        # boucle de création de matchs (Match)
        used_players: List[Player] = []
        while len(used_players) < len(self.players):
            match = Match(round=0)

            for player in self.players:
                if player not in used_players:
                    match.add_player(player)
                    used_players.append(player)
                    break

        # return round

    def create_round(self):
        pass
        # get last round
        # on applique les regles de création de matchs
        # (player triés par score + verifier que le joueur ne rencontre pas le même joueur)


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
        tournamement = Tournament(name, location, description, date_start, date_end)

        return tournamement


tournament_manager = TournamentManager()
new_tournament = tournament_manager.create_tournament(
    name="Tournoi",
    location="Nerac",
    description="le trr",
    date_start="12-07-2024",
    date_end="14-07-2024",
)

print(new_tournament)
