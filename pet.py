class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness += 1

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness += 2
        self.hunger += 1

    def get_status(self):
        print(f"Name: {self.name} | Hunger: {self.hunger} | Energy: {self.energy} | Happiness: {self.happiness}")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}")

    def show_tricks(self):
        print(f"{self.name}'s Tricks: {', '.join(self.tricks)}")
