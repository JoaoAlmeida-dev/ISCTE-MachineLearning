

class World:

    def __init__(self, width, height, rewardState, initialState, worldReward):
        self.width = width
        self.height = height
        self.rewardState = rewardState
        self.worldReward = worldReward
        self.initialState = initialState
        self.matrix = self.setMatrix(width, height)

    def nextState(self, s, a):
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

    def reward(self, s):
        if s == self.rewardState:
            print("REWARDS")
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

    def setMatrix(self,width, height):
        outerList = []
        i = 0
        for y in range(height):
            innerList = []
            for x in range(1, width + 1):
                innerList.append(x + i)
            outerList.insert(y, innerList)
            i = i + width

        return outerList