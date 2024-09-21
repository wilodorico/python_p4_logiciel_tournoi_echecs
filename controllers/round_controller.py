from typing import List
from models.player_model import PlayerManager
from models.round_model import RoundManager
from models.tournament_model import TournamentManager
from utils.rich_component import alert_message
from views.main_menu_view import MainMenuView
from views.round_view import RoundView
from views.tournament_view import TournamentView
from rich.console import Console


class RoundController:
    """
        Controller class responsible for managing rounds within a tournament.

        This class handles the creation and management of rounds, including starting rounds,
        displaying match details, entering match results, and updating player scores.

        Attributes:
        ----------
        round_view : RoundView
            The view responsible for displaying round-related information and menus.
        round_manager : RoundManager
            The manager responsible for handling round data and operations.
        tournament_manager : TournamentManager
            The manager responsible for handling tournament data and operations.
        tournament_view : TournamentView
            The view responsible for displaying tournament-related information.
        player_manager : PlayerManager
            The manager responsible for handling player data and operations.
        main_menu_view : MainMenuView
            The view responsible for displaying the main menu.
        console : Console
            A Rich console instance used to display formatted text.

        Methods:
        -------
        run(tournament_id)
            Manages the round operations, including starting a round, displaying matches,
            and entering match results.

        start_round(tournament_id)
            Starts a new round for the given tournament if the tournament is not finished.
            Generates matches for the new round.

        display_matches(tournament_id)
            Displays the matches of the current round for the given tournament.

        enter_scores(tournament_id)
            Prompts the user to enter match results for the current round and updates player scores.
    """

    def __init__(self):
        self.round_view = RoundView()
        self.round_manager = RoundManager()
        self.tournament_manager = TournamentManager()
        self.tournament_view = TournamentView()
        self.player_manager = PlayerManager()
        self.main_menu_view = MainMenuView()
        self.console = Console()

    def run(self, tournament_id):
        current_tournament = self.tournament_manager.get_tournament_by_id(tournament_id)
        current_round_number = current_tournament["number_of_current_round"] + 1

        alert_message(
            f"Tournoi {current_tournament["name"]} du {current_tournament["date_start"]} "
            f"au {current_tournament["date_end"]}",
            "deep_sky_blue1",
        )

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
        if self.tournament_manager.is_tournament_finished(tournament_id):
            alert_message("Tournoi terminé !", "deep_sky_blue1")
            self.tournament_manager.display_final_rankings(tournament_id)
            return

        players = self.round_manager.get_players_tournament(tournament_id)
        if players:
            self.round_manager.create_round(tournament_id)
            self.round_manager.start_round(tournament_id)
            self.round_manager.generate_matches(tournament_id)
            self.display_matches(tournament_id)
        else:
            alert_message("Veuillez enregistrer les joueurs au tournoi", "red")

    def display_matches(self, tournament_id):
        matches = self.round_manager.get_current_round_matches(tournament_id)
        if matches:
            self.round_view.display_matches(matches)

    def enter_scores(self, tournament_id):
        matches = self.round_manager.get_current_round_matches(tournament_id)
        if matches:
            choices: List[int] = []
            for i, match in enumerate(matches):
                choice = self.round_view.prompt_for_match_result(match, i + 1)
                choices.append(choice)
            self.round_manager.enter_scores(tournament_id, choices)
            self.round_manager.update_player_scores(tournament_id)
