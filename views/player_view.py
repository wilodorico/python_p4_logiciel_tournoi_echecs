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
        print("1. Ajouter un joueur")
        print("2. Modifier un joueur")
        print("3. Retour au menu principal")
        print()

    def request_user_choice(self):
        choice: str = input("Choisissez une option (1, 2 ou 3) : ")
        print()

        try:
            choice_number: int = int(choice)
            if choice_number in [1, 2, 3]:
                return choice_number
            else:
                print("Choix invalide : Veuillez entrer 1, 2 ou 3")
                print()
        except ValueError:
            print("Veuillez entrer un nombre valide. (1, 2 ou 3)")
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
