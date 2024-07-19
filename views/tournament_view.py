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
        print(f"Tournoi: {tournament.name} de {tournament.location}")
        print(f"Description: {tournament.description}")
        print(f"Date de début: {tournament.date_start}")
        print(f"Date de fin: {tournament.date_end}")

    def display_tournament_menu(self):
        print()
        print("1. Liste des tournois")
        print("2. Créer un tournoi")
        print("3. Ajouter les joueurs au tournoi")
        print("4. Créer un tour")
        print("5. Retour au menu principal")

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
        print(
            "-------------------------------------------------------------------------------"
        )
        for tournament in tournaments:
            print(tournament)

        print(
            "-------------------------------------------------------------------------------"
        )
