from typing import List


class Robot:

    def __init__(self, starting_pos: (int, int) = (0, 0)):
        self.position_history: List[(int, int)] = []
        self.rewards: int = 0
        self.steps: int = 0
        self.current_pos: (int, int) = starting_pos
        self.initial_pos: (int, int) = starting_pos
        self.steps_per_reward: List[int] = []
        self.total_steps = 0

    def reset(self):
        self.rewards = 0
        self.steps = 0
        self.current_pos = self.initial_pos
        self.position_history = []
        self.steps_per_reward: List[int] = []
        self.total_steps = 0

    def set_pos(self, new_pos: (int, int)):
        self.current_pos = new_pos
        self.position_history.append(new_pos)

    def move(self, new_pos: (int, int), reward: int):
        self.current_pos = new_pos
        self.position_history.append(new_pos)
        self.total_steps += 1
        self.steps += 1
        self.rewards += reward
        if reward != 0:
            self.steps_per_reward.append(self.steps)
            self.steps = 0