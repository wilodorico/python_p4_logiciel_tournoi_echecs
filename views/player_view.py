from models.player_model import Player
from utils.input_validation import InputValidator
from rich.console import Console
from rich.prompt import IntPrompt
from rich.table import Table

from utils.rich_component import alert_message


class PlayerView:
    def __init__(self):
        self.console = Console()
        self.input_validator = InputValidator()

    def display_player_menu(self):
        self.console.print("============================", style="deep_sky_blue1")
        self.console.print("         Menu joueur")
        self.console.print("============================", style="deep_sky_blue1")
        self.console.print("1. Liste des joueurs")
        self.console.print("2. Ajouter un joueur")
        self.console.print("3. Modifier un joueur")
        self.console.print("4. Retour au menu principal")
        self.console.print("============================", style="deep_sky_blue1")

    def request_user_choice(self):
        try:
            choice: int = IntPrompt.ask("Choisissez une option", choices=["1", "2", "3", "4"])
            print()
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                alert_message("Veuillez entrer un choix valide [1/2/3/4]", "red")
        except ValueError:
            alert_message("Veuillez entrer un nombre valide [1/2/3/4]", "red")
            return self.display_player_menu()

    def request_player_info(self):
        """Prompts the user for player information and validates the input."""

        def prompt_with_retry(validate_func, prompt_text):
            """Helper function to prompt for input and retry until a valid value is entered."""
            while True:
                try:
                    return validate_func(input(prompt_text))
                except ValueError as e:
                    alert_message(e.args[0], "red")

        firstname = prompt_with_retry(self.input_validator.validate_non_empty_string, "Entrez son prénom : ")
        lastname = prompt_with_retry(self.input_validator.validate_non_empty_string, "Entrez son nom : ")
        date_of_birth = prompt_with_retry(
            self.input_validator.validate_date_format, "Entrez sa date de naissance (01-01-2001) : "
        )
        point = prompt_with_retry(self.input_validator.validate_positive_float, "Entrez son nombre de point : ")
        national_id = prompt_with_retry(
            self.input_validator.validate_national_id_format, "Entrez son identifiant nationnal (AB12345) : "
        )

        return firstname, lastname, date_of_birth, point, national_id

    def request_id_player(self):
        """Prompts the user to enter a player ID."""
        try:
            player_id: int = IntPrompt.ask("Veuillez entrer l'identifiant du joueur")
            return player_id
        except ValueError:
            alert_message("Veuillez entrer un nombre !", "red")
            return self.request_id_player()

    def request_update_player_info(self, player):
        """Used to update a player's information field by field.

        If the user leaves the field blank, the player's current value is retained.
        """

        self.console.print("Laissez le champ vide si vous ne souhaitez pas le changer.", style="deep_sky_blue1")

        def prompt_update_with_validation(current_value, prompt_text, validation_func=None):
            """Helper function to prompt for an update and validate input."""
            user_input = self.console.input(prompt_text).strip()

            if not user_input:
                return current_value

            if validation_func:
                try:
                    return validation_func(user_input)
                except ValueError as e:
                    alert_message(e.args[0], "red")
                    return prompt_update_with_validation(current_value, prompt_text, validation_func)

            return user_input

        firstname = prompt_update_with_validation(
            player.firstname, f"Mettre à jour son prénom [sky_blue2]({player.firstname}): "
        )

        lastname = prompt_update_with_validation(
            player.lastname, f"Mettre à jour son nom [sky_blue2]({player.lastname}): "
        )

        date_of_birth = prompt_update_with_validation(
            player.date_of_birth,
            f"Mettre à jour sa date de naissance [sky_blue2]({player.date_of_birth}): ",
            self.input_validator.validate_date_format,
        )

        point = prompt_update_with_validation(
            player.point,
            f"Mettre à jour ses points [sky_blue2]({player.point}): ",
            self.input_validator.validate_positive_float,
        )

        national_id = prompt_update_with_validation(
            player.national_id,
            f"Mettre à jour son identifiant national [sky_blue2]({player.national_id}): ",
            self.input_validator.validate_national_id_format,
        )

        return firstname, lastname, date_of_birth, point, national_id

    def show_players(self, players: list[Player], message: str):
        """Displays a table of players with their information."""
        if not players:
            alert_message("Aucun joueur Enregistré !", "deep_sky_blue1")
            return

        table = Table(title=message, show_lines=True)
        table.add_column("ID")
        table.add_column("Prénom")
        table.add_column("Nom")
        table.add_column("Date de naissance")
        table.add_column("Points")
        table.add_column("Identifiant national")

        for player in players:
            table.add_row(
                str(player.id),
                player.firstname,
                player.lastname,
                player.date_of_birth,
                str(player.point),
                player.national_id,
            )

        self.console.print(table)
