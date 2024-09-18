from rich.console import Console
from rich.table import Table
from utils.rich_component import alert_message


class RoundView:
    """
    The RoundView class is responsible for displaying and interacting with
    the user regarding round managementin the tournament.

    Attributes:
        console (Console): A Rich Console object for displaying styled output in the terminal.

    Methods:
        display_main_menu(round_number: int): Displays the main menu for round management.
        request_user_choice() -> int: Prompts the user to select an option from the round management menu.
        display_matches(matches): Displays a list of matches in a formatted table.
        prompt_for_match_result(match, match_number: int) -> int: Prompts the user to enter the result of a match.
    """

    def __init__(self):
        self.console = Console()

    def display_main_menu(self, round_number: int):
        self.console.print("=================================", style="deep_sky_blue1")
        self.console.print("       Gestion Round       ")
        self.console.print("=================================", style="deep_sky_blue1")
        self.console.print(f"1. Démarrer le Round n°{round_number}")
        self.console.print("2. Afficher la liste des matchs")
        self.console.print("3. Renseigner les scores")
        self.console.print("4. Retour au menu du tournoi")
        self.console.print("=================================", style="deep_sky_blue1")

    def request_user_choice(self) -> int:
        while True:
            choice = self.console.input("Veuillez entrer un choix [thistle3][1/2/3/4]: ")
            print()
            try:
                choice_number: int = int(choice)
                if choice_number in [1, 2, 3, 4]:
                    return choice_number
                else:
                    alert_message("Veuillez entrer un valide [1/2/3/4]", "red")
            except ValueError:
                alert_message("Veuillez entrer un nombre [1/2/3/4]", "red")

    def display_matches(self, matches):
        table = Table(title="Liste des matchs", show_lines=True)

        table.add_column("Match", justify="center", style="cyan", no_wrap=True)
        table.add_column("Joueur 1", style="magenta")
        table.add_column("Score 1", justify="center", style="green")
        table.add_column("Joueur 2", style="magenta")
        table.add_column("Score 2", justify="center", style="green")

        # Fill in the table with the matches
        for i, match in enumerate(matches):
            player1 = match[0][0]
            score1 = match[0][1]
            player2 = match[1][0]
            score2 = match[1][1]

            # Add a row to the table
            table.add_row(f"Match {i + 1}", player1, str(score1), player2, str(score2))

        self.console.print(table)

    def prompt_for_match_result(self, match, match_number: int):
        """Displays the results options for a match and returns the user's choice."""
        player1_name = match[0][0]
        player2_name = match[1][0]
        self.console.print(
            f"Résultat du match {match_number}: [magenta]{player1_name} "
            f"[spring_green1]vs [light_steel_blue]{player2_name}"
        )
        self.console.print(f"1. Victoire de [magenta]{player1_name}")
        self.console.print(f"2. Victoire de [light_steel_blue]{player2_name}")
        self.console.print("3. Égalité")

        while True:
            try:
                choice: int = int(self.console.input("Choisissez le résultat [1/2/3]: "))
                if choice in [1, 2, 3]:
                    return choice
                else:
                    alert_message("Veuillez entrer un choix valide [1/2/3]", "red")
            except ValueError:
                alert_message("Veuillez entrer un nombre [1/2/3]", "red")
