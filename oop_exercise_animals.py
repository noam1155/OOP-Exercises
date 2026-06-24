import random









class Animal:
    def __init__(self, animal_legs, animal_color):
        self.number_of_legs =animal_legs
        self.color = animal_color
        self.tail = None

    def add_tail(self, tail_object):
        self.tail = tail_object


class Tail:
    def __init__(self, length, thick, speed):
        self.length = length
        self.thick = thick
        self.speed = speed


class Cat(Animal):
    def __init__(self, color, whisker_length):
        super().__init__(animal_legs=4,
                         animal_color=color)
        self.whisker_length = whisker_length
        self.mice_counter = 0
    def get_hunted_mice(self):
        return self.mice_counter

    def hunt_mouse(self):
        self.mice_counter += 1
        print("meow! Caught a mouse! 🐕🐁")



























































