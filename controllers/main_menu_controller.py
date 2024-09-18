from controllers.player_controller import PlayerController
from controllers.report_controller import ReportController
from controllers.tournament_controller import TournamentController
from views.main_menu_view import MainMenuView
from utils.rich_component import alert_message


class MainMenuController:
    """
    Controller class responsible for managing the main menu and navigating to other controllers.

    This class interacts with various controllers (PlayerController, TournamentController, ReportController)
    and handles user choices from the main menu to invoke the appropriate controller operations.

    Methods:
        run():
            Starts the main loop for handling user choices from the main menu.
            Navigates to the relevant controller based on user input and exits the program on selection.
    """

    def __init__(self):
        self.main_menu_view = MainMenuView()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()
        self.report_controller = ReportController()

    def run(self):
        while True:
            self.main_menu_view.display_main_menu()
            choice: int = self.main_menu_view.request_user_choice()

            match choice:
                case 1:
                    self.player_controller.run()
                case 2:
                    self.tournament_controller.run()
                case 3:
                    self.report_controller.run()
                case 4:
                    alert_message("Merci d'avoir utilisé le programme !", "deep_sky_blue1")
                    break
