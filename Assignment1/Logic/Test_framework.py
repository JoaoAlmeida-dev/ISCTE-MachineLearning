import math
import timeit
from typing import List

import seaborn as sns
from matplotlib import pyplot as plt

from Assignment1.Logic.Constants import EXPERIMENT_MAX_STEPS, EXPERIMENT_NUMBER, STARTING_POS, STEPS_FOR_TESTS
from Assignment1.Logic.Plot import plot_results
from Assignment1.Logic.Qmatrix import Qmatrix
from Assignment1.Logic.Result import Result
from Assignment1.Logic.Robot import Robot
from Assignment1.Logic.World import World


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
               robot: Robot, plot_qmatrix=False) -> (List[Result], float):
    results_list = []
    start = timeit.default_timer()
    for y in range(1, EXPERIMENT_MAX_STEPS):
        qmatrix_update_function(steps=y, robot=robot,qmatrix=qmatrix,world=world)
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

    return results_list, experiment_time


def framework(qmatrix_update_function, qmatrix: Qmatrix, world: World, plot_qmatrix: bool, robot: Robot):
    experiment_results = []
    experiment_runtimes = []
    for _experiment in range(EXPERIMENT_NUMBER):
        print("Test_framework::framework::experiment n", _experiment)
        experiment_outputs = experiment(steps_for_test_list=STEPS_FOR_TESTS,
                                        qmatrix_update_function=qmatrix_update_function,
                                        robot=robot,
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
