from matplotlib import pyplot as plt
from Week3.Stats import mean, deviation


# def plot(ratioList: list[float], rewardList: list[int], stepsList: list[int], timeList: list[float]):
def plot_results(results_list, timeList):
    rewardList = []
    steps_per_reward_List = []
    ratioList = []
    for result in results_list:
        rewardList.append(result.rewards)
        ratioList.append(result.rewards_per_step)
        steps_per_reward_List.append(result.steps_per_reward_mean)

    plot(ratioList=ratioList, rewardList=rewardList, stepsList=steps_per_reward_List, timeList=timeList)


def plot(ratioList, rewardList, stepsList, timeList):
    plt.subplot(2, 2, 1)
    plt.title("Times")
    plt.plot(timeList)
    print("Plot::plot timeMean", mean(timeList))
    print("Plot::plot timeDeviation", deviation(timeList))

    plt.subplot(2, 2, 2)
    plt.title("Rewards")
    plt.plot(rewardList)
    print("Plot::plot rewardMean", mean(rewardList))
    print("Plot::plot rewardDeviation", deviation(rewardList))

    plt.subplot(2, 2, 3)
    plt.title("Steps per Reward")
    plt.plot(stepsList)
    print("Plot::plot stepsMean", mean(stepsList))
    print("Plot::plot stepsDeviation", deviation(stepsList))

    plt.subplot(2, 2, 4)
    plt.title("Reward per step")
    plt.plot(ratioList)
    print("Plot::plot Reward per step-Mean", mean(ratioList))
    print("Plot::plot Reward per step-Deviation", deviation(ratioList))
    plt.tight_layout()
    plt.show()

    box_plot(ratioList, rewardList, stepsList, timeList)


def box_plot(ratioList, rewardList, stepsList, timeList):
    plt.subplot(1, 4, 1)
    plt.title("Times")
    plt.boxplot(timeList)

    plt.subplot(1, 4, 2)
    plt.title("Rewards")
    plt.boxplot(rewardList)

    plt.subplot(1, 4, 3)
    plt.title("Steps per Reward")
    plt.boxplot(stepsList)

    plt.subplot(1, 4, 4)
    plt.title("Reward per step")
    plt.boxplot(ratioList)

    plt.tight_layout()
    plt.show()
