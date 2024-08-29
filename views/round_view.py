class RoundView:

    def display_main_menu(self, round_number: int):
        print("-----------------------------")
        print("Menu Round : ")
        print("-----------------------------")
        print(f"1. Démarrer le Round n°{round_number}")
        print("2. Afficher la liste des matchs")
        print("3. Terminer le Round")
        print("4. Renseigner les scores")
        print("5. Retour au menu du tournois")
        print()

    def request_user_choice(self) -> int:
        while True:
            choice = input("Veuillez entrer un choix (1, 2, 3, 4 ou 5) : ")
            print()
            try:
                choice_number: int = int(choice)
                if choice_number in [1, 2, 3, 4]:
                    return choice_number
                else:
                    print("Choix invalide : Veuillez entrer 1, 2, 3, 4 ou 5")
                    print()
            except ValueError:
                print("Erreur : Veuillez entrer un nombre (1, 2, 3, 4 ou 5)")
                print()
