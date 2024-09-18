from models.player_model import PlayerManager
from views.main_menu_view import MainMenuView
from views.player_view import PlayerView
from rich.console import Console


class PlayerController:
    """
    Controller class responsible for managing player-related operations.

    This class interacts with various views and managers to handle player-related
    actions such as displaying, adding, and modifying player information.

    Methods:
        run():
            Starts the main loop for handling user choices from the player menu.
            Continues to prompt the user until an exit choice is selected.

        add_player():
            Collects player information from the user and adds a new player to the system.

        modify_player():
            Allows the user to modify an existing player's information after displaying the list of players.

        show_players():
            Retrieves and displays the list of all players.
    """

    def __init__(self):
        self.player_view = PlayerView()
        self.player_manager = PlayerManager()
        self.main_menu_view = MainMenuView()
        self.console = Console()

    def run(self):
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
        firstname, lastname, date_of_birth, point, national_id = self.player_view.request_player_info()
        self.player_manager.add_player(firstname, lastname, date_of_birth, point, national_id)

    def modify_player(self):
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
        players = self.player_manager.list_players()
        self.player_view.show_players(players, "Liste des joueurs.")
