import random

from Assignment1.Logic.Constants import EXPERIMENT_MAX_STEPS, greed_threshold, starting_greed_incremental
from Assignment1.Logic.Helpers import random_action
from Assignment1.Logic.Qmatrix import Qmatrix
from Assignment1.Logic.Robot import Robot
from Assignment1.Logic.World import World


def line_a_random_qmatrix_update(steps: int, robot: Robot, qmatrix: Qmatrix, world: World):
    action = random_action()
    current_pos = robot.current_pos

    next_state = world.next_state(_action_index=action, _current_pos=current_pos)
    world.walk(_robot=robot, _action=action, _end_of_episode=True)
    qmatrix.update_state(_current_pos=current_pos, _action_index=action, _next_pos=next_state)


def line_b_best_qmatrix_update(steps: int, robot: Robot, qmatrix: Qmatrix, world: World):
    current_pos = robot.current_pos
    action = qmatrix.best_action(current_pos)

    next_state = world.next_state(_action_index=action, _current_pos=current_pos)
    world.walk(_robot=robot, _action=action, _end_of_episode=True)
    qmatrix.update_state(_current_pos=current_pos, _action_index=action, _next_pos=next_state)


def greed_qmatrix_update(steps: int, robot: Robot, qmatrix: Qmatrix, world: World):
    _greed: float = 1
    _temp_random: float = random.random()
    _random_action: bool = _temp_random > _greed
    current_pos = robot.current_pos

    if _random_action:
        action = random_action()
    else:
        action = qmatrix.best_action(current_pos)

    next_state = world.next_state(_action_index=action, _current_pos=current_pos)
    world.walk(_robot=robot, _action=action, _end_of_episode=True)
    qmatrix.update_state(_current_pos=current_pos, _action_index=action, _next_pos=next_state)


def incremental_greed_qmatrix_update(steps: int, robot: Robot, qmatrix: Qmatrix, world: World):
    _starting_greed: float = starting_greed_incremental
    _incremental_threshold: float = greed_threshold

    _step_percentage: float = steps * 100 / EXPERIMENT_MAX_STEPS

    if _step_percentage < _incremental_threshold:
        _current_greed: float = _starting_greed
    else:
        left_greed = 1 - _starting_greed
        _added_percentage = left_greed * (steps / EXPERIMENT_MAX_STEPS)
        _current_greed: float = _starting_greed + _added_percentage

    # print("current_greed=",_current_greed, "step_percentage=",_step_percentage)
    _temp_random: float = random.random()
    _random_action: bool = _temp_random > _current_greed
    current_pos = robot.current_pos

    if _random_action:
        action = random_action()
    else:
        action = qmatrix.best_action(current_pos)

    next_state = world.next_state(_action_index=action, _current_pos=current_pos)
    world.walk(_robot=robot, _action=action, _end_of_episode=True)
    qmatrix.update_state(_current_pos=current_pos, _action_index=action, _next_pos=next_state)
