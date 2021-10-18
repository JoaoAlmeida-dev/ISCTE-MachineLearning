import random
import timeit

from Assignment1.Logic.Constants import actions
from Assignment1.Logic.Helpers import random_action
from Assignment1.Logic.Plot import plot_results
from Assignment1.Logic.Result import Result
from Assignment1.Logic.Robot import Robot
from Assignment1.Logic.World import World

ex1_world = World(_collumns=10, _rows=10, _reward_state=(9, 9))
ex1_robot = Robot(starting_pos=(0, 0))


def _setup():
    print(ex1_world.matrix)


def _line_a():
    x = (0, 0)
    print("Exercise1::line_a::", x, actions[0],
          ex1_world.next_state(_action_index=0, _current_pos=x, _error_chance=0))
    print("Exercise1::line_a::", x, actions[1],
          ex1_world.next_state(_action_index=1, _current_pos=x, _error_chance=0))
    print("Exercise1::line_a::", x, actions[2],
          ex1_world.next_state(_action_index=2, _current_pos=x, _error_chance=0))
    print("Exercise1::line_a::", x, actions[3],
          ex1_world.next_state(_action_index=3, _current_pos=x, _error_chance=0))
    print()

    x = (5, 5)
    print("Exercise1::line_a::", x, actions[0],
          ex1_world.next_state(_action_index=0, _current_pos=x, _error_chance=0))
    print("Exercise1::line_a::", x, actions[1],
          ex1_world.next_state(_action_index=1, _current_pos=x, _error_chance=0))
    print("Exercise1::line_a::", x, actions[2],
          ex1_world.next_state(_action_index=2, _current_pos=x, _error_chance=0))
    print("Exercise1::line_a::", x, actions[3],
          ex1_world.next_state(_action_index=3, _current_pos=x, _error_chance=0))
    print()
    x = (9, 9)
    print("Exercise1::line_a::", x, actions[0],
          ex1_world.next_state(_action_index=0, _current_pos=x, _error_chance=0))
    print("Exercise1::line_a::", x, actions[1],
          ex1_world.next_state(_action_index=1, _current_pos=x, _error_chance=0))
    print("Exercise1::line_a::", x, actions[2],
          ex1_world.next_state(_action_index=2, _current_pos=x, _error_chance=0))
    print("Exercise1::line_a::", x, actions[3],
          ex1_world.next_state(_action_index=3, _current_pos=x, _error_chance=0))
    print()


def _line_b():
    x = (0, 0)
    print("Exercise1::line_b::", x, ex1_world.reward(x))
    x = (5, 5)
    print("Exercise1::line_b::", x, ex1_world.reward(x))
    x = (9, 8)
    print("Exercise1::line_b::", x, ex1_world.reward(x))
    x = (10, 10)
    print("Exercise1::line_b::", x, ex1_world.reward(x))
    x = (-2, -2)
    print("Exercise1::line_b::", x, ex1_world.reward(x))
    print()


def _line_c():
    random_num = random_action()
    print("Exercise1::line_c::index:", random_num, "action", actions[random_num])
    random_num = random_action()
    print("Exercise1::line_c::index:", random_num, "action", actions[random_num])
    random_num = random_action()
    print("Exercise1::line_c::index:", random_num, "action", actions[random_num])
    random_num = random_action()
    print("Exercise1::line_c::index:", random_num, "action", actions[random_num])
    print()


def _line_d():
    ex1_robot.set_pos((9, 9))
    print("Exercise1::line_d::before:", ex1_robot.current_pos, ex1_world.end_episode(ex1_robot), "after",
          ex1_robot.current_pos)
    ex1_robot.set_pos((1, 1))
    print("Exercise1::line_d::before:", ex1_robot.current_pos, ex1_world.end_episode(ex1_robot), "after",
          ex1_robot.current_pos)
    ex1_robot.set_pos((5, 2))
    print("Exercise1::line_d::before:", ex1_robot.current_pos, ex1_world.end_episode(ex1_robot), "after",
          ex1_robot.current_pos)
    print()


def _line_e_f():
    ex1_world_line_e = World(_collumns=10, _rows=10, _reward_state=(9, 9))
    ex1_robot_line_e = Robot(starting_pos=(0, 0))

    run_time_list = []
    ratioList = []
    rewardList = []
    steps_list = []
    results_list = []
    steps_per_reward_list = []
    for x in range(30):
        start = timeit.default_timer()
        for y in range(1000):
            _action = random_action()
            ex1_world_line_e.walk(_robot=ex1_robot_line_e, _action=_action, _end_of_episode=True, _error_chance=0)
            # robot_line_e.current_pos = \
            #    world_line_e.next_state(_action_index=_action, _current_pos=robot_line_e.current_pos)
            # world_line_e.end_episode(robot_line_e)
            # robot_line_e.steps += 1
        stop = timeit.default_timer()

        results_list.append(Result(_rewards=ex1_robot_line_e.rewards,
                                   _steps_per_reward_mean=ex1_robot_line_e.get_steps_per_reward_mean(),
                                   _rewards_per_step=ex1_robot_line_e.rewards / ex1_robot_line_e.total_steps,
                                   _qmatrix_step=x)
                            )
        run_time_list.append(stop - start)
        # rewardList.append(ex1_robot_line_e.rewards)
        # ratioList.append(ex1_robot_line_e.rewards / ex1_robot_line_e.total_steps)

        for step in ex1_robot_line_e.steps_per_reward:
            steps_per_reward_list.append(step)

        # print("Exercise1::line_e::mean(steps_per_reward_list)",mean(steps_per_reward_list))

        ex1_robot_line_e.reset()
    print("Exercise1::line_e , line_f::", )

    # plot(ratioList=ratioList, rewardList=rewardList, stepsList=steps_mean_list, timeList=run_time_list)
    plot_results(results_list=results_list, timeList=run_time_list)
    print()


if __name__ == "__main__":
    random.seed(1)
    _setup()
    _line_a()
    _line_b()
    _line_c()
    _line_d()
    _line_e_f()
