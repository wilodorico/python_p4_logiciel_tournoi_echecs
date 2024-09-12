from views.report_view import ReportView
from models.player_model import PlayerManager
from views.player_view import PlayerView
from models.tournament_model import TournamentManager
from views.tournament_view import TournamentView


class ReportController:

    def __init__(self):
        self.report_view = ReportView()
        self.player_manager = PlayerManager()
        self.player_view = PlayerView()
        self.tournament_manager = TournamentManager()
        self.tournament_view = TournamentView()

    def run(self):
        while True:
            self.report_view.display_reports_menu()
            choice = self.report_view.request_user_choice()

            match choice:
                case 1:
                    self.get_all_players()
                case 2:
                    self.get_all_tournaments()
                case 3:
                    self.tournament_name_and_dates()
                case 4:
                    self.get_players_of_tournament()
                case 5:
                    self.get_all_matches_per_round_of_tournament()
                case 6:
                    break

    def get_all_players(self):
        players = self.player_manager.list_players()
        self.player_view.show_players(players, "Liste des joueurs.")

    def get_all_tournaments(self):
        tournaments = self.tournament_manager.get_tournaments()
        self.tournament_view.display_tournaments(tournaments)

    def tournament_name_and_dates(self):
        tournament = self.get_tournament_by_id()
        self.tournament_view.display_tournament_info(tournament)

    def get_players_of_tournament(self):
        tournament = self.get_tournament_by_id()
        players = self.tournament_manager.get_registered_players(tournament.doc_id)
        self.player_view.show_players(players, f"Liste des joueurs inscrits au tournoi {tournament['name']}")

    def get_all_matches_per_round_of_tournament(self):
        tournament = self.get_tournament_by_id()
        self.tournament_view.display_tournament_info(tournament)
        self.report_view.display_all_matches_per_round_of_tournament(tournament)

    def get_tournament_by_id(self):
        self.get_all_tournaments()
        choice: int = self.report_view.request_tournament_id()
        tournament = self.tournament_manager.get_tournament_by_id(choice)
        return tournament
