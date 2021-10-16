import numpy as np
from typing import List

from Week3_Remake.Logic.Constants import actions
from Week3_Remake.Logic.Robot import Robot


class World:

    penalty_positions = []
    penalty_value = 0

    def __init__(self, _collumns:int=10, _rows:int=10, _reward_state: (int, int) = (9, 9), _initial_state: (int, int) = (0, 0),
                 _penalty_position=None, _penalty_value=0):
        if _penalty_position is None:
            _penalty_position = []
        self.collumns: int = _collumns
        self.rows: int = _rows
        self.matrix: np.ndarray = World._create_matrix(_collumns=_collumns, _rows=_rows, _reward_state=_reward_state,
                                                       _penalty_pos=_penalty_position,
                                                       _penalty_value=_penalty_value)
        self.reward_state: (int, int) = _reward_state
        self.initial_state: (int, int) = _initial_state

    def pretty_print(self):
        for x in range(len(self.matrix)):
            print(self.matrix[x])

    def next_state(self, _action_index: int, _current_pos: (int, int)) -> (int, int):
        new_pos = list(_current_pos)

        if actions[_action_index] == "up" and _current_pos[0] > 0:
            new_pos[0] -= 1
        elif actions[_action_index] == "down" and _current_pos[0] < self.rows - 1:
            new_pos[0] += 1
        elif actions[_action_index] == "left" and _current_pos[1] > 0:
            new_pos[1] -= 1
        elif actions[_action_index] == "right" and _current_pos[1] < self.collumns - 1:
            new_pos[1] += 1
        return new_pos

    def reward(self, _pos: (int, int)) -> int:
        try:
            return self.matrix[_pos[0]][_pos[1]]
        except IndexError:
            return 0
#            if _pos[0] == self.reward_state[0] and _pos[1] == self.reward_state[1]:
#                return 100
#            elif _pos[0] < 0 or _pos[0] >= self.rows and _pos[1] < 0 or _pos[1] >= self.collumns:
#                return 0
#            else:
#                return 0

    def end_episode(self, _robot: Robot):
        if list(_robot.current_pos) == list(self.reward_state):
            self.reset_pos(_robot)

    def reset_pos(self, robot):
        robot.current_pos = self.initial_state

    def walk(self, _robot: Robot, _action: int, _end_of_episode:bool):
        next_state = self.next_state(_action_index=_action, _current_pos=_robot.current_pos)
        _robot.move(new_pos=next_state, reward=self.reward(next_state))
        if _end_of_episode:
            self.end_episode(_robot)
        #return _robot.current_pos

    @staticmethod
    def _create_matrix(_collumns: int, _rows: int, _reward_state: (int, int),
                       _penalty_pos=None    , _penalty_value: int = 0) -> np.ndarray:
        if _penalty_pos is None:
            _penalty_pos = []
        _matrix = np.full((_collumns, _rows), 0)
        _matrix[_reward_state[0]][_reward_state[0]] = 100
        for pos in _penalty_pos:
            _matrix[pos[0]][pos[1]] = _penalty_value
        return _matrix
