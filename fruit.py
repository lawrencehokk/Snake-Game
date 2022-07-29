

import random


class Fruit:
    def __init__(self, screen_width, screen_height):
        self.location = [random.randint(1, (screen_width // 10)) * 10, random.randint(1, (screen_height // 10)) * 10]

    def randomize_location(self, screen_width, screen_height):
        self.location = [random.randint(1, (screen_width // 10)) * 10, random.randint(1, (screen_height // 10)) * 10]


