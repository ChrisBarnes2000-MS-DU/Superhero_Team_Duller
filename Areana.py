import game_play
from game_play.superheros import *
class Areana():
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams.
        team_one = []
        team_two = []

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        # TODO: This method will allow a user to create an ability.
        # Prompt the user for the necessary information to create a new ability object.
        # return the new ability object.
        new_ability = Ability(input("New Ability's Name: "), input("Ability's Max Damage: "))
        return new_ability

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        new_weapon = Weapon(
            self.prompt_usr("New Weapon's Name: ", "string"),
            self.prompt_usr("Weapon's Max Damage: ", "number")
        )
        return new_weapon

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor
        #  object.
        #
        #  return the new armor object with values set by user.
        new_armor = Armor(
            self.prompt_usr("New Armor's Name: ", "string"),
            self.prompt_usr("Armor's Max Block: ", "number")
        )
        return new_armor

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        # TODO: This method should allow a user to create a hero.
        # User should be able to specify if they want armors, weapons, and abilities.
        # Call the methods you made above and use the return values to build your hero.
        # return the new hero object
        hero = Hero(input("Enter a Hero name: "), 100, 0, 0)
        response = self.prompt_usr("Do you want to add ARmor, an ABility, or a WEapon? ", "string").upper()
        if response == "AB":
            print("adding an ability")
            new_ability = self.create_ability()
            hero.add_ability(new_ability)
        elif response == "AR":
            print("adding armor")
            new_armor =  self.create_armor()
            hero.add_armor(new_armor)
        elif response == "WE":
            print("adding a weapon")
            new_weapon = self.create_weapon()
            hero.add_weapon(new_weapon)
        else:
            print ("Nothing was added")

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

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # TODO: This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        # Add the created hero to team one.
        num = self.prompt_usr("number of members to add to the first team: ", "number")
        #num = int(input("number of members to add to first team: "))
        for i in range(num):
            hero = self.create_hero()
            self.team_one.append(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        # Add the created hero to team two.
        num = self.prompt_usr("number of members to add to the second team: ", "number")
        #num = int(input("number of members to add to first team: "))
        for i in range(num):
            hero = self.create_hero()
            self.team_two.append(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        Team.attack()


if __name__ == "__main__":
    arena = Areana()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
