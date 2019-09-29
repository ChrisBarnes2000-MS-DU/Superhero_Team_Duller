import random
import game_play.Ability as Ability
import game_play.Armor as Armor
import game_play.Team as Team
import game_play.Weapon as Weapon

class Hero():
    def __init__(self, name, starting_health=100, deaths=0, kills=0):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer'''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armor = []
        self.kills = kills
        self.deaths = deaths
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

    def add_weapon(self, new_weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(new_weapon)

    def add_armor(self, armor):
        '''Add armor to self.armors
          Armor: Armor Object'''
        self.armor.append(armor)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total:Int'''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self, incoming_damage):
        '''Runs `block` method on each armor.
            Returns sum of all blocks'''
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
        print("Your hero's current hp is: {}".format(self.current_health))

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.'''
        if self.current_health > 0:
            print("{} is still alive".format(self.name))
            return True
        else: 
            print("{} has died".format(self.name))
            return False

    def add_kill(self, new_kills):
        ''' Update kills with num_kills'''
        self.kills += new_kills

    def add_death(self):
        ''' Update deaths with num_deaths'''
        self.deaths += 1

    def kill_hero(self, opponent):
        self.current_health = 0
        self.add_death()
        opponent.add_kills
        print("{} has died".format(self.name))

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.'''
        """This function will need to take into account the possibility that both hero may not have abilities and therefore will do no damage.
        --check if to see that at least one hero has an ability. If no abilities exist print out "Draw" """
        if len(self.abilities) == 0 or len(opponent.abilities) == 0: print("Draw")
        else:
            winner = ""
            fighting = True
            num_rounds = 0 
            while (fighting):
                print("\n\t___First Attacker, round {}___\n".format(num_rounds))
                print("{} attacks {}".format(self.name, opponent.name))
                opponent.take_damage(self.attack())
                fighting = opponent.is_alive()

                print("\n\t___Second Attacker, round {}___\n".format(num_rounds))
                print("{} attacks {}".format(opponent.name, self.name))
                self.take_damage(opponent.attack())
                fighting = self.is_alive()
            '''Check to see whose left alive and return the winner'''
            if (not fighting and opponent.is_alive()):    
                winner = ("{} won!".format(opponent.name))
                self.add_death()
                opponent.add_kills()
            else:
                winner = ("{} won!".format(self.name))
                opponent.add_death()
                self.add_kill(1)
            print("\n\n{} & {}, winner: {}".format(self.is_alive(), opponent.is_alive(), winner))
            return winner





if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    
    print("\t\t______TESTING______\n")
    
    