import random

from Assignment1.Exercises.Exercise2 import framework, EXPERIMENT_MAX_STEPS
from Assignment1.Logic.Helpers import random_action
from Assignment1.Logic.Qmatrix import Qmatrix
from Assignment1.Logic.Robot import Robot
from Assignment1.Logic.World import World

greed_threshold = 30
starting_greed_incremental = 0.9

STARTING_POS = (0, 0)
ex3_world = World(_collumns=10, _rows=10, _reward_state=(9, 9))
ex3_robot = Robot(starting_pos=STARTING_POS)
ex3_qmatrix = Qmatrix(_world=ex3_world)


def greed_qmatrix_update(steps: int):
    _greed: float = 1
    _temp_random: float = random.random()
    _random_action: bool = _temp_random > _greed
    current_pos = ex3_robot.current_pos

    if _random_action:
        action = random_action()
    else:
        action = ex3_qmatrix.best_action(current_pos)

    next_state = ex3_world.next_state(_action_index=action, _current_pos=current_pos)
    ex3_world.walk(_robot=ex3_robot, _action=action, _end_of_episode=True)
    ex3_qmatrix.update_state(_current_pos=current_pos, _action_index=action, _next_pos=next_state)


def incremental_greed_qmatrix_update(steps: int):
    _starting_greed: float = starting_greed_incremental
    _incremental_threshold:float = greed_threshold

    _step_percentage:float = steps * 100 / EXPERIMENT_MAX_STEPS

    if _step_percentage < _incremental_threshold:
        _current_greed: float = _starting_greed
    else:
        left_greed = 1 - _starting_greed
        _added_percentage = left_greed * (steps / EXPERIMENT_MAX_STEPS)
        _current_greed: float = _starting_greed + _added_percentage

    #print("current_greed=",_current_greed, "step_percentage=",_step_percentage)
    _temp_random: float = random.random()
    _random_action: bool = _temp_random > _current_greed
    current_pos = ex3_robot.current_pos

    if _random_action:
        action = random_action()
    else:
        action = ex3_qmatrix.best_action(current_pos)

    next_state = ex3_world.next_state(_action_index=action, _current_pos=current_pos)
    ex3_world.walk(_robot=ex3_robot, _action=action, _end_of_episode=True)
    ex3_qmatrix.update_state(_current_pos=current_pos, _action_index=action, _next_pos=next_state)


def _line_a():
    #constant greed
    framework(qmatrix_update_function=greed_qmatrix_update,
              qmatrix=ex3_qmatrix,
              world=ex3_world,
              plot_qmatrix=True
              )


def _line_b():
    #incremental greed
    framework(qmatrix_update_function=incremental_greed_qmatrix_update,
              qmatrix=ex3_qmatrix,
              world=ex3_world,
              plot_qmatrix=True
              )


if __name__ == "__main__":
    random.seed(1)
    _line_a()
    #starting_greed_incremental=0.3
    #_line_b()
    #starting_greed_incremental=0.6
    #_line_b()
    #starting_greed_incremental=0.9
    #_line_b()
