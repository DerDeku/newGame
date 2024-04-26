from .character import Character

class Enemy(Character):
    def __init__(self):
        super().__init__()
        self.name = "enemy1"
        