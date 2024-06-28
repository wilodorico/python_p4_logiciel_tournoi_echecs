class PlayerView:

    def display_player_menu(self):
        print("---------------------------")
        print("Menu joueur : ")
        print("---------------------------")
        print("1. Ajouter un joueur")
        print("2. Modifier un joueur")
        print("3. Retour au menu principal")
        print()

        choice: str = input("Choisissez une option (1, 2 ou 3) : ")
        print()

        try:
            choice_number: int = int(choice)
            return choice_number
        except ValueError:
            print("Veuillez entrer un nombre valide. (1, 2 ou 3)")
            print()
            return self.display_player_menu()

    def get_player_info(self):
        firstname = input("Entrez son prénom : ")
        lastname = input("Entrez son nom : ")
        date_of_birth = input("Entrez sa date de naissance : ")
        point = input("Entrez son nombre de point : ")
        national_id = input("Entrez son identifiant nationnal : ")

        return firstname, lastname, date_of_birth, point, national_id
