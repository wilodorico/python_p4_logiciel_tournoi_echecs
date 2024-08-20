class MainMenuView:

    def display_main_menu(self):
        print("-----------------------------")
        print("Menu principal : ")
        print("-----------------------------")
        print("1. Gestion joueur")
        print("2. Gestion tournoi")
        print("3. Quitter")
        print()

    def request_user_choice(self) -> int:
        while True:
            choice = input("Veuillez entrer un choix (1, 2 ou 3): ")
            print()
            try:
                choice_number: int = int(choice)
                if choice_number in [1, 2, 3]:
                    return choice_number
                else:
                    print("Choix invalide : Veuillez entrer 1, 2 ou 3")
                    print()
            except ValueError:
                print("Erreur : Veuillez entrer un nombre (1, 2 ou 3)")
                print()
