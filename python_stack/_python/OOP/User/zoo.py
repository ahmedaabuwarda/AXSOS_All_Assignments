class Animal:
    def __init__(self, name, age, health_level, happenies_level):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happenies_level = happenies_level

    def display_info(self):
        print(f"Animal: {self.name} {self.health_level} {self.happenies_level}")
    
    def feed(self):
        self.happenies_level = self.happenies_level + 10
        self.health_level = self.health_level + 10


class Lion(Animal):
    def __init__(self, name, age, health_level, happenies_level, voice, color):
        self.voice = voice
        self.color = color
        super().__init__(name, age, health_level, happenies_level)

    def feed(self):
        super().feed()
        self.happenies_level = self.happenies_level + 15
        self.health_level = self.health_level + 15


class Monky(Animal):
    def __init__(self, name, age, health_level, happenies_level, gender, family):
        self.family = family
        self.gender = gender
        super().__init__(name, age, health_level, happenies_level)

    def feed(self):
        super().feed()
        self.happenies_level = self.happenies_level + 20
        self.health_level = self.health_level + 20


class Bear(Animal):
    def __init__(self, name, age, health_level, happenies_level, type):
        self.type = type
        super().__init__(name, age, health_level, happenies_level)

    def feed(self):
        super().feed()
        self.happenies_level = self.happenies_level + 11
        self.health_level = self.health_level + 11


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name, age, health_level, happenies_level, voice, color):
        self.animals.append(Lion(name, age, health_level, happenies_level, voice, color))
    def add_lion_ob(self, lion):
        self.animals.append(lion)
    def add_bear(self, name, age, health_level, happenies_level, type):
        self.animals.append(Bear(name, age, health_level, happenies_level, type))
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala", 4, 22, 16, "Roar", "orange")
zoo1.add_lion("Simba", 5, 12, 26, "Roar", "white")
big = Lion("BeBe", 8, 12, 6, "Roar", "yellow")
big.feed()
zoo1.add_lion_ob(big)
zoo1.add_bear("Rajah", 6, 8, 55, "Wild")
zoo1.add_bear("Shere Khan", 3, 15, 60, "White")
zoo1.print_all_info()