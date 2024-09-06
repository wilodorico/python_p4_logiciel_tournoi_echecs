from typing import List
from models.player_model import PlayerManager
from models.round_model import RoundManager
from models.tournament_model import TournamentManager
from views.main_menu_view import MainMenuView
from views.round_view import RoundView


class RoundController:

    def __init__(self):
        self.round_view = RoundView()
        self.round_manager = RoundManager()
        self.tournament_manager = TournamentManager()
        self.player_manager = PlayerManager()
        self.main_menu_view = MainMenuView()
        self.current_tournament = None

    def run(self, tournament_id):
        self.current_tournament = self.tournament_manager.get_tournament_by_id(tournament_id)
        current_round_number = self.current_tournament.number_of_current_round + 1

        print(f"Tournoi {self.current_tournament.name} à {self.current_tournament.location}")
        print(f"Du {self.current_tournament.date_start} au {self.current_tournament.date_end}")
        print()

        while True:
            self.round_view.display_main_menu(current_round_number)
            choice: int = self.round_view.request_user_choice()

            match choice:
                case 1:
                    self.start_round(tournament_id)
                case 2:
                    self.display_matches(tournament_id)
                case 3:
                    self.enter_scores(tournament_id)
                case 4:
                    break

    def start_round(self, tournament_id):
        if self.tournament_manager.check_tournament_finished(tournament_id):
            print("Tournoi terminé !")
            self.tournament_manager.display_final_rankings(tournament_id)
            return

        self.round_manager.create_round(tournament_id)
        self.round_manager.start_round(tournament_id)
        self.round_manager.generate_matches(tournament_id)

    def display_matches(self, tournament_id):
        matches = self.round_manager.get_current_round_matches(tournament_id)
        if matches:
            self.round_view.display_matches(matches)
        else:
            print("Aucun match généré pour le round actuel. Veuillez démarrer un round et générer les matchs.")

    def enter_scores(self, tournament_id):
        matches = self.round_manager.get_current_round_matches(tournament_id)
        if matches:
            choices: List[int] = []
            for i, match in enumerate(matches):
                choice = self.round_view.prompt_for_match_result(match, i + 1)
                choices.append(choice)
            self.round_manager.enter_scores(tournament_id, choices)
            self.round_manager.update_player_scores(tournament_id)
