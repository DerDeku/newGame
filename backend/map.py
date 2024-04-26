from .room import Room, RoomType, Dir
from enum import Enum

class Map:
    def __init__(self,setX,setY,setDepth) -> None:
        self.sizeX = setX
        self.sizeY = setY
        self.depth = setDepth
        self.countRooms = self.sizeX * self.sizeY
        self.mainPathLength = self.sizeX - 1 + self.sizeY - 1 
        self.listRooms = [] # gonna be used as a 2D array, list of lists [[]]
        self.fillMapWithRooms()
        self.DEBUG_MAINROUTE = None

    def fillMapWithRooms(self) -> None:
        for column in range(self.sizeY):
            listRow = []
            for row in range(self.sizeX): 
                 listRow.append(Room(RoomType.EMPTY, row, column))
            self.listRooms.append(listRow)

    def room(self,x,y) -> Room:
        return self.listRooms[y][x]
    
    def getAdjacentRoom(self, room : Room, dir : Dir):
        x,y = room.getCoords()
        if dir == Dir.LEFT:
            return self.room(x-1,y)
        elif dir == Dir.RIGHT:
            return self.room(x+1,y)
        elif dir == Dir.ABOVE:
            return self.room(x,y-1)
        elif dir == Dir.BELOW:
            return self.room(x,y+1)
        
    def getAdjacentRooms(self,room : Room) -> dict[Room]:
        x,y = room.getCoords()
        rooms = dict()
        if x > 0:
            rooms.setdefault(Dir.LEFT, self.room(x-1,y))
        if x < self.sizeX-1:
            rooms.setdefault(Dir.RIGHT, self.room(x+1,y))
        if y > 0:
            rooms.setdefault(Dir.ABOVE, self.room(x,y-1))
        if y < self.sizeY-1:
            rooms.setdefault(Dir.BELOW, self.room(x,y+1))
        return rooms
        
    def setDepth(self, setDepth) -> None:
        self.depth = setDepth
    def getListRooms(self) -> list[list[Room]]:
        return self.listRooms
    def getDepth(self) -> int:
        return self.depth
    def getExit(self) -> Room:
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                room = self.listRooms[y][x]
                if room.getType() == RoomType.EXIT:
                    return room

    def getNewCoordinatesFromDir(self, x : int, y : int, dir : Dir) -> list[int, int]:
        listxy = [x,y]
        if dir == Dir.ABOVE:
            listxy[1] -= 1
        elif dir == Dir.BELOW:
            listxy[1] += 1
        elif dir == Dir.LEFT:
            listxy[0] -= 1
        elif dir == Dir.RIGHT:
            listxy[0] += 1
        return listxy
    
    def getMainPathLength(self) -> int:
        return self.mainPathLength