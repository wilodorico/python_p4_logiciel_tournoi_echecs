from rich.console import Console
from rich.table import Table
from utils.rich_component import alert_message


class RoundView:
    console = Console()

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
        # Créer un tableau avec Rich
        table = Table(title="Liste des matchs", show_lines=True)

        # Ajouter les colonnes au tableau
        table.add_column("Match", justify="center", style="cyan", no_wrap=True)
        table.add_column("Joueur 1", style="magenta")
        table.add_column("Score 1", justify="center", style="green")
        table.add_column("Joueur 2", style="magenta")
        table.add_column("Score 2", justify="center", style="green")

        # Remplir le tableau avec les matchs
        for i, match in enumerate(matches):
            player1 = match[0][0]
            score1 = match[0][1]
            player2 = match[1][0]
            score2 = match[1][1]

            # Ajouter une ligne au tableau
            table.add_row(f"Match {i + 1}", player1, str(score1), player2, str(score2))

        # Afficher le tableau dans la console
        self.console.print(table)

    def prompt_for_match_result(self, match, match_number: int):
        """Displays the results options for a match and returns the user's choice."""
        player1_name = match[0][0]
        player2_name = match[1][0]
        self.console.print(
            f"Résultat du match {match_number}: [steel_blue1]{player1_name} "
            f"[spring_green1]vs [light_steel_blue]{player2_name}"
        )
        self.console.print(f"1. Victoire de [steel_blue1]{player1_name}")
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
