import subprocess
import sys
from backend.mapAlgo import MapAlgo
from backend.gameLogic import GameLogic 

class SubprocessManager:
    def __init__(self, backend : GameLogic = None) -> None:

        self.level = 0
    def call():
        result = subprocess.run(['python', '../frontend/main.py'], capture_output=True, text=True)
    def startBackend(self):
        self.backend = GameLogic()
    def getMapFrom(self, mapDepth : int = 0 ,level : int = 0 ):
        return self.backend.mapFactory.listMapsLevel1[mapDepth]
    def getMap(self, mapDepth):
        return self.backend.mapFactory.listMapsLevel1[mapDepth]
    def proceedAlgo(self, mapDepth : int = 0, level : int = 0) -> None:
        self.backend.mapFactory.nextStage(mapDepth)
