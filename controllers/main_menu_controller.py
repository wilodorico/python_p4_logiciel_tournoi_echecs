from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from views.main_menu_view import MainMenuView


class MainMenuController:

    def __init__(self):
        self.main_menu_view = MainMenuView()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()

    def run(self):
        while True:
            self.main_menu_view.display_main_menu()
            choice: int = self.main_menu_view.request_user_choice()

            if choice == 1:
                self.player_controller.run()
            if choice == 2:
                self.tournament_controller.run()
            if choice == 3:
                print("Merci d'avoir utilisé le programme.")
                break
