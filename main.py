class animal():
    def move(self):
        print("I am an animal")

class snake(animal):
    def move(self):
        print("I slither")

class cheetah(animal):
    def move(self):
        print("I RUN!")

obj = snake()
obj.move()
obj2 = cheetah()
obj2.move()