from enum import Enum

                #       Horizontale Wände:
                #       
                #       "─" (U+2500) - Horizontale Linie
                #       "-" (U+002D) - Einfacher Bindestrich
                #       "=" (U+003D) - Gleichheitszeichen
                #       Vertikale Wände:
                #       
                #       "│" (U+2502) - Vertikale Linie
                #       "|" (U+007C) - Senkrechter Strich
                #       Ecken:
                #       
                #       "┌" (U+250C) - Obere linke Ecke
                #       "┐" (U+2510) - Obere rechte Ecke
                #       "└" (U+2514) - Untere linke Ecke
                #       "┘" (U+2518) - Untere rechte Ecke
                #       Eingang: "⮌"
                #       Ausgang: "⮎"
                #       Kampf: "⚔"
                #       Bosskampf: "⚡"
                #       Schatz: "💰"

class RoomType(Enum):
    ENTRANCE = "⮎"
    EXIT = "⮌"
    FIGHT = "⚔"
    BOSSFIGHT = "⚡"
    TREASSURE = "💰"
    EMPTY = " "
    WALL_HORIZONTAL = "■"
    WALL_VERTICAL = "■"
    WALL_CORNER = "■"

    @classmethod
    def doSomething():
        pass

class Dir(Enum):
    LEFT = 0
    RIGHT = 1
    ABOVE = 2
    BELOW = 3
   
    def opposite(self):
        opposites = {
            Dir.LEFT : Dir.RIGHT,
            Dir.RIGHT : Dir.LEFT,
            Dir.ABOVE : Dir.BELOW,
            Dir.BELOW : Dir.ABOVE
        }
        
        return opposites.get(self)

class Room:
    def __init__(self,type = None, x = None,  y = None) -> None:
        self.type = type # RommType
        self.listOfDoors = list() #list of Dir(ections)
        self.x = x
        self.y = y
        self.mainPathLength = 0
    def printContent(self):
        print(f"<startContent> {self.listOfDoors}")
    def hasDoor(self) -> bool:
        if len(self.listOfDoors) > 0:
            return True
        else:
            return False
    def getDoors(self) -> list[Dir]:
        return self.listOfDoors
    def getCoords(self) -> list[int]:
        return [self.x,self.y]    
    def setType(self, type) -> None:
        self.type = type
    def getType(self) -> RoomType:
        return self.type
    def makeDoor(self, dir : Dir):
        self.listOfDoors.append(dir)
    def getMainPathLength(self) -> int:
        return self.mainPathLength
    def setMainPathLength(self, value : int) -> None:
        self.mainPathLength = value