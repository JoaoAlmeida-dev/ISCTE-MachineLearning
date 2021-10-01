def setMatrix(width: int, height: int):
    outerList = []
    i = 0
    for y in range(height):
        innerList = []
        for x in range(1, width + 1):
            # if filled:
            value = x + i
            # else:
            #  value = 0
            innerList.append(value)
        outerList.insert(y, innerList)
        i = i + width

    return outerList


class World:

    def __init__(self, width: int, height: int, rewardState: int, initialState: int, worldReward: int):
        self.width = width
        self.height = height
        self.rewardState = rewardState
        self.worldReward = worldReward
        self.initialState = initialState
        self.matrix = setMatrix(width, height)

    def nextState(self, s: int, a: str):
        if a == "up" and s > self.width:
            return s - self.width
        elif a == "down" and s < (self.height * self.width - self.width):
            return s + self.width
        elif a == "left" and s % self.width != 1:
            return s - 1
        elif a == "right" and s % self.width != 0:
            return s + 1
        else:
            return s

    def walkable(self, state: int, action: str) -> bool:
        if (action == "up" and state > self.width) \
                or (action == "down" and state < (self.height * self.width - self.width)) \
                or (action == "left" and state % self.width != 1) \
                or (action == "right" and state % self.width != 0):
            return True
        else:
            return False

    def reward(self, s: str):
        if s == self.rewardState:
            print("REWARD REACHED")
            return self.worldReward
        else:
            return 0

    def endOfEpisode(self, bot):
        if bot.state == self.rewardState:
            bot.rewards = bot.rewards + self.worldReward
            bot.reachgoal = True
            bot.state = self.initialState
        else:
            bot.state = bot.state
