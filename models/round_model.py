import random
from datetime import datetime
from enum import Enum
from typing import List
from tinydb import TinyDB

from models.player_model import Player
from models.match_model import Match
from utils.rich_component import alert_message


class RoundStatus(Enum):
    CREATED = "Créé"
    STARTED = "En cours"
    FINISHED = "Terminé"


class Round:
    def __init__(self, name: str):
        self.name = name
        self.matches: list = []
        self.start_at: datetime = None
        self.end_at: datetime = None
        self.status: RoundStatus = RoundStatus.CREATED

    def __str__(self) -> str:
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "matches": self.matches,
            "start_at": self.start_at.strftime("%d-%m-%Y %H:%M:%S") if self.start_at else None,
            "end_at": self.end_at.strftime("%d-%m-%Y %H:%M:%S") if self.end_at else None,
            "status": self.status.value,
        }

    def start(self):
        self.start_at = datetime.now()

    def end(self):
        self.end_at = datetime.now()

    def is_running(self):
        return self.start_at

    def add_match(self, match: Match):
        self.matches.append(match.players)


class RoundManager:
    def __init__(self, db_path="data/tournaments/tournaments.json"):
        self.db = TinyDB(db_path, indent=4, ensure_ascii=False, encoding="utf-8")
        self.tournaments_table = self.db.table("tournaments")
        self.matches = []

    def start_round(self, tournament_id):
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if tournament["rounds"]:
            current_round = tournament["rounds"][-1]
        else:
            return alert_message("Aucun Round créé: Veuillez d'abord créer un Round", "red")

        if current_round["status"] == RoundStatus.CREATED.value:
            current_round["status"] = RoundStatus.STARTED.value
            current_round["start_at"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.tournaments_table.update(tournament, doc_ids=[tournament_id])
            return alert_message(f"{current_round['name']} démarrée avec succès !", "green")
        else:
            return alert_message(
                f"{current_round['name']} en cours ! Terminez le Round en saisissant les scores.", "deep_sky_blue1"
            )

    def create_round(self, tournament_id):
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            alert_message(f"Aucun tournoi trouvé avec l'ID: {tournament_id}", "red")
            return

        total_tournament_rounds = len(tournament["rounds"])

        if tournament["rounds"]:
            if (
                tournament["rounds"][-1]["status"] == RoundStatus.CREATED.value
                or tournament["rounds"][-1]["status"] == RoundStatus.STARTED.value
            ):
                return

        total_tournament_rounds += 1
        tournament["number_of_current_round"] = total_tournament_rounds
        new_round = Round(f"Round {total_tournament_rounds}")
        tournament["rounds"].append(new_round.to_dict())
        self.tournaments_table.update(tournament, doc_ids=[tournament_id])

        alert_message(f"{new_round.name} enregistré avec succès !", "green")

    def generate_matches(self, tournament_id):
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            alert_message(f"Aucun tournoi trouvé avec l'ID: {tournament_id}", "red")
            return

        players: List[Player] = tournament.get("players", [])
        max_players = tournament.get("max_players")

        if len(players) < max_players:
            alert_message(
                f"Veuillez enregistrer les {max_players} joueurs avant de créer des matchs", "deep_sky_blue1"
            )
            return

        current_round_number = len(tournament["rounds"])

        if current_round_number == 1:
            if (
                not tournament["rounds"][-1]["matches"]
                and tournament["rounds"][-1]["status"] == RoundStatus.STARTED.value
            ):
                self.matches = self.create_random_matches(players)
            else:
                return
        else:
            self.matches = self.create_matches_based_on_ranking(tournament, players)

        tournament["rounds"][-1]["matches"] = self.matches
        self.tournaments_table.update(tournament, doc_ids=[tournament_id])

        alert_message("Les matchs ont été générés avec succès !", "green")

    def create_random_matches(self, players: List[Player]):
        matches = []
        random.shuffle(players)

        for i in range(0, len(players) - 1, 2):
            player1 = players[i]
            player2 = players[i + 1]
            match = Match(
                player1["firstname"] + " " + player1["lastname"],
                0.0,
                player2["firstname"] + " " + player2["lastname"],
                0.0,
            )
            matches.append(match.players)

        if len(players) % 2 != 0:
            alert_message(
                f"Le joueur {players[-1]['firstname']} {players[-1]['lastname']} n'a pas d'adversaire pour ce round",
                "red",
            )

        return matches

    def create_matches_based_on_ranking(self, tournament, players: List[dict]):
        matches = []

        # Sort players by total score (from highest to lowest)
        players.sort(key=lambda player: player["point"], reverse=True)

        # Get pairs of players who have already played together
        already_played = self.get_already_played_pairs(tournament)

        # List of unmatched players in this round
        unpaired_players = players.copy()

        # As long as there are unpaired players
        while unpaired_players:
            player1 = unpaired_players.pop(0)  # Retrieve the first unmatched player

            # Search for an opponent with whom player1 has not yet played
            for i in range(len(unpaired_players)):
                player2 = unpaired_players[i]

                # Check whether the pair have played together before
                player1_name = f"{player1['firstname']} {player1['lastname']}"
                player2_name = f"{player2['firstname']} {player2['lastname']}"

                if (player1_name, player2_name) not in already_played:
                    # Create a new match pair
                    match = Match(
                        player1_name,
                        0.0,
                        player2_name,
                        0.0,
                    )
                    matches.append(match.players)

                    # Mark both players as paired for this round
                    unpaired_players.pop(i)  # Remove player2 from the unmatched list
                    break  # Exit the inner loop after finding an opponent for player1

        # If the logic is correct, there should never be any unmatched players.
        assert len(matches) == len(players) // 2, "Tous les joueurs n'ont pas été appariés correctement."

        return matches

    def get_already_played_pairs(self, tournament):
        """Returns a set of pairs of players who have already meet."""
        already_played = set()
        for round_data in tournament["rounds"]:
            for match in round_data["matches"]:
                player1_name = match[0][0]
                player2_name = match[1][0]
                already_played.add((player1_name, player2_name))
                already_played.add((player2_name, player1_name))
        return already_played

    def get_current_round_matches(self, tournament_id):
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            alert_message(f"Aucun tournoi trouvé avec l'ID: {tournament_id}", "red")
            return
        if not tournament["rounds"]:
            alert_message("Aucun Round créé: Veuillez d'abord créer un Round", "red")
            return

        current_round_number: int = tournament["number_of_current_round"]
        current_round = tournament["rounds"][current_round_number - 1]

        return current_round.get("matches", [])

    def enter_scores(self, tournament_id, choices):
        """Assigns match scores for the current round according to the user's choices."""
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            alert_message(f"Aucun tournoi trouvé avec l'ID: {tournament_id}", "red")
            return

        if not tournament["rounds"]:
            alert_message("Aucun Round créé: Veuillez d'abord créer un Round", "deep_sky_blue1")
            return

        current_round = tournament["rounds"][-1]

        if current_round["status"] != RoundStatus.STARTED.value:
            alert_message(
                f"Les scores ne peuvent être saisis que pour un round en cours. "
                f"{current_round['name']} n'est pas en cours.",
                "deep_sky_blue1",
            )
            return

        matches = current_round.get("matches", [])

        # Assign scores based on user choices
        for i, choice in enumerate(choices):
            match = matches[i]
            if choice == 1:
                self.set_match_result(match, 1.0, 0.0)
            elif choice == 2:
                self.set_match_result(match, 0.0, 1.0)
            elif choice == 3:
                self.set_match_result(match, 0.5, 0.5)

        # Update tournament with new scores
        current_round["matches"] = matches
        current_round["status"] = RoundStatus.FINISHED.value
        current_round["end_at"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.tournaments_table.update(tournament, doc_ids=[tournament_id])

        alert_message(f"Scores enregistrés pour {current_round['name']} et le round est maintenant terminé.", "green")

    def set_match_result(self, match, score1: float, score2: float):
        """Assigns scores to players in a match."""
        match[0][1] = score1
        match[1][1] = score2
        self.console.print(f"Scores mis à jour : {match[0][0]} ({score1}) - {match[1][0]} ({score2})")

    def update_player_scores(self, tournament_id):
        """Updates players' total points based on match results."""
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            alert_message(f"Aucun tournoi trouvé avec l'ID: {tournament_id}", "red")
            return

        # Initialize or reset player scores
        player_points = {player["id"]: 0.0 for player in tournament.get("players", [])}

        # Scroll through each round and match to calculate players' total scores
        for round_data in tournament["rounds"]:
            for match in round_data["matches"]:
                # Extract player IDs and their respective scores
                player1_name = match[0][0]
                player1_score = match[0][1]
                player2_name = match[1][0]
                player2_score = match[1][1]

                # Find players by full name
                player1 = next(
                    (
                        player
                        for player in tournament["players"]
                        if f"{player['firstname']} {player['lastname']}" == player1_name
                    ),
                    None,
                )
                player2 = next(
                    (
                        player
                        for player in tournament["players"]
                        if f"{player['firstname']} {player['lastname']}" == player2_name
                    ),
                    None,
                )

                if player1:
                    player_points[player1["id"]] += player1_score
                if player2:
                    player_points[player2["id"]] += player2_score

        # Update players' points in the tournament
        for player in tournament["players"]:
            player["point"] = player_points[player["id"]]

        # Save updated data in the database
        self.tournaments_table.update(tournament, doc_ids=[tournament_id])
        alert_message("Les scores des joueurs ont été mis à jour avec succès.", "green")
