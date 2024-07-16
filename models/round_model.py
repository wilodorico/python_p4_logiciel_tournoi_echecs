from ast import Match
from typing import List


class Round:
    def __init__(
        self,
        id: int,
        name: str,
    ):
        self.id = id
        self.name = name

    def get_matchs(self) -> List[Match]:
        pass  # return matchs filter by round id

    def start_round(self):
        # start_date = datetime.now()
        pass

    def end_round(self):
        # end_date = datetime.now()
        pass

    def set_scores_round(self) -> List[int]:
        # parcourir les matchs et fournir le score
        pass
