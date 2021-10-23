from random import random, randint
from statistics import mean

from matplotlib import pyplot as plt

from Assignment2_EvolutionaryMastermindSimulator.Logic.Mastermind import Mastermind, evaluate, fitness


def _assignment2_exercise2_line_a():
    def mutate(input: str, goal: str) -> str:

        def flip_random_bit(input: str):
            input_as_list = list(input)
            index = randint(0, len(input) - 1)
            if input_as_list[index] == "0":
                input_as_list[index] = "1"
            elif input_as_list[index] == "1":
                input_as_list[index] = "0"
            return "".join(input_as_list)

        _original_fitness: int = fitness(goal=goal, curr=input)
        _mutated = input
        _counter = 0
        while _original_fitness >= fitness(goal=goal, curr=_mutated) and _counter < 1000:
            _mutated = flip_random_bit(_mutated)
            _counter += 1
        return _mutated

    def demo1():
        _goal = "0000"
        current_solution: str = Mastermind.randomBitPattern(size=len(_goal))
        mutated: str = mutate(goal=_goal, input=current_solution)
        print("Assignment2_EvolutionaryMastermindSimulator::Exercise2::line_a::_goal", _goal,
              "\ncurrent_solution:", current_solution,
              "fitness:", fitness(goal=_goal, curr=current_solution),
              "\nmutate:", mutated,
              "fitness_mutated:", fitness(goal=_goal, curr=mutated),

              )

    def demo_graph():
        _sample_size: int = 10
        _goal: str = "0000"

        original_fitness_list: [int] = []
        mutated_fitness_list: [int] = []
        original_fitness_list_last10: [int] = []
        mutated_fitness_list_last10: [int] = []

        for _ in range(_sample_size):
            _current_solution: str = Mastermind.randomBitPattern(size=len(_goal))
            _mutated_solution: str = mutate(input=_current_solution, goal=_goal)

            _current_solution_fitness: int = fitness(goal=_goal, curr=_current_solution)
            _mutated_solution_fitness: int = fitness(goal=_goal, curr=_mutated_solution)
            original_fitness_list_last10.append(_current_solution_fitness)
            mutated_fitness_list_last10.append(_mutated_solution_fitness)
            if len(original_fitness_list_last10) == 1:
                original_fitness_list.append(mean(original_fitness_list_last10))
                mutated_fitness_list.append(mean(mutated_fitness_list_last10))

                original_fitness_list_last10.clear()
                mutated_fitness_list_last10.clear()

        plt.plot(original_fitness_list, label="Original")
        plt.plot(mutated_fitness_list, label="Mutated")

        plt.title("Means of fitness on Mutated Values and Original values")
        plt.xlabel("Iterations")
        plt.ylabel("Fitness")
        plt.legend()
        plt.tight_layout()
        plt.show()

    demo1()
    demo_graph()


if __name__ == '__main__':
    _assignment2_exercise2_line_a()
