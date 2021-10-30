# Para corrigir a função de avaliação descobri que a implementação mais obvia seria começar com um counter
# no valor do comprimento do maior pattern entre o goal e o guess
#
import random
from random import randint

from Assignment2_EvolutionaryMastermindSimulator.Logic.Mastermind import Mastermind


# First we would have to change the way we generate our patterns to acomodate the new decimal format

def random_decimal_pattern(size: int) -> str:
    result: str = ""
    for _ in range(size):
        result += random_decimal()
    return result


def random_decimal() -> str:
    numbers: [chr] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return random.choice(numbers)


# Para avaliar os novos padrões decimais estou a iterar por todos os caracteres de ambos os padrões e
# convertendo em numeros inteiros, depois calculo o absoluto da subtração do goal pelo curr
def evaluate_decimal(goal: str, curr: str) -> int:
    # _dif_counter: int = max(len(goal), len(curr))
    _dif_counter: int = 0
    for charindex in range(min(len(curr), len(goal))):
        _goal_int: int = int(goal[charindex])
        _current_int: int = int(curr[charindex])
        _dif_counter += abs(_goal_int - _current_int)
        # if curr[charindex] == goal[charindex]:
        #    _dif_counter -= 1

    return _dif_counter


def evaluate_decimal_test():
    for _ in range(10):
        _goal: str = random_decimal_pattern(4)
        _current: str = random_decimal_pattern(4)
        _evaluation: int = evaluate_decimal(goal=_goal, curr=_current)
        print("goal=", _goal, "\t_current=", _current, "\tevaluation=", _evaluation)
    print("goal=", "01231", "\t_current=", "01231", "\tevaluation=", evaluate_decimal(goal="01231", curr="01231"))
    print("goal=", "01231", "\t_current=", "01233", "\tevaluation=", evaluate_decimal(goal="01231", curr="01233"))


# Para corrigir a função de fitness
def fitness_decimal(goal: str, curr: str) -> float:
    _max_diff: int = 9 * max(len(goal), len(curr))
    _dif_counter: int = 9 * min(len(goal), len(curr))

    for charindex in range(min(len(curr), len(goal))):
        _goal_int: int = int(goal[charindex])
        _current_int: int = int(curr[charindex])
        _dif_counter -= abs(_goal_int - _current_int)
        # if curr[charindex] == goal[charindex]:
        #    _dif_counter -= 1

    return _dif_counter / _max_diff


def fitness_decimal_test():
    for _ in range(10):
        _goal: str = random_decimal_pattern(random.randint(1, 4))
        _current: str = random_decimal_pattern(random.randint(1, 4))
        _evaluation: float = fitness_decimal(goal=_goal, curr=_current)
        print("goal=", _goal, "\t_current=", _current, "\tfitness=", _evaluation)
    print("goal=", "01231", "\t_current=", "01231", "\tfitness=", fitness_decimal(goal="01231", curr="01231"))
    print("goal=", "01231", "\t_current=", "012315", "\tfitness=", fitness_decimal(goal="01231", curr="012315"))
    print("goal=", "01231", "\t_current=", "01233", "\tfitness=", fitness_decimal(goal="01231", curr="01233"))
    print("goal=", "01231", "\t_current=", "012330", "\tfitness=", fitness_decimal(goal="01231", curr="012330"))
    print("goal=", "01231", "\t_current=", "0123", "\tfitness=", fitness_decimal(goal="01231", curr="0123"))


# Para a função de mutação apenas terei de somar ou subtrair um valor a un caracter aleatório do padrão
# para alem disso, como antes ter em conta as chances para adicionar ou remover um caracter

def mutate_decimal_size(mutation_input: str) -> str:
    input_as_list = list(mutation_input)
    # print(input_as_list)
    same_add_remove: int = random.choice([1, 2, 3])
    if same_add_remove == 1:
        # same_length
        index = randint(0, len(mutation_input) - 1)
        print("same_length in ", index)
        add_or_subtract = random.choice([True, False])
        int_index_value: int = int(input_as_list[index])
        if add_or_subtract:
            input_as_list[index] = str(int_index_value + 1)
        else:
            input_as_list[index] = str(int_index_value - 1)

    elif same_add_remove == 2:
        # remove_bit
        index = randint(0, len(mutation_input) - 1)
        print("remove_bit in", index)
        input_as_list.pop(index)
    else:
        # add_bit
        index = randint(0, len(mutation_input))
        _new_bit: str = random_decimal()
        print("added_bit", _new_bit, " in", index)
        input_as_list.insert(index, _new_bit)
    # print(input_as_list)
    return "".join(input_as_list)


def mutate_decimal_test():
    for _ in range(10):
        _random: str = random_decimal_pattern(3)
        _mutated: str = mutate_decimal_size(mutation_input=_random)
        print(_random, _mutated)


# Para um padrão de numeros decimais a função de crossover

def crossover_decimal(input_a: str, input_b: str) -> str:
    first_input = random.choice([True, False])
    slice_index = randint(0, min(len(input_a), len(input_b)))
    if first_input:
        return input_a[0:slice_index+1] + input_b[slice_index-1:len(input_b)]
    else:
        return input_b[0:slice_index+1] + input_a[slice_index-1:len(input_a)]


def crossover_decimal_test():
    for _ in range(10):
        _random_a: str = random_decimal_pattern(random.randint(1, 4))
        _random_b: str = random_decimal_pattern(random.randint(1, 4))
        _crossover_value: str = crossover_decimal(input_a=_random_a, input_b=_random_b)
        print(_random_a, _random_b, _crossover_value)


if __name__ == '__main__':
    random.seed(1)
    print("----------evaluate_decimal_test----------")
    evaluate_decimal_test()
    print("----------fitness_decimal----------------")
    fitness_decimal_test()
    print("----------mutate_decimal_test-----------")
    mutate_decimal_test()
    print("----------crossover_decimal_test-----------")
    crossover_decimal_test()
