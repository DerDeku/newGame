from ability import Abilities

class AbilityHandler:
    def __init__(self) -> None:
        pass

    def triggerEffect(self, target):
        for effect in self.effects:
            if effect['type'] == 'condition':
                if effect['condition'] == 'poisoned' and target.is_poisoned():
                    if effect['action'] == 'deal_remaining_damage':
                        remaining_damage = target.get_remaining_poison_damage()
                        target.take_damage(remaining_damage)
                        print(f"{target.name} has been cleansed of poison, taking {remaining_damage} damage.")