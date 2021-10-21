import random

from Assignment1_ReinforcedLearning_Qmatrix.Logic.Constants import STARTING_POS
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Qmatrix import Qmatrix
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Qmatrix_Updaters import line_b_best_qmatrix_update
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Robot import Robot
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Test_framework import framework
from Assignment1_ReinforcedLearning_Qmatrix.Logic.World import World


ex5_world = World(_collumns=10, _rows=10, _reward_state=(9, 9))
ex5_robot = Robot(starting_pos=STARTING_POS)
ex5_qmatrix = Qmatrix(_world=ex5_world)


def _line_a(world: World, qmatrix: Qmatrix, qmatrix_update_function, robot: Robot,error_chance:float):
    print("Exercise5::line_a", )
    framework(qmatrix_update_function=qmatrix_update_function,
              qmatrix=qmatrix,
              robot=robot,
              world=world,
              error_chance=error_chance,
              plot_qmatrix=True
              )

if __name__ == "__main__":
    #Exercicio5
    random.seed(2)
    # _line_a(world=ex4_world, qmatrix=ex4_qmatrix, qmatrix_update_function=line_a_random_qmatrix_update, robot=ex4_robot)
    _line_a(world=ex5_world, qmatrix=ex5_qmatrix, qmatrix_update_function=line_b_best_qmatrix_update, robot=ex5_robot, error_chance=0.05)
    # _line_a(world=ex4_world, qmatrix=ex4_qmatrix, qmatrix_update_function=greed_qmatrix_update, robot=ex4_robot)
    # _line_a(world=ex4_world, qmatrix=ex4_qmatrix, qmatrix_update_function=incremental_greed_qmatrix_update, robot=ex4_robot)
