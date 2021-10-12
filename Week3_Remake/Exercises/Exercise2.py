import math
import random
import timeit

import numpy as np
import pylab
import seaborn as sns
from matplotlib import pyplot as plt

from Week3.Plot import plot
from Week3_Remake.Logic.Constants import random_action
from Week3_Remake.Logic.Qmatrix import Qmatrix
from Week3_Remake.Logic.Robot import Robot
from Week3_Remake.Logic.World import World

# random.seed(1)

ex2_world = World(_collumns=10, _rows=10, _reward_state=(9, 9))
ex2_robot = Robot(starting_pos=(0, 0))
ex2_qmatrix = Qmatrix(_world=ex2_world)


def setup():
    # print(ex2_qmatrix.matrix)
    pass


def line_a():
    def generate_steps_matrix(_steps_list: list, _collumns: int = 0, _rows: int = 0):

        matrix = np.full((_collumns, _rows), 0)
        for pair in _steps_list:
            x, y = pair
            matrix[x][y] += 1
        return matrix

    def run_test(qmatrix: Qmatrix, world: World, run_number: int):
        test_run_robot = Robot(starting_pos=(0, 0))
        title = "run n" + str(run_number)
        plt.title(title)
        sns.heatmap(ex2_qmatrix.normalized(), annot=True, fmt=".2F", annot_kws={"fontsize": 7})

        test_positions_list = []

        start = timeit.default_timer()
        for step_number in range(1000):
            test_current_pos = test_run_robot.current_pos
            test_positions_list.append(test_current_pos)

            matrix = qmatrix.matrix[test_current_pos[0]][test_current_pos[1]]
            max_quality = max(qmatrix.matrix[test_current_pos[0]][test_current_pos[1]])
            best_action_pos = np.where(
                matrix == max_quality)

            best_action = best_action_pos[0][0]
            world.walk(_robot=test_run_robot, _action=best_action)
            world.end_episode(_robot=test_run_robot)

        stop = timeit.default_timer()
        run_time = (stop - start)
        reward = test_run_robot.rewards
        steps = test_run_robot.steps
        ratio = (test_run_robot.rewards / test_run_robot.steps)

        print("Exercise2::line_a::run_test::run_time", run_time,
              "reward", reward,
              "steps", steps,
              "ratio", ratio
              )

        return run_time, reward, steps, ratio, test_positions_list

    test_step_numbers = [500, 2000, 10000, 20000]

    run_time_list = []
    reward_list = []
    steps_list = []
    ratio_list = []
    steps_taken_list = []
    outer_steps_list = []
    metrics = []

    for _ in range(1):
        for y in range(1, 20001):
            action = random_action()
            current_pos = ex2_robot.current_pos
            next_state = ex2_world.next_state(_action_index=action, _current_pos=current_pos)
            if next_state[0] == 9 and next_state[1] == 9:
                2 + 3
            #               print("Exercise2::line_a:: 9,9")
            ex2_world.walk(_robot=ex2_robot, _action=action)
            outer_steps_list.append(next_state)
            ex2_qmatrix.update_state(_current_pos=current_pos, _action_index=action, _next_pos=next_state)

            if y in test_step_numbers:
                sub__plot_index = test_step_numbers.index(y) + 1
                plt.subplot(2, 2, sub__plot_index)
                metrics.append(
                    run_test(qmatrix=ex2_qmatrix, world=ex2_world, run_number=y))

        for metric in metrics:
            run_time_list.append(metric[0])
            reward_list.append(metric[1])
            steps_list.append(metric[2])
            ratio_list.append(metric[3])
            steps_taken_list.append(metric[4])

        plt.tight_layout()
        plt.show()
        steps_matrix_list = []
        index = 1
        for steps_taken_list_iterated in steps_taken_list:
            subplot = math.ceil(math.sqrt(len(steps_taken_list)))
            plt.subplot(subplot, subplot, index)
            matrix = generate_steps_matrix(_steps_list=steps_taken_list_iterated, _collumns=ex2_world.collumns,
                                           _rows=ex2_world.rows)
            run_number = test_step_numbers[index - 1]
            plt.title(str(run_number))
            sns.heatmap(matrix, linewidths=0.5 )
            index += 1

        plt.tight_layout()
        plt.show()

    plot(ratioList=ratio_list, rewardList=reward_list, stepsList=steps_list, timeList=run_time_list)


def line_b():
    pass


if __name__ == "__main__":
    setup()
    line_a()
    line_b()
