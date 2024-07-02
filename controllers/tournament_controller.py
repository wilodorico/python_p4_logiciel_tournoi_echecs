# Creer le tournoi

# tournament = ...
# self.name = name
#         self.location = location
#         self.description = description
#         self.date_start = date_start
#         self.date_end = date_end

#         self.number_of_round: int = 4
#         self.number_of_current_round: int = 1
#         self.rounds: List[Round] = []
#         self.players: List[Player] = []


# Ajouter les players au tournoi
# Tournament.add_player(player_id=1)
# Tournament.add_player(player_id=2)
# Tournament.add_player(player_id=3)
# Tournament.add_player(player_id=4)


# Créer Round
#
# Tournament.create_round()  -> id de round 1

# attente de resultats

from models.tournament_model import Tournament
from views.tournament_view import TournamentView


class TournamentController:

    def __init__(self):
        self.tournament_view = TournamentView()

    def create_tournament(self):
        name, location, description, date_start, date_end = (
            self.tournament_view.get_tournament_info()
        )
        tournament = Tournament(name, location, description, date_start, date_end)

        self.tournament_view.display_tournament_info(tournament)

        self.tournament_view.display_tournament_menu()

        print(tournament)
