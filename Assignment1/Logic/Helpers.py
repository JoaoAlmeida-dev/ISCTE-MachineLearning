import random

import numpy as np

from Assignment1.Logic.Constants import ACTIONS


def max_index_of(iterable: list) -> int:
    _max_value_indexes = []
    _max_value = iterable[0]
    if len(iterable) != 0:
        # first loop determines the max value in the iterable
        for value in iterable:
            if _max_value < value:
                _max_value = value
        # second loop is for breaking ties
        for x in range(len(iterable)):
            if _max_value == iterable[x]:
                _max_value_indexes.append(x)

    random_max_value = random.randint(0, len(_max_value_indexes) - 1)
    return _max_value_indexes[random_max_value]


def generate_matrix_from_coordenates_list(_coords_list: list, _collumns: int, _rows: int):
    matrix = np.full((_collumns, _rows), 0)
    for pair in _coords_list:
        x, y = pair
        matrix[x][y] += 1
    return matrix


def deviation(list):
    if not list:
        return -1
    else:
        mean = sum(list) / len(list)
        variance = sum([((x - mean) ** 2) for x in list]) / len(list)
        res = variance ** 0.5
        return str(res)


def mean(input_list: list):
    if len(input_list) == 0:
        return -1
    else:
        return sum(input_list) / len(input_list)


def test_max_index_of():
    test_list = [5, 1, 2, 3, 4, 5]
    max_index = max_index_of(test_list)
    print("Helpers::max_index_of(", test_list, ")",
          "index=", max_index,
          "value=", test_list[max_index]
          )


def random_action():
    return random.randint(0, len(ACTIONS) - 1)


if __name__ == "__main__":
    test_max_index_of()
