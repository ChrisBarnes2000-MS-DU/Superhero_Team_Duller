import random

class Ability():
    def __init__(self, name, max_damage):
       '''Create Instance Variables:
          name:String
          max_damage: Integer'''
       self.name = name
       self.max_damage = max_damage

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        return random.randint(0, self.max_damage)

    def __repr__(self):
        return "Ability: {}, max damage: {}".format(self.name, self.max_damage)

#-------------//End OF Ability\\-------------

class Armor():
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer'''
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        return random.randint(0, self.max_block)

#-------------//End OF Armor\\-------------

class Weapon(Ability):
    def __init__(self, name, max_damage):
        super().__init__(name, max_damage)

    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon. """
        return random.randint((self.max_damage//2), self.max_damage)

    def __repr__(self):
        return "Weapon: {}, max damage: {}".format(self.name, self.max_damage)

#-------------//End OF Weapon\\-------------
























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
        print("Your new Hero is: {} \n\tStarting with: {} hp\n".format(self.name, self.current_health))

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
                print("{} armor has {} defence".format(
                    armor.name, armor.max_block))
                total_block += armor.block()
            print("total block/defence {}".format(total_block))
            return total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.'''
        print("incoming damage {}".format(damage))
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
        if len(self.abilities) == 0 or len(opponent.abilities) == 0:
            print("Draw")
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
            print("\n\n{} & {}, winner: {}".format(
                self.is_alive(), opponent.is_alive(), winner))
            return winner

#-------------//End OF Superhero\\-------------











class Team():
    def __init__(self, name):
        '''Initialize your team with its team name
            name: String'''
        self.name = name
        self.members = []
        self.dead = []

    def add_hero(self, hero):
        '''addhero: Parameters: hero: String'''
        self.members.append(hero)

    def dead_members(self, member):
        for member in self.members():
            if member.isAlive():
                self.dead.append(member)

    def remove_hero(self, name):
        '''Remove hero from hero list.
        If Hero isn't found return 0
        removehero: Parameters name: String'''
        for i, member in enumerate(self.members):
            print("looking for name {}".format(member.name))
            if member.name == name:
                del self.members[i]
        return 0

    def view_all_members(self):
        '''Prints out all hero to the console.'''
        for member in self.members:
            print(member.name)

    def kill_team(self):
        for member in self.members:
            member.kill_hero()

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving hero.
        # Hint: Use the fight method in the Hero class.
        print("in attack method")
        random.shuffle(self.members)
        random.shuffle(other_team.members)
        for member in self.members:
            for opponent in other_team.members:
                print("Fighting if both opponents are alive")
                if member.is_alive() or opponent.is_alive():
                    print("{} is fighting {}".format(member.name, opponent.name))
                    member.fight(opponent)
                else:
                    return "{} and {} are dead".format(member.name, opponent.name)
        
    def revive_heroes(self, health=100):
        ''' Reset all hero health to starting_health'''
        # TODO: This method should reset all hero health to their
        # original starting value.
        for member in self.members:
            member.health = health

    def stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        #     Show surviving heroes.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        for members in self.dead_members:
            print("Member {}: had {} kills & {} deaths").format(members.name, members.kill, members.deaths)

    def winning_team(self, opponent):
        if len(self.dead_members) == len(self.members):
            print("Your Team Lost all its members: You Lost")
            Team.stats()
        elif len(self.members) >= len(opponent.members):
            print("Your Teams dead members are")
            Team.stats()

    def __repr__(self):
        return "Team name: {}, Members: {}".format(self.name, self.view_all_members())

#-------------//End OF Team\\-------------
















class Arena():
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams.
        self.team_one = []
        self.team_two = []

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        # TODO: This method will allow a user to create an ability.
        # Prompt the user for the necessary information to create a new ability object.
        # return the new ability object.
        new_ability = Ability(input("New Ability's Name: "),
                              input("Ability's Max Damage: "))
        return new_ability

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        new_weapon = Weapon(
            get_input.prompt_usr(get_input(), "New Weapon's Name: ", "string"),
            get_input.prompt_usr(get_input(), "Weapon's Max Damage: ", "number")
        )
        return new_weapon

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor
        #  object.
        #  return the new armor object with values set by user.
        new_armor = Armor(
            get_input.prompt_usr(get_input(), "New Armor's Name: ", "string"),
            get_input.prompt_usr(get_input(), "Armor's Max Block: ", "number")
        )
        return new_armor

    def create_hero(self, name):
        '''Prompt user for Hero information
          return Hero with values from user input.'''
        # TODO: This method should allow a user to create a hero.
        # User should be able to specify if they want armors, weapons, and abilities.
        # Call the methods you made above and use the return values to build your hero.
        # return the new hero object
        return Hero(name, 100, 0, 0)

    def give_addon(self, hero):
        num = get_input.prompt_usr(get_input(), "Number of add-ons to give {}: \t".format(hero.name), "number")
        for i in range(num):
            print("Adding #{} add-on to {}".format(i+1, hero.name))
            response = get_input.prompt_usr(get_input(), "\nType NEXT to move on OR would you like to add armor, an ability, or a weapon? \t", "string").upper()
            if response == "ABILITY" or response == "AB":
                print("Adding an ability")
                new_ability = self.create_ability()
                hero.add_ability(new_ability)
            elif response == "ARMOR" or response == "AR":
                print("Adding armor")
                new_armor = self.create_armor()
                hero.add_armor(new_armor)
            elif response == "WEAPON" or response == "WE":
                print("Adding a weapon")
                new_weapon = self.create_weapon()
                hero.add_weapon(new_weapon)
            else:
                print("Nothing was added")
        print("Moving on\n")

    def build_team(self, team):
        '''Prompt the user to build a team'''
        # TODO: This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        # Add the created hero to team one.
        num = get_input.prompt_usr(get_input(), "Number of members to add to {}: \t".format(team), "number")
        for i in range(num):
            print ("Adding #{} member to {}".format(i+1, team))
            hero = self.create_hero(input("Enter a Hero name: \t"))
            self.give_addon(hero)
            if team == "team_one":
                self.team_one = Team("team_one")
                self.team_one.add_hero(hero)
            else:
                self.team_two = Team("team_two")
                self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        print("team battle commence")
        self.team_one.view_all_members()
        self.team_two.view_all_members()
        self.team_one.attack(self.team_two)

#-------------//End OF Arena\\-------------

class get_input():
    def prompt_usr(self, prompt, typ):
        if typ == "number":
            response = input(prompt)
            while not response.isnumeric():
                print("Try again: ")
                response = input(prompt)
            print("Entering response {}".format(response))
            return int(response)
        elif typ == "string":
            response = input(prompt)
            while not response.isalpha():
                print("try again: ")
                response = input(prompt)
            print("Entering response {}".format(response))
            return str(response)

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    response = get_input.prompt_usr(get_input(), "Do you want to build teams or go with the default? B or D: \t", "string").upper()  # or D
    if response == "B":
        arena.build_team("team_one")
        arena.build_team("team_two")

    elif response == "D":
        print("Setting up the default/demo teams")

        team_one_names = ["Bill", "Jill", "Jane"]
        team_two_names = ["Kim", "Meg", "Hen"]

        for name in team_one_names:
            hero = arena.create_hero(name)
            arena.team_one.add_hero(hero)
            print("#---Added {} as a member to team one---#".format(name))
        for name in team_two_names:
            hero = arena.create_hero(name)
            arena.team_two.add_hero(hero)
            print("#---added {} as a member to team two---#".format(name))

    while game_is_running:
        print("starting battle")
        arena.team_battle()
        #arena.show_stats()
        play_again = input("Play Again? Y or N: \t")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False
        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

#ARGENT SQUIRE
