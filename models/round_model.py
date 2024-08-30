import random
from datetime import datetime
from enum import Enum
from typing import List
from tinydb import TinyDB

from models.player_model import Player
from models.match_model import Match


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
            return print("Aucun Round créé: Veuillez d'abord créer un Round")

        if current_round["status"] == RoundStatus.CREATED.value:
            current_round["status"] = RoundStatus.STARTED.value
            current_round["start_at"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.tournaments_table.update(tournament, doc_ids=[tournament_id])
            return print(f"{current_round['name']} démarrée avec succès !")
        else:
            return print(f"{current_round['name']} déjà en cours")

    def create_round(self, tournament_id):
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            print(f"Aucun tournoi trouvé avec l'ID: {tournament_id}")
            return

        total_tournament_rounds = len(tournament["rounds"])

        if tournament["rounds"]:
            if (
                tournament["rounds"][-1]["status"] == RoundStatus.CREATED.value
                or tournament["rounds"][-1]["status"] == RoundStatus.STARTED.value
            ):
                return print(f"Round n°{total_tournament_rounds} déjà créée ou en cours")

        total_tournament_rounds += 1
        tournament["number_of_current_round"] = total_tournament_rounds
        new_round = Round(f"Round {total_tournament_rounds}")
        tournament["rounds"].append(new_round.to_dict())
        self.tournaments_table.update(tournament, doc_ids=[tournament_id])

        print(f"{new_round.name} enregistré avec succès !")

    def generate_matches(self, tournament_id):
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            print(f"Aucun tournoi trouvé avec l'ID: {tournament_id}")
            return

        players: List[Player] = tournament.get("players", [])
        max_players = tournament.get("max_players")

        if len(players) < max_players:
            print(f"Veuillez enregistrer les {max_players} joueurs avant de créer des matchs")
            return

        current_round_number = len(tournament["rounds"])

        if current_round_number == 1:
            if (
                not tournament["rounds"][-1]["matches"]
                and tournament["rounds"][-1]["status"] == RoundStatus.STARTED.value
            ):
                self.matches = self.create_random_matches(players)
            else:
                return print("Les matchs sont déjà générés, terminez le Round en saisissant les scores")
        else:
            self.matches = self.create_rank_based_matches(tournament, players)

        tournament["rounds"][-1]["matches"] = self.matches
        self.tournaments_table.update(tournament, doc_ids=[tournament_id])

        print("Les matchs ont été générés avec succès !")

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
            print(f"Le joueur {players[-1]['firstname']} {players[-1]['lastname']} n'a pas d'adversaire pour ce round")

        return matches

    def create_rank_based_matches(self, tournament, players: List[Player]):
        matches = []
        # Tri des joueurs par score total
        players.sort(key=lambda player: player["point"], reverse=True)
        already_played = self.get_already_played_pairs(tournament)

        for i in range(0, len(players) - 1, 2):
            player1 = players[i]
            for j in range(i + 1, len(players)):
                player2 = players[j]
                if (player1["id"], player2["id"]) not in already_played and (
                    player2["id"],
                    player1["id"],
                ) not in already_played:
                    match = Match(
                        player1["firstname"] + " " + player1["lastname"],
                        0.0,
                        player2["firstname"] + " " + player2["lastname"],
                        0.0,
                    )
                    matches.append(match.players)
                    # players.pop(j)  # Retirer player2 pour éviter les doublons
                    break

        if len(players) % 2 != 0:
            print(f"Le joueur {players[-1]['firstname']} {players[-1]['lastname']} n'a pas d'adversaire pour ce round")

        return matches

    def get_already_played_pairs(self, tournament):
        """Returns a set of pairs of players who have already met."""
        already_played = set()
        for round_data in tournament["rounds"]:
            for match in round_data["matches"]:
                player1_id = match[0][0]
                player2_id = match[1][0]
                already_played.add((player1_id, player2_id))
        return already_played

    def get_current_round_matches(self, tournament_id):
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            print(f"Aucun tournoi trouvé avec l'ID: {tournament_id}")
            return
        if not tournament["rounds"]:
            print("Aucun Round créé: Veuillez d'abord créer un Round")
            return
        current_round = tournament["rounds"][-1]
        current_round_number = len(tournament["rounds"])

        if current_round["status"] != RoundStatus.STARTED.value:
            return print(f"Les scores du Round n°{current_round_number} ont déjà été enregistrés.")

        return current_round.get("matches", [])

    def enter_scores(self, tournament_id, choices):
        """Assigns match scores for the current round according to the user's choices."""
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            print(f"Aucun tournoi trouvé avec l'ID: {tournament_id}")
            return

        if not tournament["rounds"]:
            print("Aucun Round créé: Veuillez d'abord créer un Round")
            return

        current_round = tournament["rounds"][-1]

        if current_round["status"] != RoundStatus.STARTED.value:
            print(
                f"Les scores ne peuvent être enregistrés que pour un round en cours. {current_round['name']} n'est pas en cours."
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

        print(f"Scores enregistrés pour {current_round['name']} et le round est maintenant terminé.")

    def set_match_result(self, match, score1: float, score2: float):
        """Assigns scores to players in a match."""
        match[0][1] = score1
        match[1][1] = score2
        print(f"Scores mis à jour : {match[0][0]} ({score1}) - {match[1][0]} ({score2})")

    def update_player_scores(self, tournament_id):
        """Updates players' total points based on match results."""
        tournament = self.tournaments_table.get(doc_id=tournament_id)
        if not tournament:
            print(f"Aucun tournoi trouvé avec l'ID: {tournament_id}")
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
        print("Scores des joueurs mis à jour avec succès.")
