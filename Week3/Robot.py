from Week3 import World
from Week3.Stats import randomAction


class Robot:

    def __init__(self, rewards: int, steps: int, world: World):
        self.world = world
        self.rewards = rewards
        self.steps = steps
        self.state = world.initialState
        self.reachgoal = False
        self.statesWalked = []

    def walk(self, action: str):
        self.steps = self.steps + 1
        self.state = self.world.nextState(self.state, action)
        self.statesWalked.append(self.state)
        self.world.endOfEpisode(self)
        return self.state

    def qualityWalk(self, Qmatrix):
        # maxq = Qmatrix.maxQ(self.state)
        # action = Qmatrix.decodeAction(self.state-1, maxq)

        newstate = self.walk(Qmatrix.chooseBest(self.world, self.state))

        return self.state

    def randomQualityMapingWalk(self, Qmatrix):
        action = randomAction()
        currstate = self.state
        newstate = self.walk(action)

        Qmatrix.updateQ(currstate, action)
        while currstate == newstate:
            action = randomAction()
            newstate = self.walk(action)

        self.statesWalked.append(self.state)
        return newstate

    def randomWalk(self):
        currstate = self.state
        newstate = self.walk(randomAction())
        while currstate == newstate:
            newstate = self.walk(randomAction())
            self.statesWalked.append(self.state)
        return newstate

    def reset(self):
        self.reachgoal = False
        self.rewards = 0
        self.steps = 0
        self.state = self.world.initialState
