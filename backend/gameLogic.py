from backend import player, enemy, character, ability, runeFactory, rune, characterCreator
from .rarities import Rarity
from .combat import Combat
from .runeHandler import RuneHandler
from .mapFactory import MapFactory
from .abilityFactory import AbilityFactory

class GameLogic:
    def __init__(self) -> None:
        self.abilityHandler = ability.Abilities()
        self.abilityFactory = AbilityFactory()
    
        self.abilityFactory.loadAbilitiesFromJson()
        print(self.abilityFactory.dictAssassinAbilities)
        self.runeHandler = RuneHandler()
        self.runeMaker = runeFactory.RuneFactory(self.abilityFactory)
        self.runeMaker.loadRunesFromJson()
        self.runeMaker.makeClassRune()
        self.rune1 = self.runeMaker.createRune("starter combo Rune",Rarity.COMMON)
        self.mainCharacter = player.Player()
        self.characterCreation = characterCreator.CharacterCreator(self.mainCharacter)
        self.characterCreation.startCreation()
        #characterCreation.handoverRunes() #TODO
        self.enemy1 = enemy.Enemy()
        self.mapFactory = MapFactory()
        self.mapFactory.createLevel1(5,5,30)
        #level1 = mapFactory.getLevel1()
        self.combat = Combat(self.mainCharacter, [self.enemy1])
        print("blub")
