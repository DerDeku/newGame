from enum import Enum

class Rarity(Enum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5

    @classmethod
    def stringToRarity(cls, rarity_string):
        return {
            "COMMON": cls.COMMON,
            "UNCOMMON": cls.UNCOMMON,
            "RARE": cls.RARE,
            "EPIC": cls.EPIC,
            "LEGENDARY": cls.LEGENDARY
        }.get(rarity_string)