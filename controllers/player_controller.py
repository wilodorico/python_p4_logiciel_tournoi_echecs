from models.player_model import PlayerManager
from views.main_menu_view import MainMenuView
from views.player_view import PlayerView


class PlayerController:

    def __init__(self):
        self.player_view = PlayerView()
        self.player_manager = PlayerManager()
        self.main_menu_view = MainMenuView()

    def run(self):
        while True:
            choice: int = self.player_view.display_player_menu()

            if choice == 1:
                self.add_player()
            elif choice == 2:
                self.modify_player()
            elif choice == 3:
                break

    def add_player(self):
        firstname, lastname, date_of_birth, point, national_id = (
            self.player_view.get_player_info()
        )
        self.player_manager.add_player(
            firstname, lastname, date_of_birth, point, national_id
        )

    def modify_player(self):
        self.player_manager.modify_player()
