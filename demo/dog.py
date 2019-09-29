class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Supper Woof!")

    def sit(self):
        print("{} sits".format(self.name))

    def rollover(self):
        print("{} rolls over".format(self.name))

#this ends the Dog class

Dog.greeting = "Woof"