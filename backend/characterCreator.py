from .player import Player
from .immersivePrint import iprint, dprint, Dialog
from . import immersivePrint

class CharacterCreator:
    def __init__(self, player : Player) -> None:
        self.player = player
    
    def startCreation(self):
        self.firstDialog()
        self.pickStats()
    
    def firstDialog(self):
        immersivePrint.skip = True
        iprint("Ahoy there, weary traveler, come closer, come closer")
        dprint(0.1)
        iprint("Ye look as though ye've been through the eye of a tempestuous storm.")
        iprint("But fear not, for fate has guided ye to this sacred spot.")
        iprint("Aye, ye be fortunate to cross paths with an old salt like meself.")
        iprint("Sit ye down by the hearth and listen to me tale,")
        iprint("a tale as old as the sea itself, a tale of adventure and mystery.")
        iprint("Ye can count yerself lucky, for not every soul be so fortunate,")
        iprint("to stumble upon these shores, washed up like a forgotten treasure.")
        # Beispiel-Nutzung
        root_dialog = Dialog()
        root_dialog.setQuestions("Wo bin ich?", "Wie heißt du?", "Weiter")
        root_dialog.setAnswers("Atlantis", "Albert")
        child_dialog = Dialog()
        child_dialog.setQuestions("Wie bin ich hier gelandet?", "Wie alt bist du?", "Weiter")
        child_dialog.setAnswers("bla bla bla", "bla bli blub")
        root_dialog.addChild(child_dialog)
        root_dialog.start()
        immersivePrint.skip = False
    
    def pickStats(self): #TODO big polish necessarry, just bare minimum
        print("1 - Choose to be an Assassin")
        print("2 - Choose to be a Warrior")
        print("3 - Choose to be a Mage")
        choice = 1 #TODO input()
        if choice == 1:
            self.player.setClass("Assassin")
            print("1 - Thief") #TODO show starter Runes
            print("2 - comming soon")
            print("3 - comming soon")
            choice = 1 #TODO input()
            if choice == 1:
                self.player.setSubClass("Thief")


        
