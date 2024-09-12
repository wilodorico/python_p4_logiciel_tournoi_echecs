from controllers.round_controller import RoundController
from models.player_model import PlayerManager
from models.tournament_model import TournamentManager
from utils.rich_component import alert_message
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from rich.console import Console


class TournamentController:
    console = Console()

    def __init__(self):
        self.tournament_view = TournamentView()
        self.tournament_manager = TournamentManager()
        self.player_manager = PlayerManager()
        self.player_view = PlayerView()
        self.round_controller = RoundController()

    def run(self):
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
                    # self.managing_tournament(tournament_id)
                    pass
                case 5:
                    break

    def create_tournament(self):
        name, location, description, date_start, date_end = self.tournament_view.get_tournament_info()
        self.tournament_manager.create_tournament(name, location, description, date_start, date_end)

    def show_tournaments(self):
        tournaments = self.tournament_manager.get_tournaments()
        self.tournament_view.display_tournaments(tournaments)

    def managing_last_tournament(self):
        while True:
            last_tournament = self.tournament_manager.get_last_tournament()
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
        max_players: int = self.tournament_manager.get_max_players(tournament_id)

        # Get the remaining players and those already registered
        player_data = self.player_manager.list_players()
        registered_players = self.tournament_manager.get_registered_players(tournament_id)
        remaining_players = [p for p in player_data if p.id not in {rp.id for rp in registered_players}]

        # Display available players and those already registered
        self.player_view.show_players(remaining_players, "Liste des joueurs disponibles.")
        self.player_view.show_players(
            registered_players, f"Joueurs inscrits au tournoi {len(registered_players)}/{max_players}"
        )

        while len(registered_players) < max_players:
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
                    registered_players, f"Joueurs inscrits au tournoi {len(registered_players)}/{max_players}"
                )

        if len(registered_players) >= max_players:
            self.console.print("Le nombre maximal de joueurs a été atteint pour ce tournoi.", style="deep_sky_blue1")

    def show_players_of_tournament(self, tournament_id):
        players = self.tournament_manager.get_registered_players(tournament_id)
        self.player_view.show_players(players, "Liste des joueurs inscrits au tournoi.")
