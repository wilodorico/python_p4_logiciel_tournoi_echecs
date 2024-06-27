from typing import List


class Player:

    def __init__(
        self,
        firstname: str,
        lastname: str,
        date_of_birth,
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
        return f"""Player(firstname={self.firstname},
                    lastname={self.lastname},
                    date_of_birth={self.date_of_birth},
                    point={self.point},
                    national_id={self.national_id})"""

    def to_dict(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "date_of_birth": self.date_of_birth,
            "point": self.point,
            "national_id": self.national_id,
        }
