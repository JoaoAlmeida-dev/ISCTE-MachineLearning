import random
import timeit
import matplotlib.pyplot as plt
import pandas as pd


class World:

    def __init__(self, width, height, rewardState, initialState, worldReward):
        self.width = width
        self.height = height
        self.rewardState = rewardState
        self.worldReward = worldReward
        self.initialState = initialState
        self.matrix = setMatrix(width, height)

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


def setMatrix(width, height):
    outerList = []
    i = 0
    for y in range(height):
        innerList = []
        for x in range(1, width + 1):
            innerList.append(x + i)
        outerList.insert(y, innerList)
        i = i + width

    return outerList


world1 = World(10, 10, 100, 0, 100)
print("world matrix:", world1.matrix)
print("nextState of 21 going down:", world1.nextState(21, "down"))
print("nextState of 19 going right:", world1.nextState(19, "right"))
print("nextState of 0 going left:", world1.nextState(0, "left"))


def randomAction():
    actions = ["left", "right", "down", "up"]
    return actions[random.randint(0, 3)]


print("Random Action:", randomAction())


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


def deviation(list):
    mean = sum(list) / len(list)
    variance = sum([((x - mean) ** 2) for x in list]) / len(list)
    res = variance ** 0.5
    return str(res)


def mean(list):
    return sum(list) / len(list)


def main():
    random.seed(10)

    gameWorld = World(10, 10, 100, 0, 100)
    testBot = Robot(0, 0, gameWorld)

    timeList = []
    rewardList = []
    stepsList = []
    ratioList = []

    for test in range(30):
        print("==================", "iteration", test, "==================")
        start = timeit.default_timer()
        while not testBot.reachgoal:
            testBot.walk(randomAction())
        stop = timeit.default_timer()

        timeList.append(stop - start)
        rewardList.append(testBot.rewards)
        stepsList.append(testBot.steps)
        ratioList.append(testBot.rewards / testBot.steps)

        testBot.reset()

    plt.subplot(2, 2, 1)
    plt.title("Times")
    plt.plot(timeList)
    print("timeMean", mean(timeList))
    print("timeDeviation", deviation(timeList))

    plt.subplot(2, 2, 2)
    plt.title("Rewards")
    plt.plot(rewardList)
    print("rewardMean", mean(rewardList))
    print("rewardDeviation", deviation(rewardList))

    plt.subplot(2, 2, 3)
    plt.title("Steps")
    plt.plot(stepsList)
    print("stepsMean", mean(stepsList))
    print("stepsDeviation", deviation(stepsList))

    plt.subplot(2, 2, 4)
    plt.title("Ratios")
    plt.plot(ratioList)
    print("ratiosMean", mean(ratioList))
    print("ratiosDeviation", deviation(ratioList))

    plt.tight_layout()
    plt.show()

    plt.subplot(2, 2, 1)
    plt.title("Times")
    plt.boxplot(timeList)

    plt.subplot(2, 2, 2)
    plt.title("Rewards")
    plt.boxplot(rewardList)

    plt.subplot(2, 2, 3)
    plt.title("Steps")
    plt.boxplot(stepsList)

    plt.subplot(2, 2, 4)
    plt.title("Ratios")
    plt.boxplot(ratioList)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
