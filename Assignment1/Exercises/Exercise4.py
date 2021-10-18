import random

from Assignment1.Logic.Constants import STARTING_POS
from Assignment1.Logic.Qmatrix_Updaters import line_a_random_qmatrix_update, line_b_best_qmatrix_update, \
    greed_qmatrix_update, incremental_greed_qmatrix_update
from Assignment1.Logic.Test_framework import framework
from Assignment1.Logic.Qmatrix import Qmatrix
from Assignment1.Logic.Robot import Robot
from Assignment1.Logic.World import World


def process_walls_from_txt(file):
    walls = []
    contents = file.readlines()
    for line in range(len(contents)):
        for collumn in range(len(contents[line])):
            # print("line:", contents[line], "collumn:", contents[line][collumn])
            if contents[line][collumn] == "x":
                walls.append((line, collumn))
    # print(walls)
    return walls


def setup(walls_file: str):
    with open(walls_file, 'rt') as file:
        _walls_positions = process_walls_from_txt(file)
    ex4_world = World(_collumns=10, _rows=10, _reward_state=(9, 9), _penalty_position=_walls_positions,
                      _penalty_value=-0.1)
    ex4_robot = Robot(starting_pos=STARTING_POS)
    ex4_qmatrix = Qmatrix(_world=ex4_world)

    return ex4_world, ex4_robot, ex4_qmatrix


def _line_a(world: World, qmatrix: Qmatrix, qmatrix_update_function, robot: Robot):

    print("Exercise4::line_a::", )
    framework(qmatrix_update_function=qmatrix_update_function,
              qmatrix=qmatrix,
              robot=robot,
              world=world,
              error_chance=0,
              plot_qmatrix=True
              )


if __name__ == "__main__":
    #Exercicio4
    random.seed(2)
    setup_objects = setup(walls_file='../walls.txt')
    ex4_world = setup_objects[0]
    ex4_robot = setup_objects[1]
    ex4_qmatrix = setup_objects[2]
    _line_a(world=ex4_world, qmatrix=ex4_qmatrix, qmatrix_update_function=line_a_random_qmatrix_update, robot=ex4_robot)
    #_line_a(world=ex4_world, qmatrix=ex4_qmatrix, qmatrix_update_function=line_b_best_qmatrix_update, robot=ex4_robot)
    # _line_a(world=ex4_world, qmatrix=ex4_qmatrix, qmatrix_update_function=greed_qmatrix_update, robot=ex4_robot)
    # _line_a(world=ex4_world, qmatrix=ex4_qmatrix, qmatrix_update_function=incremental_greed_qmatrix_update, robot=ex4_robot)
