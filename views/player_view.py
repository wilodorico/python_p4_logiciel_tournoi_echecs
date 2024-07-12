from utils.input_validation import (
    get_non_empty_input,
    get_valid_date_format,
    get_valid_float,
    get_valid_national_id_format,
)


class PlayerView:

    def display_player_menu(self):
        print("---------------------------")
        print("Menu joueur : ")
        print("---------------------------")
        print("1. Liste des joueurs")
        print("2. Ajouter un joueur")
        print("3. Modifier un joueur")
        print("4. Retour au menu principal")
        print()

    def request_user_choice(self):
        choice: str = input("Choisissez une option (1, 2, 3 ou 4) : ")
        print()

        try:
            choice_number: int = int(choice)
            if choice_number in [1, 2, 3, 4]:
                return choice_number
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
        national_id = get_valid_national_id_format(
            "Entrez son identifiant nationnal : "
        )

        return firstname, lastname, date_of_birth, point, national_id

    def request_id_player(self):
        player_id: str = input("Veuillez entrer l'identifiant du joueur à modifier : ")
        print()
        try:
            player_id: int = int(player_id)
            return player_id
        except ValueError:
            print("Erreur: Veuillez entrer un nombre !")
            print()
            return self.request_id_player()

    def request_update_player_info(self, player):
        print("Laisser le champ vide si vous ne voulez pas le changer.")
        firstname = (
            input(f"Mettre à jour son prénom ({player.firstname}): ").strip()
            or player.firstname
        )
        lastname = (
            input(f"Mettre à jour son nom ({player.lastname}): ").strip()
            or player.lastname
        )
        date_of_birth_str = (
            input(
                f"Mettre à jour sa date de naissance ({player.date_of_birth}): "
            ).strip()
            or player.date_of_birth
        )
        point_str = (
            input(f"Mettre à jour ses points ({player.point}): ").strip()
            or player.point
        )
        national_id = (
            input(
                f"Mettre à jour son identifiant nationnal ({player.national_id}): "
            ).strip()
            or player.national_id
        )

        return firstname, lastname, date_of_birth_str, point_str, national_id

    def show_players(self, players):
        print("Voici la liste des joueurs enregistrés.")
        print(
            "---------------------------------------------------------------------------------------------------------"
        )
        for player in players:
            print(player.to_dict())

        print(
            "---------------------------------------------------------------------------------------------------------"
        )
