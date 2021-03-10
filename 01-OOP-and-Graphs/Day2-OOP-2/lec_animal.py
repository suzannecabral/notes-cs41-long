# super class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak():
        return "I am an Animal"

# sub class
class Dog(Animal):
    def __init__(self, name, age, breed):
        # taking from the caller and pass it on
        # this is the getter for the super class
        super().__init__(name, age)
        self.breed = breed

bruno = Dog("Bruno")