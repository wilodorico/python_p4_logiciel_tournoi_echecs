import datetime


class Round:
    def __init__(self, name: str):
        self.name = name
        self.matchs: list = []
        self.start_at: datetime = None
        self.end_at: datetime = None

    def __str__(self) -> str:
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "matchs": self.matchs,
            "start_at": self.start_at.strftime("%d-%m-%Y"),
            "end_at": self.end_at.strftime("%d-%m-%Y"),
        }

    def start(self):
        self.start_at = datetime.now()

    def end(self):
        self.end_at = datetime.now()

    def is_running(self):
        if self.start_at:
            return True
        return False
