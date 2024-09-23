from controllers.round_controller import RoundController
from models.player_model import PlayerManager
from models.tournament_model import TournamentManager
from utils.rich_component import alert_message
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from rich.console import Console


class TournamentController:
    """
    Controller class to manage tournament-related actions, including creating tournaments, managing players,
    and rounds.

    Attributes:
        tournament_view (TournamentView): Manages tournament-related UI interactions.
        tournament_manager (TournamentManager): Handles tournament-related data operations.
        player_manager (PlayerManager): Manages player-related data operations.
        player_view (PlayerView): Manages player-related UI interactions.
        round_controller (RoundController): Handles round-related actions within the tournament.
        console (Console): A Rich Console object for displaying styled output in the terminal.
    """

    def __init__(self):
        self.tournament_view = TournamentView()
        self.tournament_manager = TournamentManager()
        self.player_manager = PlayerManager()
        self.player_view = PlayerView()
        self.round_controller = RoundController()
        self.console = Console()

    def run(self):
        """Displays the tournament management menu and handles user choices."""
        while True:
            self.tournament_view.display_tournament_menu()
            choice: int = self.tournament_view.request_user_choice()

            match choice:
                case 1:
                    self.show_tournaments()
                case 2:
                    self.create_tournament()
                case 3:
                    self.managing_last_tournament()
                case 4:
                    break

    def create_tournament(self):
        """Prompts the user to create a new tournament if the last tournament is finished."""
        tournaments = self.tournament_manager.get_tournaments()
        if tournaments:
            last_tournament = tournaments[-1]
            if not self.tournament_manager.is_tournament_finished(last_tournament.doc_id):
                alert_message(
                    "Vous ne pouvez pas créer un nouveau tournoi car le dernier tournoi n'est pas terminé !", "red"
                )
                return
        name, location, description, date_start, date_end = self.tournament_view.get_tournament_info()
        self.tournament_manager.create_tournament(name, location, description, date_start, date_end)

    def show_tournaments(self):
        """Displays a table of all available tournaments."""
        tournaments = self.tournament_manager.get_tournaments()
        self.tournament_view.display_tournaments(tournaments)

    def managing_last_tournament(self):
        """Provides management options for the last created tournament."""
        while True:
            last_tournament = self.tournament_manager.get_last_tournament()
            if not last_tournament:
                break
            self.tournament_view.display_tournament_info(last_tournament)
            self.tournament_view.display_tournament_management_menu()

            choice: int = self.tournament_view.request_tournament_management_choice()

            match choice:
                case 1:
                    self.add_players_to_tournament(last_tournament.doc_id)
                case 2:
                    self.show_players_of_tournament(last_tournament.doc_id)
                case 3:
                    self.round_controller.run(last_tournament.doc_id)
                case 4:
                    break

    def add_players_to_tournament(self, tournament_id):
        """Handles the registration of players to the tournament."""
        min_players: int = self.tournament_manager.get_min_players(tournament_id)

        # Get the remaining players and those already registered
        player_data = self.player_manager.list_players()
        registered_players = self.tournament_manager.get_registered_players(tournament_id)
        remaining_players = [p for p in player_data if p.id not in {rp.id for rp in registered_players}]

        # Display available players and those already registered
        self.player_view.show_players(remaining_players, "Liste des joueurs disponibles.")
        self.player_view.show_players(
            registered_players,
            f"Joueurs inscrits au tournoi {len(registered_players)} ({min_players} joueurs minimum)",
        )

        while True:
            self.console.print("Entrez 0 pour quitter.")
            player_id = self.player_view.request_id_player()
            if player_id == 0:
                break

            player = self.player_manager.get_player_by_id(player_id)
            if not player:
                continue

            response = self.tournament_manager.add_player_to_tournament(tournament_id, player)

            if response["player_exist"]:
                alert_message(response["message"], "red")
            else:
                registered_players.append(player)
                remaining_players = [p for p in remaining_players if p.id != player_id]

                alert_message(response["message"], "green")

                self.player_view.show_players(remaining_players, "Liste des joueurs disponibles.")
                self.player_view.show_players(
                    registered_players,
                    f"Joueurs inscrits au tournoi {len(registered_players)} ({min_players} joueurs minimum)",
                )

                if len(registered_players) == min_players:
                    self.console.print(
                        "Le nombre minimum de joueurs a été atteint. (conitunez ou Tapez 0 pour sortir)",
                        style="deep_sky_blue1",
                    )

    def show_players_of_tournament(self, tournament_id):
        """Displays a table of players registered in the tournament."""
        players = self.tournament_manager.get_registered_players(tournament_id)
        self.player_view.show_players(players, "Liste des joueurs inscrits au tournoi.")
