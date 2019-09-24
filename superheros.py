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
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        pass

class Hero():
    def __init__(self, name, starting_health = 100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
      '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armor = []

    def add_ability(self, new_ability):
        ''' Add ability to abilities list '''
        self.abilities.append(new_ability)

    def get_abilities(self):
        for ability in self.abilities:
            print("{}'s abilities are {} ".format(self.name, ability))

    def attack():
        pass

    def defend(self, incoming_damage):
        pass

    def take_damage(self, damage):
        pass

    def is_alive():
        pass

    def fight(Hero):
        pass


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 50)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    print("Your new Hero is: {}".format(hero.name))
    print(hero.abilities)
    hero.get_abilities()

    #print(ability.name)
    print(ability.attack())
    print(hero.current_health)
