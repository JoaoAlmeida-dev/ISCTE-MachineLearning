import timeit
import matplotlib.pyplot as plt

from Week3.Plot import plot
from Week3.Qmatrix import Qmatrix
from Week3.Stats import *
from Week3.Robot import Robot
from Week3.Stats import randomAction
from Week3.World import World
import seaborn as sns

sns.set_theme()


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
        print("Main::randomRun", "==================", "iteration", test, "==================")

        start = timeit.default_timer()
        for x in range(1000):
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
        testBot.quality_walk(quality)

        # print("Main-qualityRun","State:", testBot.state)
        # print("Main-qualityRun","Qualities", quality.matrix[testBot.state - 1])

    print("Main::qualityRun", "Walked:", testBot.statesWalked)

    # stop = timeit.default_timer()
    # timeList.append(stop - start)

    return testBot.rewards / testBot.steps


def random_qwalk():
    # random.seed(6)

    width = 10
    height = 10
    rewardState = 100

    gameWorld = World(width=width, height=height, rewardState=rewardState, initialState=0, worldReward=100)
    quality = Qmatrix(world=gameWorld, states=width * height)
    testBot = Robot(rewards=0, steps=0, world=gameWorld)
    n1 = 5000
    n2 = 10000
    n3 = 15000
    n4 = 20000

    for x in range(1):
        # print("==================", "iteration", x, "==================")
        for test in range(20000):
            testBot.random_quality_maping_walk(quality)

            # start = timeit.default_timer()
            # while not testBot.reachgoal:

            if test == n1 - 1:
                plt.subplot(2, 2, 1)
                testrun(quality, n1)
            elif test == n2 - 1:
                plt.subplot(2, 2, 2)
                testrun(quality, n2)
            elif test == n3 - 1:
                plt.subplot(2, 2, 3)
                testrun(quality, n3)
            elif test == n4 - 1:
                plt.subplot(2, 2, 4)
                testrun(quality, n4)
                pretty_print(quality.matrix, "Main::random_qwalk")

            # stop = timeit.default_timer()
            # testBot.reset()

    # plt.imshow(quality.transform())
    plt.tight_layout()
    plt.show()
    # plot(ratioList, rewardList, stepsList, timeList)


def testrun(quality, run: int):
    # plt.imshow(quality.transform())
    title = "run n" + str(run)
    plt.title(title)
    # plt.show()
    sns.heatmap(quality.transform(), annot=True, fmt=".2F", annot_kws={"fontsize": 7})
    print("Main::testrun:", "run", run, ", ratio:", qualityRun(quality))


if __name__ == "__main__":
    # ex 1
    # randomRun()
    # ex 2
    random_qwalk()
