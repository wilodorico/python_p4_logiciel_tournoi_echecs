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
        id: str = None,
    ):
        self.id = id
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
            "id": self.id,
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
            firstname, lastname, date_of_birth.strftime("%d-%m-%Y"), point, national_id
        )

        player_exist = self.players_table.search(
            (where("lastname") == new_player.lastname)
            & (where("firstname") == new_player.firstname)
            & (where("date_of_birth") == new_player.date_of_birth)
        )

        if player_exist:
            return (
                f"Le joueur {new_player.firstname} {new_player.lastname} existe déjà! Veuillez saisir un autre joueur",
            )

        self.players_table.insert(
            {
                "firstname": new_player.firstname,
                "lastname": new_player.lastname,
                "date_of_birth": new_player.date_of_birth,
                "point": new_player.point,
                "national_id": new_player.national_id,
            }
        )
        return f"Joueur {new_player.firstname} enregistré avec succès !"

    def update_player(
        self, player_id, firstname, lastname, date_of_birth, point, national_id
    ):

        updated_data = {
            "firstname": firstname,
            "lastname": lastname,
            "date_of_birth": str(date_of_birth),
            "point": point,
            "national_id": national_id,
        }

        self.players_table.update(updated_data, doc_ids=[player_id])

        print("Joueur modifié avec succés !")

    def list_players(self):
        players_data = self.players_table.all()
        players = []
        for player in players_data:
            players.append(
                Player(
                    player["firstname"],
                    player["lastname"],
                    player["date_of_birth"],
                    player["point"],
                    player["national_id"],
                    id=player.doc_id,
                )
            )

        return players

    def get_player_by_id(self, player_id):
        player = self.players_table.get(doc_id=player_id)
        if not player:
            print("Le joueur avec cet identifiant n'existe pas")
            return
        return Player(
            firstname=player["firstname"],
            lastname=player["lastname"],
            date_of_birth=player["date_of_birth"],
            point=player["point"],
            national_id=player["national_id"],
            id=player.doc_id,
        )
