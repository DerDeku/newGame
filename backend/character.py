from . import ability

class Character:
    def __init__(self):
        self.hp = 50
        self.mana = 100
        self.name : str
        self.damage = 5
    def dealDamage(self, obj):
        obj.takeDamage(self.damage)
    def takeDamage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.die()
    def die(self):
        print(f"{self.name} died")
