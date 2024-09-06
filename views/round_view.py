class RoundView:

    def display_main_menu(self, round_number: int):
        print("-----------------------------")
        print("Menu Round : ")
        print("-----------------------------")
        print(f"1. Démarrer le Round n°{round_number}")
        print("2. Afficher la liste des matchs")
        print("3. Renseigner les scores")
        print("4. Retour au menu du tournoi")
        print()

    def request_user_choice(self) -> int:
        while True:
            choice = input("Veuillez entrer un choix (1, 2, 3 ou 4) : ")
            print()
            try:
                choice_number: int = int(choice)
                if choice_number in [1, 2, 3, 4]:
                    return choice_number
                else:
                    print("Choix invalide : Veuillez entrer 1, 2, 3, ou 4")
                    print()
            except ValueError:
                print("Erreur : Veuillez entrer un nombre (1, 2, 3, ou 4)")
                print()

    def display_matches(self, matches):
        print("=== Liste des matchs ===")
        for i, match in enumerate(matches):
            player1 = match[0][0]
            score1 = match[0][1]
            player2 = match[1][0]
            score2 = match[1][1]
            print(f"Match {i + 1}: {player1} (Score: {score1}) vs {player2} (Score: {score2})")
        print()

    def prompt_for_match_result(self, match, match_number: int):
        """Affiche les options de résultats pour un match et renvoie le choix de l'utilisateur."""
        player1_name = match[0][0]
        player2_name = match[1][0]
        print(f"\nRésultat du match {match_number}: {player1_name} vs {player2_name}")
        print("1. Victoire de", player1_name)
        print("2. Victoire de", player2_name)
        print("3. Égalité")

        while True:
            try:
                choice: int = int(input("Choisissez le résultat (1, 2, 3): "))
                if choice in [1, 2, 3]:
                    return choice
                else:
                    print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")
