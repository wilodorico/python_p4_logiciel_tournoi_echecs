import datetime
from typing import List
from tinydb import TinyDB, where


class Player:

    def __init__(
        self,
        firstname: str,
        lastname: str,
        date_of_birth: datetime,
        point: float,
        national_id: str,
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.date_of_birth = date_of_birth
        self.point = point
        self.national_id = national_id
        self.lastest_oppenents: List[Player] = []

    def __str__(self) -> str:
        return f"{self.firstname}.{self.lastname}"

    def __repr__(self) -> str:
        return f"{self}"

    def to_dict(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "date_of_birth": self.date_of_birth,
            "point": self.point,
            "national_id": self.national_id,
        }


class PlayerManager:

    def __init__(self, db_path="data/players/players.json"):
        self.db = TinyDB(db_path, indent=4)
        self.players_table = self.db.table("players")

    def add_player(
        self,
        firstname: str,
        lastname: str,
        date_of_birth: datetime,
        point: float,
        national_id: str,
    ):
        new_player: Player = Player(
            firstname, lastname, date_of_birth, point, national_id
        )

        player_exist = self.players_table.search(
            (where("lastname") == new_player.lastname)
            & (where("firstname") == new_player.firstname)
            & (where("date_of_birth") == str(new_player.date_of_birth))
        )

        if player_exist:
            return (
                False,
                f"Le joueur {new_player.firstname} {new_player.lastname} existe déjà! Veuillez saisir un autre joueur",
            )

        self.players_table.insert(
            {
                "firstname": new_player.firstname,
                "lastname": new_player.lastname,
                "date_of_birth": str(new_player.date_of_birth),
                "point": new_player.point,
                "national_id": new_player.national_id,
            }
        )
        return True, f"Joueur {new_player.firstname} enregistré avec succès !"

    def modify_player(self):
        print("Joueur modifier !")
