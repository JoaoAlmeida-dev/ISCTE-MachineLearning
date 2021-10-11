import random

import numpy

from Week3.Plot import plot
from Week3_Remake.Logic.Constants import actions, random_action
from Week3_Remake.Logic.Robot import Robot
from Week3_Remake.Logic.World import World
import timeit

random.seed(1)

ex1_world = World(_collumns=10, _rows=10, _reward_state=(9, 9))
ex1_robot = Robot(starting_pos=(0, 0))


def setup():
    print(ex1_world.matrix)


def line_a():
    x = 0
    print("Exercise1::line_a::", x, x, actions[0],
          ex1_world.next_state(_action_index=0, current_row_index=x, current_collumn_index=x))
    print("Exercise1::line_a::", x, x, actions[1],
          ex1_world.next_state(_action_index=1, current_row_index=x, current_collumn_index=x))
    print("Exercise1::line_a::", x, x, actions[2],
          ex1_world.next_state(_action_index=2, current_row_index=x, current_collumn_index=x))
    print("Exercise1::line_a::", x, x, actions[3],
          ex1_world.next_state(_action_index=3, current_row_index=x, current_collumn_index=x))
    print()

    x = 5
    print("Exercise1::line_a::", x, x, actions[0],
          ex1_world.next_state(_action_index=0, current_row_index=x, current_collumn_index=x))
    print("Exercise1::line_a::", x, x, actions[1],
          ex1_world.next_state(_action_index=1, current_row_index=x, current_collumn_index=x))
    print("Exercise1::line_a::", x, x, actions[2],
          ex1_world.next_state(_action_index=2, current_row_index=x, current_collumn_index=x))
    print("Exercise1::line_a::", x, x, actions[3],
          ex1_world.next_state(_action_index=3, current_row_index=x, current_collumn_index=x))
    print()
    x = 9
    print("Exercise1::line_a::", x, x, actions[0],
          ex1_world.next_state(_action_index=0, current_row_index=x, current_collumn_index=x))
    print("Exercise1::line_a::", x, x, actions[1],
          ex1_world.next_state(_action_index=1, current_row_index=x, current_collumn_index=x))
    print("Exercise1::line_a::", x, x, actions[2],
          ex1_world.next_state(_action_index=2, current_row_index=x, current_collumn_index=x))
    print("Exercise1::line_a::", x, x, actions[3],
          ex1_world.next_state(_action_index=3, current_row_index=x, current_collumn_index=x))
    print()


def line_b():
    x = 0
    print("Exercise1::line_b::", x, x, ex1_world.reward(x, x))
    x = 5
    print("Exercise1::line_b::", x, x, ex1_world.reward(x, x))
    x = 9
    print("Exercise1::line_b::", x, x, ex1_world.reward(x, x))
    x = 10
    print("Exercise1::line_b::", x, x, ex1_world.reward(x, x))
    x = -2
    print("Exercise1::line_b::", x, x, ex1_world.reward(x, x))
    print()


def line_c():
    random_num = random_action()
    print("Exercise1::line_c::index:", random_num, "action", actions[random_num])
    random_num = random_action()
    print("Exercise1::line_c::index:", random_num, "action", actions[random_num])
    random_num = random_action()
    print("Exercise1::line_c::index:", random_num, "action", actions[random_num])
    random_num = random_action()
    print("Exercise1::line_c::index:", random_num, "action", actions[random_num])
    print()


def line_d():
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


def line_e_f():
    world_line_e = World(_collumns=10, _rows=10, _reward_state=(9, 9))
    robot_line_e = Robot(starting_pos=(0, 0))

    run_time_list = []
    ratioList = []
    rewardList = []
    stepsList = []
    for x in range(30):
        start = timeit.default_timer()
        for y in range(1000):
            robot_line_e.current_pos = \
                world_line_e.next_state(_action_index=random_action(), _current_pos=robot_line_e.current_pos)
            world_line_e.end_episode(robot_line_e)
            robot_line_e.steps += 1
        stop = timeit.default_timer()
        run_time_list.append(stop - start)
        rewardList.append(robot_line_e.rewards)
        stepsList.append(robot_line_e.steps)
        ratioList.append(robot_line_e.rewards / robot_line_e.steps)

        robot_line_e.reset()
    print("Exercise1::line_e , line_f::", )
    plot(ratioList=ratioList, rewardList=rewardList, stepsList=stepsList, timeList=run_time_list)
    print()


if __name__ == "__main__":
    setup()
    line_a()
    line_b()
    line_c()
    line_d()
    line_e_f()
