# Parent Class
class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def introduce(self):
        print(f"I am {self.name} from {self.universe}. My power is {self.power}.")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Subclass demonstrating Inheritance + Encapsulation
class FlyingHero(Superhero):
    def __init__(self, name, power, universe, altitude=0):
        super().__init__(name, power, universe)
        self.__altitude = altitude  # Encapsulated

    def fly(self):
        self.__altitude += 1000
        print(f"{self.name} is flying at {self.__altitude} feet!")

    def get_altitude(self):
        return self.__altitude

# Create objects
hero1 = Superhero("ShadowMan", "Invisibility", "DarkVerse")
hero2 = FlyingHero("SkyQueen", "Wind Control", "CloudRealm")

hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.fly()
print(f"Current altitude: {hero2.get_altitude()} feet")
