from .ability import Abilities
from .rarities import Rarity
from .rune import Rune
from . import logConfig
import random
import json

logger = logConfig.configure_logger()

class RuneFactory:
    def __init__(self, abilities : Abilities) -> None:
        self.abilities = abilities
        self.dictRawClassRunesAssassin = dict()
        self.dictRawRunesAssassin = dict()
        self.listRawClassRunesWarrior = None
        self.listRawRunesWarrior = None
        self.listRawClassRunesMage = None
        self.listRawRunesMage = None
        self.listOfAbilitesWithTag = []
        self.listClassRunesAssassin = []

    def loadRunesFromJson(self) -> None:
        try: 
            with open('abilityRunes.json') as f:
                dictRunes = json.load(f)
                for dictRuneName, dictRune in dictRunes['Assassin'].items():
                    logger.info("runes loaded:\n")
                    logger.info(f"\t{dictRune}")
                    if dictRune["type"] == "class":
                        self.dictRawClassRunesAssassin.setdefault(dictRuneName, dictRune)
                    elif dictRune["type"] == "random":
                        self.dictRawRunesAssassin.setdefault(dictRuneName, dictRune)
        except Exception as e:
            logger.error("An error occurred:", e)

    def makeClassRune(self) -> Rune:
        for runeName, runeBluePrint in self.dictRawClassRunesAssassin.items():
            self.listClassRunesAssassin.append(self.makeRune(runeName, runeBluePrint))
        
    def makeRune(self, runeName : str, runeBluePrint : Rune):
        rune = Rune(runeName,runeBluePrint["rarity"])
        for abilityName, ability in self.abilities.dictAssassinAbilities.items():
            if abilityName in runeBluePrint["abilities"]:
                rune.addAbility(abilityName, ability)
        return rune
        
    def createRune(self, name : str, rarity : Rarity) -> Rune:
        rune = Rune(name, rarity)
        for rawRuneName, rawRune in self.dictRawRunesAssassin.items():
            if rawRuneName == name:            
                dictAbilities = self.getDictFromTags(rawRune["tags"])
                numberAbilities = rune.getValueOfRarity()
                rune.addNumberOfRandomAbilities(dictAbilities, numberAbilities)

        return rune

    def getDictFromTags(self, tags : list[str]) -> dict:
        dictOfAbilitesWithTags = dict()
        for dictAbilityName, dictAbility in self.abilities.dictAssassinAbilities.items():
            for tagAbility in dictAbility["tags"]:
                if tagAbility in tags and dictAbilityName not in dictOfAbilitesWithTags:
                    dictOfAbilitesWithTags.setdefault(dictAbilityName,dictAbility)
        return dictOfAbilitesWithTags

    