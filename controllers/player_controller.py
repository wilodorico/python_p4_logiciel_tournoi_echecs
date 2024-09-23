from models.player_model import PlayerManager
from views.main_menu_view import MainMenuView
from views.player_view import PlayerView
from rich.console import Console


class PlayerController:
    """
    Controller class responsible for managing player-related operations.

    This class interacts with various views and managers to handle player-related
    actions such as displaying, adding, and modifying player information.

    Attributes:
        player_view (PlayerView): Manages player-related UI interactions.
        player_manager (PlayerManager): Manages player-related data operations.
        main_menu_view (MainMenuView): Manages the main menu.
        console (Console): A Rich Console object for displaying styled output in the terminal.
    """

    def __init__(self):
        self.player_view = PlayerView()
        self.player_manager = PlayerManager()
        self.main_menu_view = MainMenuView()
        self.console = Console()

    def run(self):
        """Displays the player management menu and handles user choices."""
        while True:
            self.player_view.display_player_menu()
            choice: int = self.player_view.request_user_choice()

            if choice == 1:
                self.show_players()
            if choice == 2:
                self.add_player()
            if choice == 3:
                self.modify_player()
            if choice == 4:
                break

    def add_player(self):
        """Prompts the user for player information and adds a new player to the database."""
        firstname, lastname, date_of_birth, point, national_id = self.player_view.request_player_info()
        self.player_manager.add_player(firstname, lastname, date_of_birth, point, national_id)

    def modify_player(self):
        """Allows the user to modify an existing player's information after displaying the list of players."""
        self.show_players()
        self.console.print("Entrez 0 pour quitter.")
        player_id: int = self.player_view.request_id_player()
        if player_id == 0:
            return
        player = self.player_manager.get_player_by_id(player_id)
        if player:
            firstname, lastname, date_of_birth, point, national_id = self.player_view.request_update_player_info(
                player
            )
            self.player_manager.update_player(player_id, firstname, lastname, date_of_birth, point, national_id)

    def show_players(self):
        """Displays a table of all players."""
        players = self.player_manager.list_players()
        self.player_view.show_players(players, "Liste des joueurs.")
