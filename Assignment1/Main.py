from math import sqrt, ceil
import random

from Assignment1.Logic.World import World


def main():
    # randomQWalk()
    side_size = 10
    world = World(_collumns=side_size, _rows=side_size, _reward_state=(9, 9))
    print(world.pretty_print())

    print(ceil(sqrt(12)))
    print(ceil(sqrt(11)))
    print(ceil(sqrt(10)))
    print(ceil(sqrt(9)))
    print(ceil(sqrt(8)))
    print(ceil(sqrt(7)))
    print(ceil(sqrt(6)))
    print(ceil(sqrt(5)))
    print(ceil(sqrt(4)))


def random_test():
    _true = 0
    _false = 0
    _total = 0
    for y in range(100000):
        _greed: float = 0.9
        _temp_random: float = random.random()
        _random_action: bool = _temp_random > _greed
        if _random_action:
            _true += 1
        else:
            _false += 1
        _total += 1
    print(
        "true", _true, "true %", _true * 100 / _total,"%",
        "\nfalse", _false, "false %", _false * 100 / _total,"%",
        "\ntotal", _total,
    )


if __name__ == "__main__":
    # main()
    random_test()
