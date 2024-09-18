import datetime
from typing import List
from tinydb import TinyDB, where
from utils.rich_component import alert_message


class Player:
    """
    Represents a player in a tournament.

    Attributes:
        id (str): Unique identifier for the player.
        firstname (str): First name of the player.
        lastname (str): Last name of the player.
        date_of_birth (datetime): Date of birth of the player.
        point (float): Points accumulated by the player in the tournament.
        national_id (str): National ID of the player authorized format (AB45612).
        latest_opponents (List[Player]): List of opponents the player has already faced.

    Methods:
        __str__(): Returns the player's full name.
        __repr__(): Provides a string representation of the player.
        add_opponent(opponent_id): Adds an opponent to the player's opponent list if not already present.
        to_dict(): Converts the player's attributes into a dictionary format.
    """

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
        self.latest_opponents: List[Player] = []

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"

    def __repr__(self) -> str:
        return f"{self}"

    def add_opponent(self, opponent_id):
        """Adds an opponent to the list of opponents encountered if not already present."""
        if opponent_id not in self.latest_opponents:
            self.latest_opponents.append(opponent_id)

    def to_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "date_of_birth": self.date_of_birth,
            "point": self.point,
            "national_id": self.national_id,
            "latest_opponents": self.latest_opponents,
        }


class PlayerManager:
    """
    A class that manages player-related operations, including adding, updating, and retrieving player data
    from the database.

    Attributes:
        db (TinyDB): The database instance for storing player data.
        players_table (TinyDB.table): The table within the database that holds player information.

    Methods:
        add_player: Adds a new player to the database if they do not already exist.
        update_player: Updates an existing player's information in the database.
        list_players: Retrieves all players from the database and returns them as Player instances.
        get_player_by_id: Retrieves a player from the database using their unique ID.
    """

    def __init__(self, db_path="data/players/players.json"):
        self.db = TinyDB(db_path, indent=4, ensure_ascii=False, encoding="utf-8")
        self.players_table = self.db.table("players")

    def add_player(
        self,
        firstname: str,
        lastname: str,
        date_of_birth: datetime,
        point: float,
        national_id: str,
    ):
        new_player = Player(firstname, lastname, date_of_birth.strftime("%d-%m-%Y"), point, national_id)

        player_exist = self.players_table.search(
            (where("lastname") == new_player.lastname)
            & (where("firstname") == new_player.firstname)
            & (where("date_of_birth") == new_player.date_of_birth)
        )

        if player_exist:
            alert_message(
                f"{new_player.firstname} {new_player.lastname} existe déjà ! Veuillez saisir un autre joueur.", "red"
            )
            return

        self.players_table.insert(
            {
                "firstname": new_player.firstname,
                "lastname": new_player.lastname,
                "date_of_birth": new_player.date_of_birth,
                "point": new_player.point,
                "national_id": new_player.national_id,
            }
        )
        alert_message(f"Joueur {new_player.firstname} {new_player.lastname} ajouté avec succès !", "green")

    def update_player(self, player_id, firstname, lastname, date_of_birth, point, national_id):
        updated_data = {
            "firstname": firstname,
            "lastname": lastname,
            "date_of_birth": str(date_of_birth),
            "point": point,
            "national_id": national_id,
        }

        self.players_table.update(updated_data, doc_ids=[player_id])
        alert_message("Joueur modifié avec succés !", "green")

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
            alert_message("Le joueur avec cet identifiant n'existe pas", "red")
            return
        return Player(
            firstname=player["firstname"],
            lastname=player["lastname"],
            date_of_birth=player["date_of_birth"],
            point=player["point"],
            national_id=player["national_id"],
            id=player.doc_id,
        )
