from models.player_model import Player


class Match:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

        self.score1 = 0
        self.score2 = 0

    def set_winner(self, player: Player):
        if player == self.player1:
            self.score1 += 1
            self.score2 += 0

        elif player == self.player2:
            self.score1 += 0
            self.score2 += 1

    def set_draw(self):
        self.score1 += 0.5
        self.score2 += 0.5

    def is_done(self) -> bool:
        pass
