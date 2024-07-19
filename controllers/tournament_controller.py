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

            # remplacer par le match case

            if choice == 1:
                # self.show_tournaments()
                pass
            if choice == 2:
                self.create_tournament()
            if choice == 3:
                # self.add_player_to_tournament()
                pass
            if choice == 4:
                pass
            if choice == 5:
                break

    def create_tournament(self):
        name, location, description, date_start, date_end = (
            self.tournament_view.get_tournament_info()
        )

        self.tournament_manager.create_tournament(
            name, location, description, date_start, date_end
        )
