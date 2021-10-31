import random
from random import randint


class Mastermind:
    goal: str
    pattern_size: int

    def __init__(self, goal: str):
        self.goal = goal
        self.pattern_size = len(goal)

    @staticmethod
    def random_bit_pattern(size: int) -> str:
        result: str = ""
        for _ in range(size):
            result += Mastermind.random_bit()
        return result

    @staticmethod
    def random_bit() -> str:
        return random.choice(['0','1'])

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
    def mutate(input: str) -> str:
        input_as_list = list(input)
        index = randint(0, len(input) - 1)
        if input_as_list[index] == "0":
            input_as_list[index] = "1"
        elif input_as_list[index] == "1":
            input_as_list[index] = "0"
        return "".join(input_as_list)

    @staticmethod
    def crossover(input_a: str, input_b: str) -> str:
        first_input = randint(0, 1)
        slice_index = randint(0, min(len(input_a), len(input_b)))
        if first_input == 0:
            return input_a[0:slice_index] + input_b[slice_index:len(input_b)]
        else:
            return input_b[0:slice_index] + input_a[slice_index:len(input_a)]


if __name__ == '__main__':
    for _ in range(100):
        _goal = "11111111"
        _original:str = "11111111"
        print("original:",_original, "mutated:" , Mastermind.mutate(_original,_goal))


    print(Mastermind.crossover("00000", "11111"))
