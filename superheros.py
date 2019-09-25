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

    def __repr__(self):
        return "Ability: {}, max damage: {}".format(self.name, self.max_damage)

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

    def display_abilities(self):
        print("{}'s abilities are ".format(self.name), end="")
        for i, ability in enumerate(self.abilities):
            if i == len(self.abilities)-1:
                print("{}".format(ability.name), end="")
            else:
                print("{}, ".format(ability.name), end="")

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total:Int
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
          Armor: Armor Object
        '''
        self.armor.append(armor)

    def defend(self, incoming_damage):
        '''Runs `block` method on each armor.
            Returns sum of all blocks
        '''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        pass

    def is_alive(self):
        return self.current_health == 0

    def fight(Hero):
        pass


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging", 50)
    second_ability = Ability("Coding", 50)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(second_ability)
    print("Your new Hero is: {}".format(hero.name))
    print(hero.abilities)
    hero.display_abilities()

    #print(ability.name)
    print("\n{}".format(ability.attack()))
    print(hero.current_health)
