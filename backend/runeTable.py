from .rune import Rune
import logging

class RuneTable:
    def __init__(self) -> None:
        self.slotNumber = 3
        self.slots = [Rune]

    def replaceRune(self, rune) -> None:
        print("Rune Table ist full")
        print("replace Rune: " + rune.name + " with")
        for i in range(self.slotNumber):
            print(f"{i+1} - {self.slots[i].name}")
        choice = input()
        self.replaceSlotWithRune(choice-1, rune)

    def replaceSlotWithRune(self, slotNumber : int, rune : Rune) -> None:
        if slotNumber >= len(self.slots) and self.slots[slotNumber] is not None:
            oldRune = self.slots.pop(slotNumber)
            self.slots.insert(slotNumber, rune)
        else:
            self.slots.append(rune)
            logging.warning("placed rune in slot: " + len(self.slots)-1)
    
    def addRune(self, rune : Rune) -> None:
        if self.slotsNumber >= len(self.slots):
            self.slots.append(rune)
        else:
            logging.warning("rune table full, couldn't add rune")

    def notFull(self) -> bool:
        if len(self.slots) <= self.slotNumber:
            return True
        else:
            return False