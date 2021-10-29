# Para corrigir a função de avaliação descobri que a implementação mais obvia seria começar com um counter
# no valor do comprimento do maior pattern entre o goal e o guess
#
import random
from random import randint

from Assignment2_EvolutionaryMastermindSimulator.Logic.Mastermind import Mastermind


def evaluate_undefined_size(goal: str, curr: str) -> int:
    _dif_counter: int = max(len(goal), len(curr))
    for charindex in range(min(len(curr), len(goal))):
        if curr[charindex] == goal[charindex]:
            _dif_counter -= 1

    return _dif_counter


def evaluate_undefined_size_test():
    print("goal=110,\t curr=110\t", evaluate_undefined_size(goal="110", curr="110"))
    print("goal=1101,\t curr=110\t", evaluate_undefined_size(goal="1101", curr="110"))
    print("goal=11011,\t curr=110\t", evaluate_undefined_size(goal="11011", curr="110"))
    print("goal=110111, curr=110\t", evaluate_undefined_size(goal="110111", curr="110"))
    print("goal=110111, curr=11\t", evaluate_undefined_size(goal="110111", curr="11"))
    print("goal=1,\t\t curr=110\t", evaluate_undefined_size(goal="1", curr="110"))
    print("goal=1,\t\t curr=11011\t", evaluate_undefined_size(goal="1", curr="11011"))
    print("goal=1,\t\t curr=1\t", evaluate_undefined_size(goal="1", curr="1"))


# Para corrigir a função de avaliação poderiamos, por exemplo armazenar o numero de caracteres iguais nos
# dois padroẽs e dividir pelo tamanho do padrão maior entre os dois desta maneira tratamos de todas as
# possibilidades, o goal ser maior e o goal ser menor, atribuindo menos fitness e ambas
def fitness_undefined_size(goal: str, curr: str) -> float:
    _max_size: int = max(len(goal), len(curr))
    _equal_counter: int = 0
    for charindex in range(min(len(curr), len(goal))):
        if curr[charindex] == goal[charindex]:
            _equal_counter += 1
    return _equal_counter / _max_size


def fitness_undefined_size_test():
    print("goal=110,\t curr=110\t", fitness_undefined_size(goal="110", curr="110"))
    print("goal=1101,\t curr=110\t", fitness_undefined_size(goal="1101", curr="110"))
    print("goal=11011,  curr=110\t", fitness_undefined_size(goal="11011", curr="110"))
    print("goal=110111, curr=110\t", fitness_undefined_size(goal="110111", curr="110"))
    print("goal=1,\t\t curr=110\t", fitness_undefined_size(goal="1", curr="110"))
    print("goal=1,\t\t curr=11011\t", fitness_undefined_size(goal="1", curr="11011"))
    print("goal=1,\t\t curr=1\t", fitness_undefined_size(goal="1", curr="1"))
    print("goal=1,\t\t curr=01\t", fitness_undefined_size(goal="1", curr="01"))


# In mutation my guess is that the function will have the chance of adding or removing a random bit

def mutate_undefined_size(input: str) -> str:
    input_as_list = list(input)
    # print(input_as_list)
    same_add_remove: int = randint(0, 3)
    if same_add_remove == 1:
        # same_length
        index = randint(0, len(input) - 1)
        print("same_length in ", index)
        if input_as_list[index] == "0":
            input_as_list[index] = "1"
        elif input_as_list[index] == "1":
            input_as_list[index] = "0"
    elif same_add_remove == 2:
        # remove_bit
        index = randint(0, len(input) - 1)
        print("remove_bit in", index)
        input_as_list.pop(index)
    else:
        # add_bit
        index = randint(0, len(input))
        _new_bit:str = Mastermind.random_bit()
        print("added_bit",_new_bit," in", index )
        input_as_list.insert(index,_new_bit )
    # print(input_as_list)
    return "".join(input_as_list)


def mutate_undefined_size_test():
    for _ in range(10):
        _random: str = Mastermind.random_bit_pattern(3)
        _mutated: str = mutate_undefined_size(input=_random)
        print(_random, _mutated)


if __name__ == '__main__':
    print("----------evaluate_undefined_size_test----------")
    evaluate_undefined_size_test()
    print("----------fitness_undefined_size----------")
    fitness_undefined_size_test()
    print("----------mutate_undefined_size_test----------")
    mutate_undefined_size_test()
