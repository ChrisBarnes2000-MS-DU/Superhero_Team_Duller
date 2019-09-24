class Ability():
    def __init__(self, name, max_damage):
       self.name = name
       self.max_damage = max_damage

    def attack(self):
        pass

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