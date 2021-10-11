import builtins

from Week3 import World
from Week3.Stats import actions, pretty_print


def setQmatrix(states: int, actionN: int):
    outerList = []

    for y in range(states):
        innerList = []
        for x in range(actionN):
            innerList.append(0)
        outerList.insert(y, innerList)

    return outerList


class Qmatrix():

    def __init__(self, world: World, states: int):
        self.matrix = setQmatrix(states, len(actions))
        self.world = world

    def update_quality(self, s: int, a: str):
        alfa = 0.7
        discount = 0.99

        nextState = self.world.nextState(s, a)
        rs = self.world.reward(nextState)
        actionnum = actions.index(a)

        self.matrix[s][actionnum] = (1 - alfa) * self.matrix[s][actionnum] + alfa * (
                rs + discount * self.max_quality(nextState))

    def decode_action(self, state, value):
        qualityState = self.matrix[state]
        index = qualityState.index(value)
        return actions[index]

    def max_quality(self, s):
        return max(self.matrix[s - 1], default=0)
        # actions.index(randomAction()))

    def choose_best(self, world: World, state: int) -> str:
        qualityCopy = self.matrix[state - 1].copy()

        maxquality = self.max_quality(state)

        action = self.decode_action(state - 1, maxquality)
        while not world.walkable(state, action):
            qualityCopy[qualityCopy.index(maxquality)] = -1
            maxquality = builtins.max(qualityCopy)
            action = actions[qualityCopy.index(maxquality)]
        return action

    def transform(self):
        outerList = []
        i = 1
        for y in range(self.world.height):
            innerList = []
            for x in range(1, self.world.width + 1):
                innerList.append(self.max_quality(i))
                i = i + 1
            outerList.insert(y, innerList)

        pretty_print(outerList, "Qmatrix::transform")

        return outerList
