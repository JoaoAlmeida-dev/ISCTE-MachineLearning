import timeit
import matplotlib.pyplot as plt

from Week3.Qmatrix import Qmatrix
from Week3.Stats import *
from Week3.Robot import Robot
from Week3.Stats import randomAction
from Week3.World import World


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


def randomRun():
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


def qualityRun(quality):
    gameWorld = World(10, 10, 100, 1, 100)
    testBot = Robot(0, 0, gameWorld)

    # start = timeit.default_timer()
    for x in range(1000):
        testBot.qualityWalk(quality)

        print("State:",testBot.state)
        print("Qualities",quality.matrix[testBot.state-1])

    print("Walked:", testBot.statesWalked)

    # stop = timeit.default_timer()

    # timeList.append(stop - start)

    return testBot.rewards / testBot.steps


def randomQWalk():
    random.seed(6)

    width = 10
    height = 10
    rewardState = 100

    gameWorld = World(width, height, rewardState, 0, 100)
    quality = Qmatrix(gameWorld, width * height)
    testBot = Robot(0, 0, gameWorld)

    for x in range(1):
        # print("==================", "iteration", x, "==================")
        for test in range(2000):

            # start = timeit.default_timer()
            # while not testBot.reachgoal:
            if test == 1000:
                plt.imshow(quality.transform())
                plt.show()
                print("run 1000 ratio:", qualityRun(quality))
            # elif test == 1999:
            # print("run 1000",qualityRun(quality))
            testBot.randomQualityMapingWalk(quality)
            # stop = timeit.default_timer()

            # testBot.reset()

    plt.imshow(quality.transform())
    plt.show()
    # plot(ratioList, rewardList, stepsList, timeList)


if __name__ == "__main__":
    randomQWalk()
