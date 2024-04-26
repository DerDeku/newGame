from .map import Map, Dir
from .room import Room, RoomType
import random
class MapAlgo:
    def __init__(self) -> None:
        self.stage = 1
        #for y in range(map.sizeY):
            #    for x in range(map.sizeX):
    def prepareAlgo(self, map : Map) -> Map:
        for column in range(map.sizeY):
            for row in range(map.sizeX):
                map.listRooms[column][row].setType(RoomType.EMPTY)
        return map
    def nextStage(self, map : Map) -> None:
        
        if self.stage == 1:
            return self.stage1(map)
        elif self.stage == 2:
            return self.stage2(map)
        elif self.stage == 3:
            return self.stage3(map)

    def stage1(self, map : Map) -> None:
        def doorAlgo(room : Room, pathLength : int, mainPath : list) -> None:
            dictAdjacentRooms = map.getAdjacentRooms(room)
            emptyRooms = 0
            for i in range(4):
                i = Dir(i) 
                if i in dictAdjacentRooms:
                    if dictAdjacentRooms[i].getType() != RoomType.EMPTY or dictAdjacentRooms[i].hasDoor(): #TODO Does this work?
                        dictAdjacentRooms.pop(i)

            listOfChoices = []
            for direction in dictAdjacentRooms:
                listOfChoices.append(Dir(direction))
            if len(listOfChoices) == 0:
                #go here if algo found itself in dead end and fix it by going one step back
                opDir = mainPath.pop().opposite()
                room.mainPathLength = pathLength
                pathLength -= 1
                doorAlgo(map.getAdjacentRoom(room,opDir), pathLength,mainPath)
                return map
                
            dir = Dir(random.choice(listOfChoices))
            room.makeDoor(dir)
            mainPath.append(dir)
            nextRoom = map.getAdjacentRoom(room,dir) 
            nextRoom.makeDoor(dir.opposite())     
            room.mainPathLength = pathLength
            pathLength += 1
            if len(mainPath) < map.mainPathLength:
                doorAlgo(nextRoom, pathLength, mainPath)
            else:
                nextRoom.setType(RoomType.EXIT)
                nextRoom.mainPathLength = pathLength
                return map

        mainPath = list() #list of Dir
        entrance = map.room(0,0)
        entrance.setType(RoomType.ENTRANCE)
        pathLength = 0
        doorAlgo(entrance, pathLength, mainPath)
        map.DEBUG_MAINROUTE = mainPath
        self.stage = 2
        return map

    def stage2(self, map) -> None:
        def doorAlgo(room : Room, cameFrom : Dir,  isDiscover : bool, pathLength : int) -> None:
            def checkAdjacentRooms(checkRoom : Room) -> list[Dir]:
                listDir = []
                listDiscoverDir = []
                dictAdjacentRooms = map.getAdjacentRooms(checkRoom)
                for inDir in dictAdjacentRooms:
                    adjRoom = Room(dictAdjacentRooms[inDir]) #TODO remove explicit type change
                    if not room.hasDoor():
                        isDiscover = True
                        if pathLength < map.getMainPathLength():
                            nextRoom = map.getAdjacentRoom(room, inDir)
                            room.makeDoor(inDir)
                        nextRoom.makeDoor(inDir.opposite())
                        checkAdjacentRooms(nextRoom)


                    else: #eig not discover mode
                        listDirDoors = room.getDoors()
                        if len(listDirDoors) == 1:
                            self.stage = 3
                            return 
                        
                    dir = Dir(random.choice(listDirDoors))
                    #TODO IDKKKKKK wut d fq i jeg ga nix me

                    


            def discover():
                pass
            def retrace():
                pass

            #start of func
            pathLength += 1
            #check => discover/retrace/stop
            listDir, isDiscover = checkAdjacentRooms(room)
            if isDiscover and len(listDir) > 0 and not pathLength > map.getMainPathLength():
                discover()
            elif not isDiscover and len(listDir) > 0 and not pathLength > map.getMainPathLength() :
                retrace()
            else:
                return 3

            exit = map.getExit()
            dirGoto = exit.getDoors()[0]
            room = map.getAdjacentRoom(exit, dirGoto)
            doorAlgo(room, dirGoto, False, pathLength=0)
        

    def stage3(self):
        pass 



        # stage1()
        #stage = 2
        #while True:
        #   if stage == 2:
        #       stage = stage2()
        #   elif stage == 3:
        #       stage = stage3()
        #   elif stage == 0:
        #       break

        # return map
