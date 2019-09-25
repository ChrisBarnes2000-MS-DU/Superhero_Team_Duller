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
        print("Your new Hero is: {} starting with: {} hp\n".format(self.name, self.current_health))

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
            print("{} has no armor on, so 0 defence is provided".format(self.name))
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
        print("{} takes {} damage".format(self.name, defended_damage))
        self.current_health -= defended_damage
        print("{} is now at {}/{} hp".format(self.name, self.current_health, self.starting_health))

    def get_current_health(self):
        print("Your hero's current hp is: {}".format(hero.current_health))

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.'''
        if self.current_health > 0:
            print("{} is still alive".format(self.name))
            return True
        else: 
            print("{} has died".format(self.name))
            return False

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.'''
        """This function will need to take into account the possibility that both heroes may not have abilities and therefore will do no damage.
        --check if to see that at least one hero has an ability. If no abilities exist print out "Draw"
        """
        if len(self.abilities) == 0 or len(opponent.abilities) == 0: print("Draw")
        else:
            winner = ""
            fighting = True
            while (fighting):
                print("\n\t___First Attacker___\n")
            
                print("{} attacks {}".format(self.name, opponent.name))
                opponent.take_damage(self.attack())
                fighting = opponent.is_alive()

                print("\n\t___Second Attacker___\n")

                print("{} attacks {}".format(opponent.name, self.name))
                self.take_damage(opponent.attack())
                fighting = self.is_alive()
            '''Check to see whose left alive and return the winner'''
            if (not fighting and opponent.is_alive()):    
                winner = ("{} won!".format(opponent.name))
            else:
                winner = ("{} won!".format(self.name))
            print("\n\n{} & {}, winner: {}".format(self.is_alive(), opponent.is_alive(), winner))
            return winner

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    print("\t\t______TESTING______\n")
    
    print("______First Hero______")
    hero = Hero("Iron Bat", 200)
    print("______First Hero's Abilities______")
    hero.add_ability(Ability("Lazar Eyes", 100))
    hero.add_ability(Ability("Super Speed", 50))
    hero.add_ability(Ability("Strength", 30))
    hero.display_abilities()
    print(hero.abilities)

    #print("\nputting on chest plate for protection")
    #hero.add_armor(Armor("Chest Plate", 60))

    print()

    print("______Second Hero______")
    opponent = Hero("Strange Sponge", 200)
    print("______Second Hero's Abilities______")
    opponent.add_ability(Ability("Soapy", 50))
    opponent.add_ability(Ability("Gross food", 150))
    opponent.display_abilities()
    print(opponent.abilities)

    print("\t\t______FIGHT TESTING______\n")
    hero.fight(opponent)
