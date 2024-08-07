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
            self.player_view.display_player_menu()
            choice: int = self.player_view.request_user_choice()

            if choice == 1:
                self.add_player()
            if choice == 2:
                self.modify_player()
            if choice == 3:
                break

    def add_player(self):
        while True:
            firstname, lastname, date_of_birth, point, national_id = (
                self.player_view.request_player_info()
            )
            success, message = self.player_manager.add_player(
                firstname, lastname, date_of_birth, point, national_id
            )
            print(message)
            if success:
                break

    def modify_player(self):
        self.player_manager.modify_player()
