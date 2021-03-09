class Animal:
    def __init__(self, species, diet, native_to):
        self.species = species
        self.diet = diet
        self.native_to = native_to
    def __str__(self):
        return (f"This is a {self.species}. It eats {self.diet} and is native to {self.native_to}.")
    def __repr__(self):
        return (f"Animal: (species: {self.species}, diet: {self.diet}, native_to: {self.native_to})")


lemur = Animal("Lemur", "bugs", "Madagascar")
raccoon = Animal("Raccoon","garbage","USA")

print(lemur)
print(raccoon)

print(repr(lemur))
print(repr(raccoon))