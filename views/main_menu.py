class MainMenuView:

    def display_main_menu(self):
        print(
            """
              Menu principal :
              1. Enregistrer un joueur
              2. Modifier un joueur
              3. Créer un tournoi
              4. Quitter
            """
        )

        while True:
            choice = input("Veuillez entrer un choix (1, 2, 3 ou 4) ")
            try:
                choice_number: int = int(choice)
                if choice_number in [1, 2, 3, 4]:
                    return choice_number
                else:
                    print("Choix invalide : Veuillez entrer 1, 2 ou 3")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre (1, 2, 3 ou 4)")
