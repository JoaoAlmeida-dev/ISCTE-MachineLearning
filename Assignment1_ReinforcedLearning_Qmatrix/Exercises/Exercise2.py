import random

from Assignment1_ReinforcedLearning_Qmatrix.Logic.Constants import STARTING_POS
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Qmatrix import Qmatrix
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Qmatrix_Updaters import line_a_random_qmatrix_update, line_b_best_qmatrix_update
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Robot import Robot
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Test_framework import framework
from Assignment1_ReinforcedLearning_Qmatrix.Logic.World import World

# random.seed(1)

ex2_world = World(_collumns=10, _rows=10, _reward_state=(9, 9))
ex2_robot = Robot(starting_pos=STARTING_POS)
ex2_qmatrix = Qmatrix(_world=ex2_world)


def _line_a():
    print("Exercise2::line_a::")
    framework(line_a_random_qmatrix_update, qmatrix=ex2_qmatrix, world=ex2_world, robot=ex2_robot, plot_qmatrix=True,error_chance=0)


def _line_b():
    print("Exercise2::line_b::")
    framework(line_b_best_qmatrix_update, qmatrix=ex2_qmatrix, world=ex2_world, robot=ex2_robot, plot_qmatrix=True,error_chance=0)


if __name__ == "__main__":
    #Exercicio2
    random.seed(1)
    #_line_a()
    _line_b()
