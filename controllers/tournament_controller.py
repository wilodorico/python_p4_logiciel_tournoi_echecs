from models.tournament_model import TournamentManager
from views.tournament_view import TournamentView


class TournamentController:

    def __init__(self):
        self.tournament_view = TournamentView()
        self.tournament_manager = TournamentManager()

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
                    break

    def create_tournament(self):
        name, location, description, date_start, date_end = (
            self.tournament_view.get_tournament_info()
        )

        self.tournament_manager.create_tournament(
            name, location, description, date_start, date_end
        )

    def show_tournaments(self):
        tournaments = self.tournament_manager.get_tournaments()
        self.tournament_view.display_tournaments(tournaments)

    def managing_tournament(self):
        while True:
            self.tournament_view.display_tournament_management_menu()
            choice: int = self.tournament_view.request_tournament_management_choice()

            match choice:
                case 1:
                    # self.add_players_to_tournament()
                    print("TODO")
                case 2:
                    # self.show_players_of_tournament()
                    print("TODO 2")
                case 3:
                    # self.managing_rounds_of_tournament()
                    print("TODO 3")
                case 4:
                    break
