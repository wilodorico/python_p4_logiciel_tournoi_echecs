from rich.console import Console
from rich.prompt import IntPrompt

from utils.rich_component import alert_message


class MainMenuView:
    """Class to display the main menu."""

    def __init__(self):
        self.console = Console()

    def display_main_menu(self):
        self.console.print("=========================", style="deep_sky_blue1")
        self.console.print("    Menu principal    ")
        self.console.print("=========================", style="deep_sky_blue1")
        self.console.print("1. Gestion joueur")
        self.console.print("2. Gestion tournoi")
        self.console.print("3. Consulter les rapports")
        self.console.print("4. Quitter")
        self.console.print("=========================", style="deep_sky_blue1")

    def request_user_choice(self) -> int:
        """Requests the user choice from the console.
        Returns the choice as an integer.
        """
        while True:
            try:
                choice: int = IntPrompt.ask("Veuillez entrer un choix", choices=["1", "2", "3", "4"])
                return choice
            except ValueError:
                alert_message("Erreur : Veuillez entrer un nombre [1/2/3/4]", "red")
