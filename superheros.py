import random

class Ability():
    def __init__(self, name, max_damage):
       '''Create Instance Variables:
          name:String
          max_damage: Integer
       '''
       self.name = name
       self.max_damage = max_damage

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        return random.randint(0, self.max_damage)

class Armor():
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        pass

class Hero():
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health

    def add_ability(Ability):
        pass

    def attack():
        pass

    def defend(incoming_damage):
        pass

    def take_damage(damage):
        pass

    def is_alive():
        pass

    def fight(Hero):
        pass


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
