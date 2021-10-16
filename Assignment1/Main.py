from math import sqrt, ceil

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

if __name__ == "__main__":
    main()



