from lec_product import Product

# inheritance(is_a relationship)
class Clothing(Product):
    def __init__(self, name, price, size, color):
        super().__init__(name, price)
        self.size = size
        self.color = color

    def __str__(self):
        return f"{super().__str__()} comes in {self.size} and {self.color}"