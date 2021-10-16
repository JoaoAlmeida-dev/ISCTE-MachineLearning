import math
import timeit
import random

import seaborn as sns
from matplotlib import pyplot as plt
from typing import Tuple, List

from Assignment1.Logic.Plot import plot, plot_results
from Assignment1.Logic.Helpers import max_index_of, generate_matrix_from_coordenates_list, mean, random_action
from Assignment1.Logic.Qmatrix import Qmatrix
from Assignment1.Logic.Result import Result
from Assignment1.Logic.Robot import Robot
from Assignment1.Logic.World import World

# random.seed(1)
EXPERIMENT_MAX_STEPS = 20001
EXPERIMENT_NUMBER = 30
STARTING_POS = (0, 0)

ex2_world = World(_collumns=10, _rows=10, _reward_state=(9, 9))
ex2_robot = Robot(starting_pos=STARTING_POS)
ex2_qmatrix = Qmatrix(_world=ex2_world)

STEPS_FOR_TESTS = [100, 1000, 10000, 20000]


# STEPS_FOR_TESTS = [0,1,10,50,100,20000]
# STEPS_FOR_TESTS = [100, 200, 500, 600, 700, 800, 900, 1000, 2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000]


def line_a_random_qmatrix_update(steps: int):
    action = random_action()
    current_pos = ex2_robot.current_pos

    next_state = ex2_world.next_state(_action_index=action, _current_pos=current_pos)
    ex2_world.walk(_robot=ex2_robot, _action=action, _end_of_episode=True)
    ex2_qmatrix.update_state(_current_pos=current_pos, _action_index=action, _next_pos=next_state)


def line_b_best_qmatrix_update(steps: int):
    current_pos = ex2_robot.current_pos
    action = ex2_qmatrix.best_action(current_pos)

    next_state = ex2_world.next_state(_action_index=action, _current_pos=current_pos)
    ex2_world.walk(_robot=ex2_robot, _action=action, _end_of_episode=True)
    ex2_qmatrix.update_state(_current_pos=current_pos, _action_index=action, _next_pos=next_state)


def run_test(qmatrix: Qmatrix, world: World, run_number: int, plot_qmatrix: bool) -> Result:
    _exploiter_robot = Robot(starting_pos=STARTING_POS)
    if plot_qmatrix:
        title = "run n" + str(run_number)
        plt.title(title)
        sns.heatmap(qmatrix.normalized(), annot=False, fmt=".2F", annot_kws={"fontsize": 7})

    for step_number in range(1000):
        test_current_pos = _exploiter_robot.current_pos

        # matrix = qmatrix.matrix[test_current_pos[0]][test_current_pos[1]]
        # max_quality = max(qmatrix.matrix[test_current_pos[0]][test_current_pos[1]])
        # best_action_pos = np.where(    matrix == max_quality)

        # best_action = best_action_pos[0][0]
        best_action = qmatrix.best_action(test_current_pos)
        # best_action = max_index_of(qmatrix.matrix[test_current_pos[0]][test_current_pos[1]])
        world.walk(_robot=_exploiter_robot, _action=best_action, _end_of_episode=True)
        # world.end_episode(_robot=exploiter_robot)

    reward_per_step = (_exploiter_robot.rewards / _exploiter_robot.total_steps)
    result = Result(_rewards=_exploiter_robot.rewards,
                    _steps_per_reward_mean=_exploiter_robot.get_steps_per_reward_mean(),
                    _rewards_per_step=reward_per_step, )
    return result
    # return reward_per_step, _exploiter_robot.total_steps
    # ,exploiter_robot.position_history


def experiment(steps_for_test_list: list, qmatrix_update_function, qmatrix: Qmatrix, world: World,
               plot_qmatrix=False) -> (List[Result], float):
    results_list = []
    start = timeit.default_timer()
    for y in range(1, EXPERIMENT_MAX_STEPS):
        # random_qmatrix_update()
        qmatrix_update_function(y)

        if y in steps_for_test_list:
            sub__plot_index = steps_for_test_list.index(y) + 1
            plt.subplot(
                math.ceil(math.sqrt(len(steps_for_test_list))),
                math.ceil(math.sqrt(len(steps_for_test_list))),
                sub__plot_index)
            results_list.append(
                run_test(qmatrix=qmatrix, world=world, run_number=y, plot_qmatrix=plot_qmatrix))

    stop = timeit.default_timer()
    experiment_time = stop - start
    qmatrix.reset()
    # if plot_qmatrix:
    #    plt.tight_layout()
    #    plt.show()

    return results_list, experiment_time


def framework(qmatrix_update_function, qmatrix: Qmatrix, world: World, plot_qmatrix: bool):
    experiment_results = []
    experiment_runtimes = []
    for _experiment in range(EXPERIMENT_NUMBER):
        print("Exercise2::framework::experiment n", _experiment)
        experiment_outputs = experiment(steps_for_test_list=STEPS_FOR_TESTS,
                                        qmatrix_update_function=qmatrix_update_function,
                                        qmatrix=qmatrix,
                                        world=world,
                                        plot_qmatrix=plot_qmatrix
                                        )
        experiment_runtimes.append(experiment_outputs[1])
        for result in experiment_outputs[0]:
            experiment_results.append(result)
    plt.tight_layout()
    plt.show()
    # results_averages = results_parser(experiment_results)
    # plot_line_a(results_averages)
    plot_results(experiment_results, experiment_runtimes)


def _line_a():
    framework(line_a_random_qmatrix_update, qmatrix=ex2_qmatrix, world=ex2_world, plot_qmatrix=True)


def _line_b():
    framework(line_b_best_qmatrix_update, qmatrix=ex2_qmatrix, world=ex2_world, plot_qmatrix=True)


if __name__ == "__main__":
    random.seed(1)
    # _line_a()
    _line_b()
