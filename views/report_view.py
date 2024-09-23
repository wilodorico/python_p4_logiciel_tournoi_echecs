from rich.console import Console
from rich.prompt import IntPrompt
from rich.table import Table
from utils.rich_component import alert_message


class ReportView:
    """
    The ReportView class handles the display of various tournament and player reports to the user.

    Attributes:
        console (Console): A Rich Console object for displaying styled output in the terminal.
    """

    def __init__(self):
        self.console = Console()

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
        """Requests the user choice from the console.
        Returns the choice as an integer.
        """
        while True:
            try:
                choice: int = IntPrompt.ask("Veuillez entrer un choix", choices=["1", "2", "3", "4", "5", "6"])
                return choice
            except ValueError:
                alert_message("Erreur : Veuillez entrer un nombre [1/2/3/4/5/6]", "red")

    def request_tournament_id(self):
        """Requests the user to enter a tournament ID.
        Returns the ID as an integer.
        """
        try:
            tournament_id: int = IntPrompt.ask("Veuillez entrer l'ID du tournoi")
            return tournament_id
        except ValueError:
            alert_message("Veuillez entrer un nombre !", "red")
            return self.request_tournament_id()

    def display_all_matches_per_round_of_tournament(self, tournament):
        """Displays all matches per round of a tournament.
        Args:
            tournament (dict): Dictionary representing the tournament data.
        """
        rounds = tournament.get("rounds", [])

        # For each round, create and display a table
        for round_data in rounds:
            round_name = round_data["name"]
            matches = round_data["matches"]

            # Create a table for the current round
            table = Table(title=f"{round_name} - {round_data['status']}", title_style="bold magenta", show_lines=True)

            # Add columns to the table
            table.add_column("Match", justify="center", style="cyan")
            table.add_column("Joueur 1", style="magenta")
            table.add_column("Score 1", justify="center", style="green")
            table.add_column("Joueur 2", style="magenta")
            table.add_column("Score 2", justify="center", style="green")

            # Fill in the table with the round's matches
            for i, match in enumerate(matches):
                player1_name = match[0][0]
                score1 = match[0][1]
                player2_name = match[1][0]
                score2 = match[1][1]

                table.add_row(f"Match {i + 1}", player1_name, str(score1), player2_name, str(score2))

            # Display the round table
            self.console.print(table)

            # Display the start and end dates of the round
            round_date_end = round_data["end_at"] if round_data["end_at"] else "Toujours en cours..."
            self.console.print(f"Début : {round_data['start_at']}", style="yellow")
            self.console.print(f"Fin : {round_date_end}", style="yellow")
            self.console.print()
