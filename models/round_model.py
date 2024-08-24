import datetime
from enum import Enum

from tinydb import TinyDB


class RoundStatus(Enum):
    CREATED = "Créé"
    STARTED = "En cours"
    FINISHED = "Terminé"


class Round:
    def __init__(self, name: str):
        self.name = name
        self.matchs: list = []
        self.start_at: datetime = None
        self.end_at: datetime = None
        self.status: RoundStatus = RoundStatus.CREATED

    def __str__(self) -> str:
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "matchs": self.matchs,
            "start_at": self.start_at.strftime("%d-%m-%Y") if self.start_at else None,
            "end_at": self.end_at.strftime("%d-%m-%Y") if self.end_at else None,
            "status": self.status.value,
        }

    def start(self):
        self.start_at = datetime.now()

    def end(self):
        self.end_at = datetime.now()

    def is_running(self):
        if self.start_at:
            return True
        return False


class RoundManager:
    def __init__(self, db_path="data/tournaments/tournaments.json"):
        self.db = TinyDB(db_path, indent=4, ensure_ascii=False, encoding="utf-8")
        self.tournaments_table = self.db.table("tournaments")

    def create_round(self, tournament_id):
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        total_tournament_rounds = len(tournament["rounds"])
        current_round = tournament["number_of_current_round"]

        if tournament["rounds"]:
            if (
                tournament["rounds"][-1]["status"] == RoundStatus.CREATED.value
                or tournament["rounds"][-1]["status"] == RoundStatus.STARTED.value
            ):
                return print(f"Tour n°{total_tournament_rounds} déjà créée ou en cours")

        total_tournament_rounds += 1
        new_round = Round(f"Tour n°{total_tournament_rounds}")
        tournament["rounds"].append(new_round.to_dict())
        self.tournaments_table.update(tournament, doc_ids=[tournament_id])

        print(f"Round '{new_round.name}' enregistré avec succès !")

    def start_round(self, tournament_id):
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if tournament["rounds"]:
            current_round = tournament["rounds"][-1]
        else:
            return print("Aucun tour créé: Veuillez d'abord créer un tour")

        if current_round["status"] == RoundStatus.CREATED.value:
            current_round["status"] = RoundStatus.STARTED.value
            self.tournaments_table.update(tournament, doc_ids=[tournament_id])
            return print(f"{current_round['name']} démarrée avec succès !")
        else:
            return print(f"{current_round['name']} déjà en cours")
