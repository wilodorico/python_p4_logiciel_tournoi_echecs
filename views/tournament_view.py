class TournamentView:

    def get_tournament_info(self):
        print()
        print("Renseignez les informations du tournoi.")
        print()
        name = input("Veuillez entrer le nom : ")
        location = input("Veuillez entrer le lieu : ")
        description = input("Veuillez entrer la description : ")
        date_start = input("Veuillez saisir la date de début : ")
        date_end = input("Veuillez saisir la date de fin : ")

        return name, location, description, date_start, date_end

    def display_tournament_info(self, tournament):
        print(f"Tournoi: {tournament.name} de {tournament.location}")
        print(f"Description: {tournament.description}")
        print(f"Date de début: {tournament.date_start}")
        print(f"Date de fin: {tournament.date_end}")

    def display_tournament_menu(self):
        print()
        print("1. Ajouter les joueurs")
        print("2. Créer le Tour")

        while True:
            choice = input("Veuillez entrer un choix (1 ou 2) ")
            print()
            try:
                choice_number: int = int(choice)
                if choice_number in [1, 2]:
                    return choice_number
                else:
                    print("Choix invalide : Veuillez entrer 1 ou 2")
                    print()
            except ValueError:
                print("Erreur : Veuillez entrer un nombre (1 ou 2)")
                print()
