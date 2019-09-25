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
        return random.randint(0, self.max_block)

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
                print("& {} \n".format(ability.name), end="")
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
        if len(self.armor) == 0:
            print("You have no armor on, so 0 defence is provided")
            return 0
        else:
            for armor in self.armor:
                print("{} armor has {} defence".format(armor.name, armor.max_block))
                total_block += armor.block()
            print("total block/defence {}".format(total_block))
            return total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.'''
        print ("incoming damage {}".format(damage))
        defence = self.defend(damage)
        defended_damage = (damage - defence)
        print("You take", defended_damage, "damage")
        self.current_health -= defended_damage

    def get_current_health(self):
        print("Your hero's current hp is: {}".format(hero.current_health))

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.'''
        if self.current_health > 0: return True
        else: return False

    def fight(Hero):
        pass


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Iron Bat", 200)
    print("Your new Hero is: {} starting with: {} hp\n".format(
        hero.name, hero.current_health))

    hero.add_ability(Ability("Lazar Eyes", 500))
    hero.add_ability(Ability("Super Speed", 50))
    hero.display_abilities()
    print(hero.abilities)

    hero.get_current_health()
    print("\nIs the hero still alive: {}".format(hero.is_alive()))
    hero.take_damage(50)
    hero.get_current_health()
    print("\nIs the hero still alive: {}".format(hero.is_alive()))

    print("\nputting on chest plate for protection")
    hero.add_armor(Armor("Chest Plate", 60))
    hero.take_damage(50)
    hero.get_current_health()
    print("\nIs the hero still alive: {}".format(hero.is_alive()))
