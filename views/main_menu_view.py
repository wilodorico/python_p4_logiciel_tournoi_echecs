from rich.console import Console
from rich.prompt import Prompt


class MainMenuView:
    console = Console()

    def display_main_menu(self):
        self.console.print("======================", style="deep_sky_blue1")
        self.console.print("    Menu principal    ")
        self.console.print("======================", style="deep_sky_blue1")
        self.console.print("1. Gestion joueur")
        self.console.print("2. Gestion tournoi")
        self.console.print("3. Quitter")
        self.console.print()

    def request_user_choice(self) -> int:
        while True:
            choice = Prompt.ask("Veuillez entrer un choix", choices=["1", "2", "3"])
            print()
            try:
                choice_number: int = int(choice)
                if choice_number in [1, 2, 3]:
                    return choice_number
                else:
                    print("Choix invalide : Veuillez entrer 1, 2 ou 3")
                    print()
            except ValueError:
                print("Erreur : Veuillez entrer un nombre (1, 2 ou 3)")
                print()
