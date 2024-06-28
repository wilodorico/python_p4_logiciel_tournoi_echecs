from views.main_menu_view import MainMenuView


class MainMenuController:

    def __init__(self):
        self.main_menu_view = MainMenuView()

    def run(self):
        while True:
            choice: int = self.main_menu_view.display_main_menu()

            if choice == 1:
                print("Menu gestion joueur")
            elif choice == 2:
                print("Créer un tournoi")
            elif choice == 3:
                print("Merci d'avoir utilisé le programme.")
                break
