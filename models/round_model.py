import random
from datetime import datetime
from enum import Enum
from typing import List
from tinydb import TinyDB

from models.player_model import Player
from models.match_model import Match


class RoundStatus(Enum):
    CREATED = "Créé"
    STARTED = "En cours"
    FINISHED = "Terminé"


class Round:
    def __init__(self, name: str):
        self.name = name
        self.matches: list = []
        self.start_at: datetime = None
        self.end_at: datetime = None
        self.status: RoundStatus = RoundStatus.CREATED

    def __str__(self) -> str:
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "matches": self.matches,
            "start_at": self.start_at.strftime("%d-%m-%Y %H:%M:%S") if self.start_at else None,
            "end_at": self.end_at.strftime("%d-%m-%Y %H:%M:%S") if self.end_at else None,
            "status": self.status.value,
        }

    def start(self):
        self.start_at = datetime.now()

    def end(self):
        self.end_at = datetime.now()

    def is_running(self):
        return self.start_at

    def add_match(self, match: Match):
        self.matches.append(match.players)


class RoundManager:
    def __init__(self, db_path="data/tournaments/tournaments.json"):
        self.db = TinyDB(db_path, indent=4, ensure_ascii=False, encoding="utf-8")
        self.tournaments_table = self.db.table("tournaments")
        self.matches = []

    def start_round(self, tournament_id):
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if tournament["rounds"]:
            current_round = tournament["rounds"][-1]
        else:
            return print("Aucun Round créé: Veuillez d'abord créer un Round")

        if current_round["status"] == RoundStatus.CREATED.value:
            current_round["status"] = RoundStatus.STARTED.value
            current_round["start_at"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.tournaments_table.update(tournament, doc_ids=[tournament_id])
            return print(f"{current_round['name']} démarrée avec succès !")
        else:
            return print(f"{current_round['name']} déjà en cours")

    def create_round(self, tournament_id):
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            print(f"Aucun tournoi trouvé avec l'ID: {tournament_id}")
            return

        total_tournament_rounds = len(tournament["rounds"])

        if tournament["rounds"]:
            if (
                tournament["rounds"][-1]["status"] == RoundStatus.CREATED.value
                or tournament["rounds"][-1]["status"] == RoundStatus.STARTED.value
            ):
                return print(f"Round n°{total_tournament_rounds} déjà créée ou en cours")

        total_tournament_rounds += 1
        tournament["number_of_current_round"] = total_tournament_rounds
        new_round = Round(f"Round {total_tournament_rounds}")
        tournament["rounds"].append(new_round.to_dict())
        self.tournaments_table.update(tournament, doc_ids=[tournament_id])

        print(f"{new_round.name} enregistré avec succès !")

    def generate_matches(self, tournament_id):
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            print(f"Aucun tournoi trouvé avec l'ID: {tournament_id}")
            return

        players: List[Player] = tournament.get("players", [])
        max_players = tournament.get("max_players")

        if len(players) < max_players:
            print(f"Veuillez enregistrer les {max_players} joueurs avant de créer des matchs")
            return

        current_round_number = len(tournament["rounds"])

        if current_round_number == 1:
            if (
                not tournament["rounds"][-1]["matches"]
                and tournament["rounds"][-1]["status"] == RoundStatus.STARTED.value
            ):
                self.matches = self.create_random_matches(players)
            else:
                return print("Les matchs sont déjà générés, terminez le Round en saisissant les scores")
        else:
            print("TODO")

        tournament["rounds"][-1]["matches"] = self.matches
        self.tournaments_table.update(tournament, doc_ids=[tournament_id])

        print("Les matchs ont été générés avec succès !")

    def create_random_matches(self, players: List[Player]):
        matches = []
        random.shuffle(players)

        for i in range(0, len(players) - 1, 2):
            player1 = players[i]
            player2 = players[i + 1]
            match = Match(
                player1["firstname"] + " " + player1["lastname"],
                0.0,
                player2["firstname"] + " " + player2["lastname"],
                0.0,
            )
            matches.append(match.players)

        if len(players) % 2 != 0:
            print(f"Le joueur {players[-1]['firstname']} {players[-1]['lastname']} n'a pas d'adversaire pour ce round")

        return matches

    def get_current_round_matches(self, tournament_id):
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            print(f"Aucun tournoi trouvé avec l'ID: {tournament_id}")
            return
        if not tournament["rounds"]:
            print("Aucun Round créé: Veuillez d'abord créer un Round")
            return
        current_round = tournament["rounds"][-1]

        if current_round["status"] != RoundStatus.STARTED.value:
            print("Le Round n°1 n'est pas encore démarré")
            return

        return current_round.get("matches", [])
