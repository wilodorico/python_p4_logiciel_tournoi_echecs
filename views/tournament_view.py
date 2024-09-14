from utils.input_validation import InputValidator
from rich.console import Console
from rich.table import Table
from utils.rich_component import alert_message


class TournamentView:
    def __init__(self):
        self.console = Console()
        self.input_validator = InputValidator()

    def get_tournament_info(self):
        def prompt_with_retry(validate_func, prompt_text):
            """Helper function to prompt for input and retry until a valid value is entered."""
            while True:
                try:
                    return validate_func(input(prompt_text))
                except ValueError as e:
                    alert_message(e.args[0], "red")

        print()
        self.console.print("Renseignez les informations du tournoi.", style="deep_sky_blue1")
        print()
        name = prompt_with_retry(self.input_validator.validate_non_empty_string, "Veuillez entrer le nom : ")
        location = prompt_with_retry(self.input_validator.validate_non_empty_string, "Veuillez entrer le lieu : ")
        description = prompt_with_retry(
            self.input_validator.validate_non_empty_string, "Veuillez entrer la description : "
        )
        date_start = prompt_with_retry(
            self.input_validator.validate_date_format, "Veuillez saisir la date de début (01-01-2021) : "
        )
        date_end = prompt_with_retry(
            self.input_validator.validate_date_format, "Veuillez saisir la date de fin (01-01-2021) : "
        )

        return name, location, description, date_start, date_end

    def display_tournament_info(self, tournament):
        if tournament:
            alert_message(
                f"Tournoi: {tournament['name']} du {tournament['date_start']} au {tournament['date_end']}",
                "deep_sky_blue1",
            )

    def display_tournament_menu(self):
        self.console.print("=================================", style="deep_sky_blue1")
        self.console.print("       Gestion tournoi       ")
        self.console.print("=================================", style="deep_sky_blue1")
        self.console.print("1. Liste des tournois")
        self.console.print("2. Créer un tournoi")
        self.console.print("3. Gérer le dernier tournoi créé")
        self.console.print("4. Retour au menu principal")
        self.console.print("=================================", style="deep_sky_blue1")

    def request_user_choice(self):
        while True:
            print()
            choice = self.console.input("Veuillez entrer un choix [thistle3][1/2/3/4]: ")
            print()
            try:
                choice_number: int = int(choice)
                if choice_number in [1, 2, 3, 4]:
                    return choice_number
                else:
                    alert_message("Veuillez entrer un choix valide [1/2/3/4]", "red")
            except ValueError:
                alert_message("Veuillez entrer un choix valide [1/2/3/4]", "red")

    def display_tournaments(self, tournaments):
        if not tournaments:
            self.console.print("Aucun tournoi enregistré.", style="sky_blue2")
            return

        table = Table(title="Liste des tournois", show_lines=True)
        table.add_column("ID")
        table.add_column("Nom")
        table.add_column("Lieu")
        table.add_column("Date de début")
        table.add_column("Date de fin")

        for tournament in tournaments:
            table.add_row(
                str(tournament.doc_id),
                tournament["name"],
                tournament["location"],
                tournament["date_start"],
                tournament["date_end"],
            )

        self.console.print(table)

    def display_tournament_management_menu(self):
        self.console.print("=================================", style="deep_sky_blue1")
        self.console.print("       Menu tournoi       ")
        self.console.print("=================================", style="deep_sky_blue1")
        self.console.print("1. Inscrire les joueurs")
        self.console.print("2. Liste des joueurs inscrits")
        self.console.print("3. Gérer les Rounds")
        self.console.print("4. Retour au menu gestion tournoi")
        self.console.print("=================================", style="deep_sky_blue1")

    def request_tournament_management_choice(self):
        while True:
            print()
            choice = self.console.input("Veuillez entrer un choix [thistle3][1/2/3/4]: ")
            print()
            try:
                choice_number: int = int(choice)
                if choice_number in [1, 2, 3, 4]:
                    return choice_number
                else:
                    alert_message("Veuillez entrer un choix valide [1/2/3/4]", "red")
            except ValueError:
                alert_message("Veuillez entrer un nombre [1/2/3/4]", "red")
