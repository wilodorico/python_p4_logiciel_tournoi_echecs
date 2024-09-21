import datetime
from typing import List

from tinydb import TinyDB

from models.player_model import Player
from models.round_model import Round, RoundStatus
from utils.rich_component import alert_message
from rich.console import Console
from rich.table import Table


class Tournament:
    """
    Represents a tournament with rounds and players.

    Attributes:
        name (str): The name of the tournament.
        location (str): The location where the tournament takes place.
        description (str): A brief description of the tournament.
        date_start (datetime): The start date of the tournament.
        date_end (datetime): The end date of the tournament.
        number_of_round (int): The total number of rounds in the tournament, default is 4.
        number_of_current_round (int): The current round number in progress, starting from 0.
        rounds (List[Round]): A list of rounds that belong to the tournament.
        players (List[Player]): A list of players participating in the tournament.
        min_players (int): The minimum number of players allowed in the tournament,
                           default is twice the number of rounds.

    Methods:
        __str__(): Returns a string representation of the tournament.
        to_dict(): Converts the tournament instance into a dictionary for serialization or storage.
    """

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
        self.number_of_current_round: int = 0
        self.rounds: List[Round] = []
        self.players: List[Player] = []
        self.min_players: int = self.number_of_round * 2

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
            "min_players": self.min_players,
        }


class TournamentManager:
    """
    The TournamentManager class handles the creation, retrieval, and management of tournaments,
    as well as player management within tournaments.

    Attributes:
        db (TinyDB): The database connection to store and retrieve tournament data.
        tournaments_table (Table): The specific table within the TinyDB where tournament data is stored.
        console (Console): A Rich Console object for printing styled messages in the terminal.

    Methods:
        create_tournament(name, location, description, date_start, date_end): Creates and stores a new tournament in
                                                                              the database.
        get_tournaments(): Retrieves and returns a list of all tournaments from the database.
        get_tournament_by_id(tournament_id): Retrieves a specific tournament by its ID.
        get_last_tournament(): Retrieves the most recently created tournament.
        get_registered_players(tournament_id): Retrieves a list of players registered for a given tournament.
        add_player_to_tournament(tournament_id, player): Adds a player to a tournament.
        get_min_players(tournament_id): Retrieves the minimum number of players allowed in the tournament.
        is_tournament_finished(tournament_id) -> bool: Checks if the tournament has been completed.
        display_final_rankings(tournament_id): Displays the final player rankings based on tournament performance.
    """

    def __init__(self, db_path="data/tournaments/tournaments.json"):
        self.db = TinyDB(db_path, indent=4, ensure_ascii=False, encoding="utf-8")
        self.tournaments_table = self.db.table("tournaments")
        self.console = Console()

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

        alert_message(f"Tournoi '{new_tournament.name}' enregistré avec succès !", "green")

    def get_tournaments(self):
        tournaments = self.tournaments_table.all()
        return tournaments

    def get_tournament_by_id(self, tournament_id):
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            alert_message(f"Aucun tournoi trouvé avec l'ID: {tournament_id}", "red")
            return

        return tournament

    def get_last_tournament(self):
        tournament_data = self.tournaments_table.all()
        if not tournament_data:
            return alert_message("Aucun tournoi enregistré", "red")
        last_tournament = tournament_data[-1]
        return last_tournament

    def get_registered_players(self, tournament_id):
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            alert_message(f"Aucun tournoi trouvé avec l'ID: {tournament_id}", "red")
            return
        registered_players = tournament["players"]
        players = []

        for player in registered_players:
            players.append(
                Player(
                    player["firstname"],
                    player["lastname"],
                    player["date_of_birth"],
                    player["point"],
                    player["national_id"],
                    player["id"],
                )
            )
        return players

    def add_player_to_tournament(self, tournament_id, player: Player):
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            alert_message(f"Aucun tournoi trouvé avec l'ID: {tournament_id}", "red")
            return

        for player_tournament in tournament["players"]:
            if player_tournament["id"] == player.id:
                return {
                    "player_exist": True,
                    "message": "Ce joueur est déjà enregistré au tournoi",
                }

        tournament["players"].append(player.to_dict())
        self.tournaments_table.update(tournament, doc_ids=[tournament_id])

        return {
            "player_exist": False,
            "message": f"Joueur {player.firstname} {player.lastname} ajouté au tournoi {tournament['name']}",
        }

    def get_min_players(self, tournament_id):
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            alert_message(f"Aucun tournoi trouvé avec l'ID: {tournament_id}", "red")
            return
        return tournament["min_players"]

    def is_tournament_finished(self, tournament_id) -> bool:
        """Returns True if the tournament is finished, otherwise False."""
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            alert_message(f"Aucun tournoi trouvé avec l'ID: {tournament_id}", "red")
            return False
        number_of_round = tournament["number_of_round"]
        number_of_current_round = len(tournament["rounds"])
        is_total_rounds_complete = number_of_current_round == number_of_round

        if is_total_rounds_complete:
            last_round = tournament["rounds"][-1]
            if last_round["status"] == RoundStatus.FINISHED.value:
                return True
        return False

    def display_final_rankings(self, tournament_id):
        """Displays the final ranking of players based on their points."""
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            alert_message(f"Aucun tournoi trouvé avec l'ID: {tournament_id}", "red")
            return
        players = tournament.get("players", [])
        players.sort(key=lambda player: player["point"], reverse=True)

        table = Table(title="=== Classement Final ===", show_lines=True)
        table.add_column("Rang", justify="right", style="cyan", no_wrap=True)
        table.add_column("Prénom", style="magenta")
        table.add_column("Nom", style="magenta")
        table.add_column("Points", justify="right", style="green")

        for rank, player in enumerate(players, start=1):
            table.add_row(str(rank), player["firstname"], player["lastname"], str(player["point"]))

        self.console.print(table)
