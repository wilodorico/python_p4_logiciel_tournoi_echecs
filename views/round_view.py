class RoundView:

    def display_main_menu(self, round_number: int):
        print("-----------------------------")
        print("Menu Round : ")
        print("-----------------------------")
        print(f"1. Démarrer le Round n°{round_number}")
        print("2. Afficher la liste des matchs")
        print("3. Renseigner les scores")
        print("4. Terminer le Round")
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

    def display_matches(self, matches):
        print("\n=== Liste des matchs générés ===")
        for i, match in enumerate(matches):
            player1 = match[0][0]
            score1 = match[0][1]
            player2 = match[1][0]
            score2 = match[1][1]
            print(f"Match {i + 1}: {player1} (Score: {score1}) vs {player2} (Score: {score2})")
        print()
