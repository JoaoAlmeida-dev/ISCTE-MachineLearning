import random
from random import randint


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

    @staticmethod
    def evaluate(goal: str, curr: str):
        close_value = len(goal)
        for char_index in range(len(goal)):
            if goal[char_index] == curr[char_index]:
                close_value -= 1
        return close_value

    @staticmethod
    def fitness(goal: str, curr: str):
        fitness_value = 0
        for char_index in range(len(goal)):
            if goal[char_index] == curr[char_index]:
                fitness_value += 1
        return fitness_value

    @staticmethod
    def mutate(input: str, goal: str) -> str:

        def flip_random_bit(input: str):
            input_as_list = list(input)
            index = randint(0, len(input) - 1)
            if input_as_list[index] == "0":
                input_as_list[index] = "1"
            elif input_as_list[index] == "1":
                input_as_list[index] = "0"
            return "".join(input_as_list)

        _original_fitness: int = Mastermind.fitness(goal=goal, curr=input)
        _mutated = input
        _counter = 0
        while _original_fitness >= Mastermind.fitness(goal=goal, curr=_mutated) and _counter < 1000:
            _mutated = flip_random_bit(_mutated)
            _counter += 1
        return _mutated