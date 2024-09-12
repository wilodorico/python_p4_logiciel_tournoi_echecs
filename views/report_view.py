from rich.console import Console
from rich.prompt import IntPrompt
from utils.rich_component import alert_message


class ReportView:
    console = Console()

    def display_reports_menu(self):
        self.console.print("=================================================", style="deep_sky_blue1")
        self.console.print("                  Menu Rapports                  ")
        self.console.print("=================================================", style="deep_sky_blue1")
        self.console.print("1. Liste de tous les joueurs enregistrés")
        self.console.print("2. Liste de tous les tournois enregistrés")
        self.console.print("3. Nom et dates d'un tournoi")
        self.console.print("4. Liste des joueurs d'un tournoi")
        self.console.print("5. Liste de tous les matchs / Round d'un tournoi")
        self.console.print("6. Retour au menu principal")
        self.console.print("=================================================", style="deep_sky_blue1")

    def request_user_choice(self) -> int:
        while True:
            try:
                choice: int = IntPrompt.ask("Veuillez entrer un choix", choices=["1", "2", "3", "4", "5", "6"])
                return choice
            except ValueError:
                alert_message("Erreur : Veuillez entrer un nombre [1/2/3/4/5/6]", "red")

    def request_tournament_id(self):
        try:
            tournament_id: int = IntPrompt.ask("Veuillez entrer l'ID du tournoi")
            return tournament_id
        except ValueError:
            alert_message("Veuillez entrer un nombre !", "red")
            return self.request_tournament_id()
