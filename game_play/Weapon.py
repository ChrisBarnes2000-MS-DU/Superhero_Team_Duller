import random
import game_play.Ability as Ability

class Weapon(Ability):
    def __init__(self, name, max_damage):
        super().__init__(name, max_damage)

    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon. """
        return random.randint((self.max_damage//2), self.max_damage)

    def __repr__(self):
        return "Weapon: {}, max damage: {}".format(self.name, self.max_damage)
