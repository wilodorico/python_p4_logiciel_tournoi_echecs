from datetime import datetime

import pytest

from models.player_model import Player
from models.tournament_model import Tournament

# @pytest.fixture
# def my_fruit():
#     return Fruit("apple")

# @pytest.fixture
# def fruit_basket(my_fruit):
#     return [Fruit("banana"), my_fruit]


@pytest.fixture
def tournament():
    return Tournament(
        name="Tournament 1",
        location="Paris",
        description="This is a tournament",
        date_start=datetime.now(),
        date_end=datetime.now(),
    )


class Match:
    def __init__(
        self,
        player1: Player,
        player2: Player,
        score1: int,
        score2: int,
    ):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2


def test_tournament(tournament):
    t = tournament
    assert t.name == "Tournament 1"


def test_tournament_add_player(tournament):
    t = tournament
    p = Player(
        firstname="John",
        lastname="Doe",
        date_of_birth=datetime.now(),
        point=100,
        national_id="123456789",
    )
    p2 = Player(
        firstname="Jane",
        lastname="Doe",
        date_of_birth=datetime.now(),
        point=100,
        national_id="123456789",
    )
    p3 = Player(
        firstname="George",
        lastname="Doe",
        date_of_birth=datetime.now(),
        point=100,
        national_id="123456789",
    )
    p4 = Player(
        firstname="Ali",
        lastname="Doe",
        date_of_birth=datetime.now(),
        point=100,
        national_id="123456789",
    )
    t.add_player(p)
    assert len(t.players) == 1
    assert t.players[0].firstname == "John"

    t.add_player(p2)
    assert len(t.players) == 2
    assert t.players[1].firstname == "Jane"

    t.add_player(p3)
    assert len(t.players) == 3
    assert t.players[2].firstname == "George"

    t.add_player(p4)
    assert len(t.players) == 4
    assert t.players[3].firstname == "Ali"


def test_tournament_create_round(tournament):
    t = tournament
    p = Player(
        firstname="John",
        lastname="Doe",
        date_of_birth=datetime.now(),
        point=100,
        national_id="123456789",
    )
    p2 = Player(
        firstname="Jane",
        lastname="Doe",
        date_of_birth=datetime.now(),
        point=100,
        national_id="123456789",
    )
    p3 = Player(
        firstname="George",
        lastname="Doe",
        date_of_birth=datetime.now(),
        point=100,
        national_id="123456789",
    )
    p4 = Player(
        firstname="Ali",
        lastname="Doe",
        date_of_birth=datetime.now(),
        point=100,
        national_id="123456789",
    )
    t.add_player(p)
    t.add_player(p2)
    t.add_player(p3)
    t.add_player(p4)
    assert len(t.players) == 4
    assert t.players[0].firstname == "John"
    assert t.players[1].firstname == "Jane"
    assert t.players[2].firstname == "George"
    assert t.players[3].firstname == "Ali"

    t.create_round()
    assert len(t.rounds) == 1
    assert t.rounds[0].name == "Round 1"

    """
    je crée un tournoi
    
    Q : Je demande à ajouter des joueurs
    j'ajoute des joueurs en nombres pair
    
    J'affiche total joueurs enregistrés
    
    Q : Je demande à créer le premier round
    Q : je demande à générer les matchs
        Pour le round 1 les matchs sont aléatoires
    
    Q : je demande à commencer le Round 1
        J'affiche Round 1 commencé la date du jour + l'heure de début
    
    Q : je demande à terminer le Round 1
        J'affiche Round 1 terminé la date du jour + l'heure de fin
        
    Q : je demande à rentrer les scores des joueurs
        J'affiche le score des joueurs
        
    je génère le classement des joueurs par ordre decroissant
    
    
    
    """
