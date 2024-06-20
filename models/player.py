class Player:
    def __init__(self, firstname, lastname, point):
        self.firstname = firstname
        self.lastname = lastname
        self.point = point

    def __str__(self) -> str:
        return f"{self.firstname}.{self.lastname}"

    def __repr__(self) -> str:
        return f"Player(firstname={self.firstname}, lastname={self.lastname}, point={self.point})"
