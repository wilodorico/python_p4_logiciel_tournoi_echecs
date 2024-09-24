from rich.console import Console
from rich.table import Table
from utils.rich_component import alert_message


class RoundView:
    """The RoundView class handles the display and interaction related to round management.

    Attributes:
        console (Console): A Rich Console object for displaying styled output in the terminal.
    """

    def __init__(self):
        self.console = Console()

    def display_round_menu(self):
        self.console.print("=================================", style="deep_sky_blue1")
        self.console.print("       Gestion Round       ")
        self.console.print("=================================", style="deep_sky_blue1")
        self.console.print("1. Démarrer un Round")
        self.console.print("2. Afficher la liste des matchs")
        self.console.print("3. Renseigner les scores")
        self.console.print("4. Voir le classement")
        self.console.print("5. Retour au menu du tournoi")
        self.console.print("=================================", style="deep_sky_blue1")

    def request_user_choice(self) -> int:
        """Asks the player to choose an option from the Round management menu
        Returns:
            choice_number (int): The number of the chosen option
        """
        while True:
            choice = self.console.input("Veuillez entrer un choix [thistle3][1/2/3/4/5]: ")
            print()
            try:
                choice_number: int = int(choice)
                if choice_number in [1, 2, 3, 4, 5]:
                    return choice_number
                else:
                    alert_message("Veuillez entrer un valide [1/2/3/4/5]", "red")
            except ValueError:
                alert_message("Veuillez entrer un nombre [1/2/3/4/5]", "red")

    def display_matches(self, matches):
        """Displays the list of matches for the current round."""
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
        """Prompts the player to enter the result of a match.
        Returns:
            choice (int): The number of the chosen option
        """
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

    def display_rankings(self, players):
        """Displays the ranking of players based on their points."""

        table = Table(title="=== Classement joueurs ===", show_lines=True)
        table.add_column("Rang", justify="right", style="cyan", no_wrap=True)
        table.add_column("Prénom", style="magenta")
        table.add_column("Nom", style="magenta")
        table.add_column("Points", justify="right", style="green")

        for rank, player in enumerate(players, start=1):
            table.add_row(str(rank), player.firstname, player.lastname, str(player.point))

        self.console.print(table)
