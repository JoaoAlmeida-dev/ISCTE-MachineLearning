import random

from Assignment1_ReinforcedLearning_Qmatrix.Logic.Constants import EXPERIMENT_MAX_STEPS, GREED_THRESHOLD, STARTING_GREED_INCREMENTAL, \
    CONSTANT_GREED
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Helpers import random_action
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Qmatrix import Qmatrix
from Assignment1_ReinforcedLearning_Qmatrix.Logic.Robot import Robot
from Assignment1_ReinforcedLearning_Qmatrix.Logic.World import World


def line_a_random_qmatrix_update(steps: int, robot: Robot, qmatrix: Qmatrix, world: World,error_chance:float):
    action = random_action()
    current_pos = robot.current_pos

    next_state = world.next_state(_action_index=action, _current_pos=current_pos,_error_chance=error_chance)[0]
    world.walk(_robot=robot, _action=action, _end_of_episode=True,_error_chance=error_chance)
    qmatrix.update_state(_current_pos=current_pos, _action_index=action, _next_pos=next_state)


def line_b_best_qmatrix_update(steps: int, robot: Robot, qmatrix: Qmatrix, world: World,error_chance:float):
    current_pos = robot.current_pos
    action = qmatrix.best_action(current_pos)

    next_state = world.next_state(_action_index=action, _current_pos=current_pos,_error_chance=error_chance)[0]
    world.walk(_robot=robot, _action=action, _end_of_episode=True,_error_chance=error_chance)
    qmatrix.update_state(_current_pos=current_pos, _action_index=action, _next_pos=next_state)


def greed_qmatrix_update(steps: int, robot: Robot, qmatrix: Qmatrix, world: World,error_chance:float):
    _greed: float = CONSTANT_GREED
    _temp_random: float = random.random()
    _random_action: bool = _temp_random > _greed
    current_pos = robot.current_pos

    if _random_action:
        action = random_action()
    else:
        action = qmatrix.best_action(current_pos)

    next_state = world.next_state(_action_index=action, _current_pos=current_pos,_error_chance=error_chance)[0]
    world.walk(_robot=robot, _action=action, _end_of_episode=True,_error_chance=error_chance)
    qmatrix.update_state(_current_pos=current_pos, _action_index=action, _next_pos=next_state)


def incremental_greed_qmatrix_update(steps: int, robot: Robot, qmatrix: Qmatrix, world: World,error_chance:float):
    _starting_greed: float = STARTING_GREED_INCREMENTAL
    _incremental_threshold: float = GREED_THRESHOLD

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

    next_state = world.next_state(_action_index=action, _current_pos=current_pos,_error_chance=error_chance)[0]
    world.walk(_robot=robot, _action=action, _end_of_episode=True,_error_chance=error_chance)
    qmatrix.update_state(_current_pos=current_pos, _action_index=action, _next_pos=next_state)
