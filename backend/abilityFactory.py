from .ability import Abilities
import json
from . import logConfig


class AbilityFactory:
    def __init__(self) -> None:
        self.allRunes = None
        self.listNamesAssassinAbilities = []
        self.dictAssassinAbilities = []

    def loadAbilitiesFromJson(self):
        try:
            with open('backend\\abilities.json') as f:
                dictAbilities = json.load(f)
                self.dictAssassinAbilities = dictAbilities["Assassin"]
                for dictAssassinAbilityName in dictAbilities['Assassin']:
                    self.listNamesAssassinAbilities.append(dictAssassinAbilityName)

        except Exception as e:
            print("An error occurred:", e)