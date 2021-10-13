import random

import numpy

from Week3_Remake.Logic.Helpers import mean
from Week3_Remake.Logic.Plot import plot
from Week3_Remake.Logic.Constants import actions, random_action
from Week3_Remake.Logic.Robot import Robot
from Week3_Remake.Logic.World import World
import timeit

random.seed(1)

ex1_world = World(_collumns=10, _rows=10, _reward_state=(9, 9))
ex1_robot = Robot(starting_pos=(0, 0))


def _setup():
    print(ex1_world.matrix)


def _line_a():
    x = (0, 0)
    print("Exercise1::line_a::", x, actions[0],
          ex1_world.next_state(_action_index=0, _current_pos=x))
    print("Exercise1::line_a::", x, actions[1],
          ex1_world.next_state(_action_index=1, _current_pos=x))
    print("Exercise1::line_a::", x, actions[2],
          ex1_world.next_state(_action_index=2, _current_pos=x))
    print("Exercise1::line_a::", x, actions[3],
          ex1_world.next_state(_action_index=3, _current_pos=x))
    print()

    x = (5, 5)
    print("Exercise1::line_a::", x, actions[0],
          ex1_world.next_state(_action_index=0, _current_pos=x))
    print("Exercise1::line_a::", x, actions[1],
          ex1_world.next_state(_action_index=1, _current_pos=x))
    print("Exercise1::line_a::", x, actions[2],
          ex1_world.next_state(_action_index=2, _current_pos=x))
    print("Exercise1::line_a::", x, actions[3],
          ex1_world.next_state(_action_index=3, _current_pos=x))
    print()
    x = (9, 9)
    print("Exercise1::line_a::", x, actions[0],
          ex1_world.next_state(_action_index=0, _current_pos=x))
    print("Exercise1::line_a::", x, actions[1],
          ex1_world.next_state(_action_index=1, _current_pos=x))
    print("Exercise1::line_a::", x, actions[2],
          ex1_world.next_state(_action_index=2, _current_pos=x))
    print("Exercise1::line_a::", x, actions[3],
          ex1_world.next_state(_action_index=3, _current_pos=x))
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
    _world_line_e = World(_collumns=10, _rows=10, _reward_state=(9, 9))
    _robot_line_e = Robot(starting_pos=(0, 0))

    run_time_list = []
    ratioList = []
    rewardList = []
    steps_list = []
    for x in range(30):
        start = timeit.default_timer()
        for y in range(1000):


            _action = random_action()
            _world_line_e.walk(_robot=_robot_line_e, _action=_action, _end_of_episode=True)
            # robot_line_e.current_pos = \
            #    world_line_e.next_state(_action_index=_action, _current_pos=robot_line_e.current_pos)
            # world_line_e.end_episode(robot_line_e)
            # robot_line_e.steps += 1
        stop = timeit.default_timer()

        run_time_list.append(stop - start)
        rewardList.append(_robot_line_e.rewards)
        ratioList.append(_robot_line_e.rewards / _robot_line_e.total_steps)

        steps_list.append(_robot_line_e.steps_per_reward)
        steps_mean_list = []
        for step in steps_list:
            steps_mean_list.append(mean(step))

        _robot_line_e.reset()
    print("Exercise1::line_e , line_f::", )
    plot(ratioList=ratioList, rewardList=rewardList, stepsList=steps_mean_list, timeList=run_time_list)
    print()


if __name__ == "__main__":
    _setup()
    _line_a()
    _line_b()
    _line_c()
    _line_d()
    _line_e_f()
