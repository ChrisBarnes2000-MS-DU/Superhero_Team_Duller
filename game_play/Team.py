import random
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

    def view_all_heroes(self):
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
        num = random(0,len(self.members))
        for member in self.members not in self.dead_members():
            member.fight()
        else:
            return "{} member is dead".format(member.name)

    def revive_heroes(self, health=100):
        ''' Reset all hero health to starting_health'''
        # TODO: This method should reset all hero health to their
        # original starting value.
        pass

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        pass

        def __repr__(self):
            return "Team name: {}, Members: {}".format(self.name, self.view_all_heros())
