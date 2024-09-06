from utils.input_validation import get_non_empty_input, get_valid_date_format


class TournamentView:

    def get_tournament_info(self):
        print()
        print("Renseignez les informations du tournoi.")
        print()
        name = get_non_empty_input("Veuillez entrer le nom : ")
        location = get_non_empty_input("Veuillez entrer le lieu : ")
        description = get_non_empty_input("Veuillez entrer la description : ")
        date_start = get_valid_date_format("Veuillez saisir la date de début : ")
        date_end = get_valid_date_format("Veuillez saisir la date de fin : ")

        return name, location, description, date_start, date_end

    def display_tournament_info(self, tournament):
        print("-------------------------------")
        print(f"Tournoi: {tournament['name']} le {tournament['date_start']}")
        print(f"Finit le: {tournament['date_end']}")
        print("-------------------------------")

    def display_tournament_menu(self):
        print("-------------------------------")
        print("Menu :Gestion tournoi")
        print("-------------------------------")
        print("1. Liste des tournois")
        print("2. Créer un tournoi")
        print("3. Gérer le dernier tournoi créé")
        print("4. Gérer un tournoi")
        print("5. Retour au menu principal")
        print("-------------------------------")

    def request_user_choice(self):
        while True:
            print()
            choice = input("Veuillez entrer un choix (1, 2, 3, 4 ou 5) ")
            print()
            try:
                choice_number: int = int(choice)
                if choice_number in [1, 2, 3, 4, 5]:
                    return choice_number
                else:
                    print("Choix invalide : Veuillez entrer 1, 2, 3, 4 ou 5")
                    print()
            except ValueError:
                print("Erreur : Veuillez entrer un nombre (1, 2, 3, 4 ou 5)")
                print()

    def display_tournaments(self, tournaments):
        print("Liste des tournois enregistrés.")
        print("-------------------------------------------------------------------------------")
        if tournaments:
            for tournament in tournaments:
                print(
                    (
                        f"ID: {tournament.doc_id} - {tournament['name']} "
                        f"à {tournament['location']} "
                        f"du {tournament['date_start']} au {tournament['date_end']}"
                    )
                )
        else:
            print("Aucun tournoi enregistré.")
        print("-------------------------------------------------------------------------------")

    def display_tournament_management_menu(self):
        print()
        print("1. Inscrire les joueurs")
        print("2. Liste des joueurs inscrits")
        print("3. Gérer les tours")
        print("4. Retour au menu gestion tournoi")

    def request_tournament_management_choice(self):
        while True:
            print()
            choice = input("Veuillez entrer un choix (1, 2, 3 ou 4) ")
            print()
            try:
                choice_number: int = int(choice)
                if choice_number in [1, 2, 3, 4]:
                    return choice_number
                else:
                    print("Choix invalide : Veuillez entrer 1, 2, 3 ou 4")
                    print()
            except ValueError:
                print("Erreur : Veuillez entrer un nombre (1, 2, 3 ou 4)")
                print()

    def request_tournament_id(self):
        print("")
