from .rarities import Rarity
import random

class Rune:
    def __init__(self, name, rarity):
        self.name = name
        if isinstance(rarity, str):
            self.rarity = Rarity.stringToRarity(rarity)
        else:
            self.rarity = rarity
        self.__dictRarities__= {"COMMON" : 2,
                                "UNCOMMON": 3,
                                "RARE": 4,
                                "EPIC": 5,
                                "LEGENDARY": 6}
        self.dictAbilities = dict()

    def addAbility(self,abilityName : str, ability : dict):
        self.dictAbilities.setdefault(abilityName, ability)

    def setRarity(self, rarity : Rarity):
        self.rarity = rarity

    def getValueOfRarity(self):
        return self.__dictRarities__[self.rarity.name]
    
    def addNumberOfRandomAbilities(self, dictAbilities : dict, number : int) -> None:
        for i in range(number):
            if len(dictAbilities) > 1:
                random_key = random.choice(list(dictAbilities.keys()))
                random_ability = dictAbilities.pop(random_key)
                self.dictAbilities.setdefault(random_key, random_ability)
            else:
                print("not enough abilities with tag")
                break
        