from Week3 import World
from Week3.Stats import actions


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

    def updateQ(self, s: int, a: str):
        alfa = 0.7
        discount = 0.99

        nextState = self.world.nextState(s, a)
        rs = self.world.reward(nextState)
        actionnum = actions.index(a)

        self.matrix[s][actionnum] = (1 - alfa) * self.matrix[s][actionnum] + alfa * (
                rs + discount * self.maxQ(nextState))

    def maxQ(self, s):
        return max(self.matrix[s - 1], default=0)
        # actions.index(randomAction()))

    def chooseBest(self, world: World, state: int) -> str:
        max = self.maxQ(state)
        return world.walkable(state, self.decodeAction(state-1, max))

    def transform(self):
        outerList = []
        i = 1
        for y in range(self.world.height):
            innerList = []
            for x in range(1, self.world.width + 1):
                innerList.append(self.maxQ(i))
                i = i + 1
            outerList.insert(y, innerList)

        print(outerList)
        return outerList

    def decodeAction(self, state, value):
        qualityState = self.matrix[state]
        index = qualityState.index(value)
        return actions[index]
