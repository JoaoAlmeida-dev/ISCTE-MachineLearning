import random

from Assignment1_ReinforcedLearning_Qmatrix.Logic.Constants import STARTING_POS
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Qmatrix_Updaters import greed_qmatrix_update, incremental_greed_qmatrix_update
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Test_framework import framework
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Qmatrix import Qmatrix
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Robot import Robot
from Assignment1_ReinforcedLearning_Qmatrix.Logic.World import World

ex3_world = World(_collumns=10, _rows=10, _reward_state=(9, 9))
ex3_robot = Robot(starting_pos=STARTING_POS)
ex3_qmatrix = Qmatrix(_world=ex3_world)


def _line_a():
    print("Exercise3::line_a::")
    #constant greed
    framework(qmatrix_update_function=greed_qmatrix_update,
              qmatrix=ex3_qmatrix,
              robot=ex3_robot,
              world=ex3_world,
              error_chance=0,
              plot_qmatrix=True
              )


def _line_b():
    print("Exercise3::line_b::")
    #incremental greed
    framework(qmatrix_update_function=incremental_greed_qmatrix_update,
              qmatrix=ex3_qmatrix,
              robot=ex3_robot,
              world=ex3_world,
              error_chance=0,
              plot_qmatrix=True
              )


if __name__ == "__main__":
    #Exercicio3
    random.seed(1)
    #_line_a()
    _line_b()
