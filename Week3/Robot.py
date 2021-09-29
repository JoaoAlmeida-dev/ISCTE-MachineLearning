
class Robot:
    def __init__(self, rewards, steps, world):
        self.world = world
        self.rewards = rewards
        self.steps = steps
        self.state = world.initialState
        self.reachgoal = False

    def walk(self, action):
        self.steps = self.steps + 1
        self.state = self.world.nextState(self.state, action)
        self.world.endOfEpisode(self)

    def reset(self):
        self.reachgoal = False
        self.rewards = 0
        self.steps = 0
        self.state = self.world.initialState