class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        # f string converts numbers to strings to concat
        return f"{self.name} \t${self.price}"