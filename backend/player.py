from .character import Character
from .runeTable import RuneTable
from .movement import Movement

class Player(Character):
    def __init__(self):
        super().__init__()
        self.movementHandler = Movement()
        self.name = "player"
        self.runeTable = RuneTable()
        self.starterClass = None
        self.subClass = None
        runes = {}

    def setClass(self, newClass):
        self.starterClass = newClass

    def addRune(self, rune):
        if self.runeTable.notFull():
            self.runeTable.addRune(rune)
        else:
            self.runeTable.replaceRune(rune)
    
    def setSubClass(self, newSubClass):
        self.subClass = newSubClass