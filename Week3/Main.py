import random
import timeit
import matplotlib.pyplot as plt
import pandas as pd

from Week3.Stats import *
from Week3.Robot import Robot
from Week3.World import World


def randomAction():
    actions = ["left", "right", "down", "up"]
    return actions[random.randint(0, 3)]


def plot(ratioList, rewardList, stepsList, timeList):
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


def main():
    # world1 = World(10, 10, 100, 0, 100)
    # print("world matrix:", world1.matrix)
    # print("nextState of 21 going down:", world1.nextState(21, "down"))
    # print("nextState of 19 going right:", world1.nextState(19, "right"))
    # print("nextState of 0 going left:", world1.nextState(0, "left"))

    # print("Random Action:", randomAction())

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

    plot(ratioList, rewardList, stepsList, timeList)


if __name__ == "__main__":
    main()
