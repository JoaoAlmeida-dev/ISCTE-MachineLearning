import random


class Mastermind:
    goal: str
    pattern_size: int

    def __init__(self, goal: str):
        self.goal = goal
        self.pattern_size = len(goal)

    @staticmethod
    def randomBitPattern(size: int) -> str:
        result: str = ""
        for i in range(size):
            if random.random() > 0.5:
                result += '0'
            else:
                result += '1'

        return result


def evaluate(goal: str, curr: str):
    close_value = len(goal)
    for char_index in range(len(goal)):
        if goal[char_index] == curr[char_index]:
            close_value -= 1
    return close_value


def fitness(goal: str, curr: str):
    fitness_value = 0
    for char_index in range(len(goal)):
        if goal[char_index] == curr[char_index]:
            fitness_value += 1
    return fitness_value