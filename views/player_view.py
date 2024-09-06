from models.player_model import Player
from utils.input_validation import (
    get_non_empty_input,
    get_valid_date_format,
    get_valid_float,
    get_valid_national_id_format,
)
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.table import Table


class PlayerView:
    console = Console()

    def display_player_menu(self):
        self.console.print("=============================", style="slate_blue3")
        self.console.print("         Menu joueur")
        self.console.print("=============================", style="slate_blue3")
        self.console.print("1. Liste des joueurs")
        self.console.print("2. Ajouter un joueur")
        self.console.print("3. Modifier un joueur")
        self.console.print("4. Retour au menu principal")
        self.console.print()

    def request_user_choice(self):
        try:
            choice: int = IntPrompt.ask("Choisissez une option", choices=["1", "2", "3", "4"])
            print()
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Choix invalide : Veuillez entrer 1, 2, 3 ou 4")
                print()
        except ValueError:
            print("Veuillez entrer un nombre valide. (1, 2, 3 ou 4)")
            print()
            return self.display_player_menu()

    def request_player_info(self):
        firstname = get_non_empty_input("Entrez son prénom : ")
        lastname = get_non_empty_input("Entrez son nom : ")
        date_of_birth = get_valid_date_format("Entrez sa date de naissance : ")
        point = get_valid_float("Entrez son nombre de point : ")
        national_id = get_valid_national_id_format("Entrez son identifiant nationnal : ")

        return firstname, lastname, date_of_birth, point, national_id

    def request_id_player(self):
        player_id: str = Prompt.ask("Veuillez entrer l'identifiant du joueur").strip()
        print()
        try:
            player_id: int = int(player_id)
            return player_id
        except ValueError:
            print("Erreur: Veuillez entrer un nombre !")
            print()
            return self.request_id_player()

    def request_update_player_info(self, player):
        self.console.print("Laisser le champ vide si vous ne voulez pas le changer.", style="sky_blue2")
        firstname = input(f"Mettre à jour son prénom ({player.firstname}): ").strip() or player.firstname
        lastname = input(f"Mettre à jour son nom ({player.lastname}): ").strip() or player.lastname
        date_of_birth_str = (
            input(f"Mettre à jour sa date de naissance ({player.date_of_birth}): ").strip() or player.date_of_birth
        )
        point_str = input(f"Mettre à jour ses points ({player.point}): ").strip() or player.point
        national_id = (
            input(f"Mettre à jour son identifiant nationnal ({player.national_id}): ").strip() or player.national_id
        )

        return firstname, lastname, date_of_birth_str, point_str, national_id

    def show_players(self, players: list[Player], message: str):
        if not players:
            self.console.print("Aucun joueur Enregistré !", style="sky_blue2")
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
