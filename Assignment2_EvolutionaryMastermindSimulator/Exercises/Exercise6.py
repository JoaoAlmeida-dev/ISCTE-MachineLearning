# Para corrigir a função de avaliação descobri que a implementação mais obvia seria começar com um counter
# no valor do comprimento do maior pattern entre o goal e o guess
#
import random
from random import randint

from Assignment2_EvolutionaryMastermindSimulator.Logic.Mastermind import Mastermind


def random_decimal_pattern(size: int) -> str:
    result: str = ""
    for _ in range(size):
        result += random_decimal()
    return result


def random_decimal() -> str:
    numbers: [chr] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return random.choice(numbers)


def evaluate_decimal(goal: str, curr: str) -> int:
    # _dif_counter: int = max(len(goal), len(curr))
    _dif_counter: int = 0
    for charindex in range(min(len(curr), len(goal))):
        _goal_int: int = int(goal[charindex])
        _current_int: int = int(curr[charindex])
        _dif_counter += _goal_int - _current_int
        # if curr[charindex] == goal[charindex]:
        #    _dif_counter -= 1

    return _dif_counter


def evaluate_decimal_test():
    for _ in range(10):
        _goal: str = random_decimal_pattern(4)
        _current: str = random_decimal_pattern(4)
        _evaluation: int = evaluate_decimal(goal=_goal, curr=_current)
        print("goal=", _goal, "\t_current=", _current, "\tevaluation=", _evaluation)


# Para corrigir a função de avaliação poderiamos, por exemplo armazenar o numero de caracteres iguais nos
# dois padroẽs e dividir pelo tamanho do padrão maior entre os dois desta maneira tratamos de todas as
# possibilidades, o goal ser maior e o goal ser menor, atribuindo menos fitness e ambas
def fitness_decimal(goal: str, curr: str) -> float:
    pass


def fitness_decimal_test(): pass


# In mutation my guess is that the function will have the chance of adding or removing a random bit

def mutate_decimal_size(input: str) -> str: pass


def mutate_decimal_test(): pass


if __name__ == '__main__':
    print("----------evaluate_decimal_test----------")
    evaluate_decimal_test()
    print("----------fitness_decimal----------")
    fitness_decimal_test()
    print("----------mutate_decimal_test----------")
    mutate_decimal_test()
