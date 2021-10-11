class Robot:

    def __init__(self, starting_pos: (int, int) = (0, 0)):
        self.rewards: int = 0
        self.steps: int = 0
        self.current_pos: (int, int) = starting_pos
        self.initial_pos: (int, int) = starting_pos

    def reset(self):
        self.rewards = 0
        self.steps = 0
        self.current_pos = self.initial_pos

    def set_pos(self, new_pos: (int, int)):
        self.current_pos = new_pos
