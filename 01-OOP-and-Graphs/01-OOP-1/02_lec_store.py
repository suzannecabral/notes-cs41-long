# from Department

class Store:
    # attributes
    # names
    # departments

    # method of a class
    # initializer, similar to a constructor
    # can give it a default name, leave optional ones at the end
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def __str__(self):
        output = f"{self.name}\n"
        for i, dept in enumerate(self.departments):
            output += " " + str(i + 1) + ". " + dept + "\n"
        return output
    
my_store = Store("Bob's Emporium", ["Clothes","Tools","Electronics"])
# printing the object will output the location of the object in memory
# print(my_store)

# dir()
# gives all the methods of something

# making it user-selectable
# make a var to hold the user's choice 
choice = 0

# print out the menu 
print(my_store)

# await some input from the user
choice = int(input(f"Select the number of department you wish to enter.\n"))

# print the users choice
print(f"You chose {my_store.departments[choice-1]}")