import random


def deviation(list):
    if not list:
        return -1
    else:
        mean = sum(list) / len(list)
        variance = sum([((x - mean) ** 2) for x in list]) / len(list)
        res = variance ** 0.5
        return str(res)


def mean(list:list):
    if not list:
        return -1
    else:
        return sum(list) / len(list)


actions = ["left", "right", "down", "up"]


def randomAction():
    return actions[random.randint(0, 3)]


def pretty_print(matrix, string):
    for x in range(len(matrix)):
        print(string, matrix[x])
