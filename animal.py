class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

    def __repr__(self):
        return f"Animal(name={self.name}, group={self.group}, number_of_legs={self.number_of_legs}, skills={self.skills})"

cat = Animal("Cat", "Mammals", 4, ["climbing", "jumping", "hunting"])
eagle = Animal("Eagle", "Birds", 2, ["flying", "sharp vision", "hunting"])
frog = Animal("Frog", "Amphibians", 4, ["jumping", "swimming", "croaking"])
cobra = Animal("Cobra", "Reptiles", 0, ["slithering", "venomous bite"])
dolphin = Animal("Dolphin", "Mammals", 0, ["swimming", "echolocation", "jumping"])

animals = [cat, eagle, frog, cobra, dolphin]
