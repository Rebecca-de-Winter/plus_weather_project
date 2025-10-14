class Cow():
    species_name = "Bos Taurus"
    diet = "grass"
    
    def __init__(self, instance_name, instance_colour):
        self.name = instance_name
        self.colour = instance_colour
    
    def speak(self):
        print(self)
        print("MOO!")

# bessie = Cow()
bessie = Cow("Bessie", "Brown")
# print(f"Bessie the cow eats {bessie.diet}")
# print("Say something Bessie!")
# bessie.speak()
print(f"This cow's name is {bessie.name}.")
print(f"{bessie.name} is {bessie.colour}")