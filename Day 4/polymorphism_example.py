class Bird:
    def fly(self):
        return "Most birds can fly."

class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly."

def show_fly(bird):
    print(bird.fly())

sparrow = Bird()
penguin = Penguin()

show_fly(sparrow)
show_fly(penguin)
