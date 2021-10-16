from matplotlib import pyplot as plt
from Assignment1.Logic.Helpers import mean, deviation


# def plot(ratioList: list[float], rewardList: list[int], stepsList: list[int], timeList: list[float]):
REWARDS_TITLE = "Rewards"
TIMES_TITLE = "Times"
STEPS_PER_REWARD_TITLE="Steps per Reward"
REWARD_PER_STEP_TITLE="Reward per step"

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
    plt.title(TIMES_TITLE)
    plt.plot(timeList)
    print("Plot::plot ",TIMES_TITLE,"Mean", mean(timeList))
    print("Plot::plot ",TIMES_TITLE,"Deviation", deviation(timeList))

    plt.subplot(2, 2, 2)
    plt.title(REWARDS_TITLE)
    plt.plot(rewardList)
    print("Plot::plot ",REWARDS_TITLE,"Mean", mean(rewardList))
    print("Plot::plot ",REWARDS_TITLE,"Deviation", deviation(rewardList))

    plt.subplot(2, 2, 3)
    plt.title(STEPS_PER_REWARD_TITLE)
    plt.plot(stepsList)
    print("Plot::plot ",STEPS_PER_REWARD_TITLE,"Mean", mean(stepsList))
    print("Plot::plot ",STEPS_PER_REWARD_TITLE,"Deviation", deviation(stepsList))

    plt.subplot(2, 2, 4)
    plt.title(REWARD_PER_STEP_TITLE)
    plt.plot(ratioList)
    print("Plot::plot ",REWARD_PER_STEP_TITLE,"-Mean", mean(ratioList))
    print("Plot::plot ",REWARD_PER_STEP_TITLE,"Deviation", deviation(ratioList))
    plt.tight_layout()
    plt.show()

    box_plot(ratioList, rewardList, stepsList, timeList)


def box_plot(ratioList, rewardList, stepsList, timeList):
    plt.subplot(1, 4, 1)
    plt.title(TIMES_TITLE)
    plt.boxplot(timeList)

    plt.subplot(1, 4, 2)
    plt.title(REWARDS_TITLE)
    plt.boxplot(rewardList)

    plt.subplot(1, 4, 3)
    plt.title(STEPS_PER_REWARD_TITLE)
    plt.boxplot(stepsList)

    plt.subplot(1, 4, 4)
    plt.title(REWARD_PER_STEP_TITLE)
    plt.boxplot(ratioList)

    plt.tight_layout()
    plt.show()
