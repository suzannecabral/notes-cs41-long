class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin

class Admin(User):
    def __init__(self, name):
        super().__init__(name, is_admin=True)

class Customer(User):
    def __init__(self,name):
        super().__init__(name)
        # Super has a default value false
        # don't have to refer to is_admin

class Vendor(User):
    def __init__(self, name):
        super().__init__(name)

