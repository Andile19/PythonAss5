#base class
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

#subclass
class Bird(Animal):
    def move(self):
        return "Flap wings and fly"
    
class Fish(Animal):
    def move(self):
        return "Swim in water"

class Mammal(Animal):
    def move(self):
        return "Walk on land"

class Reptile(Animal):
    def move(self):
        return "Crawl on land"

class Amphibian(Animal):
    def move(self):
        return "Swim in water and crawl on land"

class Insect(Animal):
    def move(self):
        return "Crawl or fly"

class Arachnid(Animal):
    def move(self):
        return "Crawl on land"

# list of Animals 
animals = [
    Bird(),
    Fish(),
    Mammal(),
    Reptile(),
    Amphibian(),
    Insect(),
    Arachnid()
]
# polymorphic behavior
for animal in animals:
    print(f"{animal.__class__.__name__} moves by: {animal.move()}")
# Output:
# Bird moves by: Flap wings and fly