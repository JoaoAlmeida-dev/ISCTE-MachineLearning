from matplotlib import pyplot as plt

from Week3.Stats import mean, deviation


#def plot(ratioList: list[float], rewardList: list[int], stepsList: list[int], timeList: list[float]):
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
    plt.title("Steps")
    plt.plot(stepsList)
    print("Plot::plot stepsMean", mean(stepsList))
    print("Plot::plot stepsDeviation", deviation(stepsList))

    plt.subplot(2, 2, 4)
    plt.title("Ratios")
    plt.plot(ratioList)
    print("Plot::plot ratiosMean", mean(ratioList))
    print("Plot::plot ratiosDeviation", deviation(ratioList))
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
