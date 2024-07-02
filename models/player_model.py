import datetime
from typing import List


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

    def __init__(self):
        self.players: List[Player] = []

    def add_player(
        self,
        firstname: str,
        lastname: str,
        date_of_birth: datetime,
        point: float,
        national_id: str,
    ):
        player: Player = Player(firstname, lastname, date_of_birth, point, national_id)
        self.players.append(player)
        print(self.players)

    def modify_player(self):
        print("Joueur modifier !")
