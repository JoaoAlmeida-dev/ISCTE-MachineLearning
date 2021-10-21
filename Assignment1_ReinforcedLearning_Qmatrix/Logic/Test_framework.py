import math
import timeit
from typing import List

import seaborn as sns
from matplotlib import pyplot as plt

from Assignment1_ReinforcedLearning_Qmatrix.Logic.Constants import EXPERIMENT_MAX_STEPS, EXPERIMENT_NUMBER, STARTING_POS, STEPS_FOR_TESTS
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Plot import plot_results
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Qmatrix import Qmatrix
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Result import Result
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Robot import Robot
from Assignment1_ReinforcedLearning_Qmatrix.Logic.World import World


def run_test(qmatrix: Qmatrix, world: World, run_number: int, plot_qmatrix: bool, qmatrix_step_number: int,
             error_chance: float) -> Result:
    _exploiter_robot = Robot(starting_pos=STARTING_POS)
    if plot_qmatrix:
        title = "run n" + str(run_number)
        plt.title(title)
        sns.heatmap(qmatrix.normalized(), annot=False, fmt=".2F", annot_kws={"fontsize": 7})

    for step_number in range(1000):
        test_current_pos = _exploiter_robot.current_pos

        best_action = qmatrix.best_action(test_current_pos)

        world.walk(_robot=_exploiter_robot, _action=best_action, _end_of_episode=True, _error_chance=error_chance)

    reward_per_step = (_exploiter_robot.rewards / _exploiter_robot.total_steps)
    result = Result(_rewards=_exploiter_robot.rewards,
                    _steps_per_reward_mean=_exploiter_robot.get_steps_per_reward_mean(),
                    _rewards_per_step=reward_per_step,
                    _qmatrix_step=qmatrix_step_number)
    return result


def experiment(steps_for_test_list: list, qmatrix_update_function, qmatrix: Qmatrix, world: World,
               robot: Robot, error_chance: float, plot_qmatrix=False
               ) -> (List[Result], float):
    results_list = []
    start = timeit.default_timer()
    for y in range(1, EXPERIMENT_MAX_STEPS):
        qmatrix_update_function(steps=y, robot=robot, qmatrix=qmatrix, world=world, error_chance=error_chance)
        if y in steps_for_test_list:
            sub__plot_index = steps_for_test_list.index(y) + 1
            plt.subplot(
                math.ceil(math.sqrt(len(steps_for_test_list))),
                math.ceil(math.sqrt(len(steps_for_test_list))),
                sub__plot_index)
            results_list.append(
                run_test(qmatrix=qmatrix, world=world, run_number=y, plot_qmatrix=plot_qmatrix, qmatrix_step_number=y,
                         error_chance=error_chance)
            )

    stop = timeit.default_timer()
    experiment_time = stop - start
    qmatrix.reset()

    return results_list, experiment_time


def framework(qmatrix_update_function, qmatrix: Qmatrix, world: World, plot_qmatrix: bool, robot: Robot,
              error_chance: float):
    experiment_results = []
    experiment_runtimes = []
    for _experiment in range(EXPERIMENT_NUMBER):
        print("Test_framework::framework::experiment n", _experiment)
        experiment_outputs = experiment(steps_for_test_list=STEPS_FOR_TESTS,
                                        qmatrix_update_function=qmatrix_update_function,
                                        robot=robot,
                                        qmatrix=qmatrix,
                                        world=world,
                                        error_chance=error_chance,
                                        plot_qmatrix=plot_qmatrix
                                        )
        experiment_runtimes.append(experiment_outputs[1])
        for result in experiment_outputs[0]:
            experiment_results.append(result)
    plt.tight_layout()
    plt.show()
    plot_results(experiment_results, experiment_runtimes)
