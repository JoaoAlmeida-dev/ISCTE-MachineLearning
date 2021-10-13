import math
import timeit

import seaborn as sns
from matplotlib import pyplot as plt
from typing import Tuple

from Week3_Remake.Logic.Plot import plot
from Week3_Remake.Logic.Constants import random_action
from Week3_Remake.Logic.Helpers import max_index_of, generate_matrix_from_coordenates_list, mean
from Week3_Remake.Logic.Qmatrix import Qmatrix
from Week3_Remake.Logic.Robot import Robot
from Week3_Remake.Logic.World import World

# random.seed(1)

ex2_world = World(_collumns=10, _rows=10, _reward_state=(9, 9))
ex2_robot = Robot(starting_pos=(0, 0))
ex2_qmatrix = Qmatrix(_world=ex2_world)


def random_qmatrix_update():
    action = random_action()
    current_pos = ex2_robot.current_pos
    next_state = ex2_world.next_state(_action_index=action, _current_pos=current_pos)
    ex2_world.walk(_robot=ex2_robot, _action=action, _end_of_episode=True)
    ex2_qmatrix.update_state(_current_pos=current_pos, _action_index=action, _next_pos=next_state)
    # ex2_world.end_episode(_robot=ex2_robot)


def run_test(qmatrix: Qmatrix, world: World, run_number: int, plot_qmatrix: bool, upgrade_steps_matrix: int):
    exploiter_robot = Robot(starting_pos=(0, 0))
    if plot_qmatrix:
        title = "run n" + str(run_number)
        plt.title(title)
        sns.heatmap(ex2_qmatrix.normalized(), annot=False, fmt=".2F", annot_kws={"fontsize": 7})

    for step_number in range(1000):
        test_current_pos = exploiter_robot.current_pos

        # matrix = qmatrix.matrix[test_current_pos[0]][test_current_pos[1]]
        # max_quality = max(qmatrix.matrix[test_current_pos[0]][test_current_pos[1]])
        # best_action_pos = np.where(    matrix == max_quality)

        # best_action = best_action_pos[0][0]
        best_action = max_index_of(qmatrix.matrix[test_current_pos[0]][test_current_pos[1]])
        world.walk(_robot=exploiter_robot, _action=best_action, _end_of_episode=True)
        # world.end_episode(_robot=exploiter_robot)

    reward_per_step = (exploiter_robot.rewards / exploiter_robot.total_steps)

    # print("Exercise2::line_a::run_test::run_time", run_time,
    #      "reward", reward,
    #      "steps", steps,
    #      "ratio", ratio
    #      )
    return reward_per_step, upgrade_steps_matrix, exploiter_robot.position_history


def experiment(steps_for_test_list: list, qmatrix_update_function):
    metrics = []
    start = timeit.default_timer()
    for y in range(1, 20001):
        # random_qmatrix_update()
        qmatrix_update_function()

        if y in steps_for_test_list:
            sub__plot_index = steps_for_test_list.index(y) + 1
            plt.subplot(
                math.ceil(math.sqrt(len(steps_for_test_list))),
                math.ceil(math.sqrt(len(steps_for_test_list))),
                sub__plot_index)
            metrics.append(
                run_test(qmatrix=ex2_qmatrix, world=ex2_world, run_number=y, plot_qmatrix=True, upgrade_steps_matrix=y))
    stop = timeit.default_timer()
    experiment_time = stop - start
    ex2_qmatrix.reset()
    return metrics, experiment_time


def results_parser(results: list):
    # [30]EXP RESULTS
    #   runtime :int
    #   [4]
    #      (ratio,steps)
    #      [] steps history

    run_time_list = []
    avg_reward_per_step_list = []
    steps_upgraded_matrix = []
    ratio_list = []
    steps_taken_list = []
    averages = []

    # results has an entry for each experiment, each position has the results of one experiment
    for experiment_result in results:
        run_time_list.append(experiment_result[1])
        for result in experiment_result[0]:
            avg_reward_per_step_list.append(result[0])
            steps_upgraded_matrix.append(result[1])
            steps_taken_list.append(result[2])
    # run_time_average = sum(run_time_list) / len(run_time_list)
    # reward_average = sum(reward_list) / len(reward_list)
    # steps_average = sum(steps_list) / len(steps_list)
    # ratio_average = sum(ratio_list) / len(ratio_list)

    run_time_average = mean(run_time_list)
    # ratio_average = mean(ratio_list)
    avg_reward_zip_steps_upgrade = []
    for y in zip(avg_reward_per_step_list, steps_upgraded_matrix):
        avg_reward_zip_steps_upgrade.append(y)
    return run_time_average, avg_reward_zip_steps_upgrade


def plot_line_a(_tuple: Tuple[any, any, list]):
    run_time = _tuple[0]
    avg_reward_steps_list = _tuple[1]

    steps_list = []
    steps_upgrade_matrix = []
    for ratio_step in avg_reward_steps_list:
        steps_list.append(ratio_step[0])
        steps_upgrade_matrix.append(ratio_step[1])

    plt.scatter(steps_list, steps_upgrade_matrix)
    plt.ylabel("avg-reward")
    plt.xlabel("steps upgrade matrix")
    plt.show()


def _line_a():
    # test_ = [100, 1000, 10000, 20000]
    test_ = [100, 200, 500, 600, 700, 800, 900, 1000, 2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000]
    # test_ = [0,1,10,50,100,20000]

    experiment_results = []

    for _ in range(5):
        experiment_results.append(
            experiment(test_, random_qmatrix_update)
        )
    plt.tight_layout()
    plt.show()

    results_averages = results_parser(experiment_results)
    plot_line_a(results_averages)
    # plot(ratioList=test_ratio_list,
    #     rewardList=test_reward_list,
    #     stepsList=test_steps_list,
    #     timeList=test_run_time_list
    #     )

    # for metric in metrics:
    #    test_run_time_list.append(metric[0])
    #    test_reward_list.append(metric[1])
    #    test_steps_list.append(metric[2])
    #    test_ratio_list.append(metric[3])
    #    test_steps_taken_list.append(metric[4])

    # plt.tight_layout()
    # plt.show()

    # index = 1
    # for steps_taken_list_iterated in test_steps_taken_list:
    #    subplot = math.ceil(math.sqrt(len(test_steps_taken_list)))
    #    plt.subplot(subplot, subplot, index)
    #    matrix = generate_matrix_from_coordenates_list(steps_taken_list_iterated, ex2_world.collumns, ex2_world.rows)
    #    run_number = test_[index - 1]
    #    plt.title(str(run_number))
    #    sns.heatmap(matrix, annot=True, linewidths=0.1)
    #    index += 1

    # plt.tight_layout()
    # plt.show()


def _line_b():
    pass


if __name__ == "__main__":
    _line_a()
    _line_b()
