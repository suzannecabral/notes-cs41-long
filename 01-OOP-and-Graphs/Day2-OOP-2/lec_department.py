class Department:
    #default values go in args
    def __init__(self, name, products=[]): # , products):
        self.name = name
        # this is a string
        self.products = products
        # this takes in a list of products (has_a)/(has_many)
        # plural, expects a list or dictionary
    def __str__(self):
        output = f" {self.name}\n"
        if len(self.products) < 1:
            output = f"No products found in {self.name}"
        for product in self.products:
            output += f"\t{product}\n"

        return output