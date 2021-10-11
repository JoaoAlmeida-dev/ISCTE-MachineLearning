import random

actions = ["left", "right", "down", "up"]


def random_action():
    return random.randint(0, len(actions) - 1)
