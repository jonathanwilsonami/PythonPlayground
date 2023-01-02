import Animal

class Human(Animal):
    name = None

    def __init__(self, name):
        super().__init__("Human")
        self.name = name

if (__name__ == '__main__'):
    print("Stuff")