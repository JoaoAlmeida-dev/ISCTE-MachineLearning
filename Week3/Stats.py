import random


def deviation(list):
    mean = sum(list) / len(list)
    variance = sum([((x - mean) ** 2) for x in list]) / len(list)
    res = variance ** 0.5
    return str(res)


def mean(list):
    return sum(list) / len(list)


actions = ["left", "right", "down", "up"]


def randomAction():
    return actions[random.randint(0, 3)]