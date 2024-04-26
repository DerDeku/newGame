from .map import Map
from .mapAlgo import MapAlgo

class MapFactory:
    def __init__(self) -> None:
        self.listMapsLevel1 : list[Map] = list() 
        self.mapAlgo = MapAlgo()
        

    def createLevel1(self,x,y,z) -> None:
        for i in range(z):
            map = Map(x,y,i)
            self.listMapsLevel1.append(map)
        for i, map in enumerate(self.listMapsLevel1): 
            self.listMapsLevel1[i] = self.mapAlgo.prepareAlgo(map)
    def nextStage(self, depth):
        map = self.listMapsLevel1[depth]
        self.listMapsLevel1[depth]= self.mapAlgo.nextStage(map)
    def getLevel1(self) -> list[Map]:
        return self.listMapsLevel1
    