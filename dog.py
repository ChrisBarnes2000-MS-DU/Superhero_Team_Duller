class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Supper Woof!")



#this ends the Dog class


my_dog = Dog("Rover", "SuperDog")
print(my_dog)
print(my_dog.name)
print(my_dog.breed)
my_dog.bark()