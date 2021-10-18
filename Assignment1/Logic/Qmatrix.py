import numpy as np

from Assignment1.Logic.Constants import ACTIONS
from Assignment1.Logic.Helpers import max_index_of
from Assignment1.Logic.World import World


class Qmatrix:

    def __init__(self, _world: World):
        self.world: World = _world
        self.matrix = np.full((_world.rows, _world.collumns, len(ACTIONS)), 0)

    def update_state(self, _current_pos: (int, int), _action_index: int, _next_pos: (int, int)):
        alfa = 0.7
        discount = 0.99

        # quality_current_state = self.matrix[_current_pos[0]][_current_pos[1]][_action_index]
        # max_quality_next_state = max(self.matrix[_next_pos[0]][_next_pos[1]])
        # reward = self.world.reward(_current_pos)

        quality = (1 - alfa) \
                  * self.matrix[_current_pos[0]][_current_pos[1]][_action_index] \
                  + alfa * (
                          self.world.reward(_next_pos) + discount * max(self.matrix[_next_pos[0]][_next_pos[1]])
                  )
        self.matrix[_current_pos[0]][_current_pos[1]][_action_index] = quality

    def normalized(self):
        transformed_matrix = np.full(
            (len(self.matrix), len(self.matrix[0])), 0)
        for row in range(len(self.matrix)):
            for collumn in range(len(self.matrix[row])):
                transformed_matrix[row][collumn] = (max(self.matrix[row][collumn]))
        return transformed_matrix

    def best_action(self, pos: (int, int)) -> int:
        return max_index_of(self.matrix[pos[0]][pos[1]])

    def reset(self):
        self.matrix = np.full((self.world.rows, self.world.collumns, len(ACTIONS)), 0)
