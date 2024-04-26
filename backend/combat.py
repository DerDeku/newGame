from .character import Character
from .player import Player
from .enemy import Enemy
from .ability import Abilities

class Combat:
    def __init__(self, player : Player, listEnemies : list[Enemy]):
        self.player = player
        self.listEnemies = listEnemies
        self.listOrder = []

    def startCombat(self):
        self.getOrder()
        activeCharacter = self.nextInOrder()
        if isinstance(activeCharacter, Player):
            self.playersTurn()
        elif isinstance(activeCharacter, Enemy):
            self.enemyTurn(activeCharacter)

    def playersTurn(self):
        pass

    def enemyTurn(self, enemy):
        pass

    def getOrder(self):
        pass


    def nextInOrder(self) -> Character:
        character = self.listOrder.pop(0)
        self.listOrder.append(character)
        return character