class Animal:
    def __init__(self, species, diet, native_to):
        self.species = species
        self.diet = diet
        self.native_to = native_to

lemur = Animal("Lemur", "bugs", "Madagascar")
raccoon = Animal("Raccoon","garbage","USA")

print(lemur)
print(raccoon)