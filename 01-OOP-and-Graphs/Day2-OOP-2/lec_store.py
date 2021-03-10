from lec_department import Department
from lec_product import Product
from lec_electronic import Electronic

class Store:
    # attributes
    # name
    # departments
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments
    def __str__(self):
        output = f"\n{self.name}\n"
 
        for i, dept in enumerate(self.departments):
            output += " " + str(i + 1) + ". " + dept.name + "\n"
        
        output += f" {i + 2}. Exit"
        return output

    def __repr__(self):
        return f'Store("{self.name}", {self.departments})'

# lets create some products

# clothes_dept
tshirt = Product("Long Sleeve T-Shirt", 20, "Blue")
red_shoes = Product("Red Running Shoe", 34, "Red")

# tools_dept
hammer = Product("Ball Pane Hammer", 5, "Hammer")
screwdriver = Product("Philips Head Screwdriver", 3, "Screwdriver")

# electronics_dept
television = Product("50 inch Wide Screen LCD", 400, "50w")
tablet = Product("Android Tablet", 50, "8w")



# lets create some Departments
clothes_dept = Department("Clothes", [tshirt, red_shoes])
tools_dept = Department("Tools", [hammer, screwdriver])
electronics_dept = Department("Electronics", [television, tablet])


# instance of the Store class
my_store = Store("Bobs Emporium", [clothes_dept, tools_dept, electronics_dept])

# print(repr(my_store))
# make a variable to hold the users choice?
choice = 0
while choice != len(my_store.departments) + 1:

    # print out the menu
    print(my_store)

    # request input from the user
    choice = int(input("Select the number of department you wish to enter. "))
    if choice == len(my_store.departments) + 1:
        print(f"Thanks for shopping at {my_store.name}")
        break
    elif choice > 0 and choice <= len(my_store.departments):
        # print the users choice
        print(f"{my_store.departments[choice - 1]}")
    else:
        print(f"Please choose a valid number between [1] and [{len(my_store.departments) + 1}]")