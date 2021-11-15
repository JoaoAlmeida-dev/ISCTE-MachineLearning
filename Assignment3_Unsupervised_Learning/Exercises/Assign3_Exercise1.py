import matplotlib.pyplot as plt
import numpy as np
import random

from Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator import generate_Points

alpha = 10E-3

def assign3_exercise1(seed:int):
    figure, axes = plt.subplots()

    a, b, c = generate_Points(plot=True, alpha=0.2, pointN=1000)
    r1ListBeggining: list = []
    r2ListBeggining: list = []
    r3ListBeggining: list = []
    r1ListEndOfPassage: list = []
    r2ListEndOfPassage: list = []
    r3ListEndOfPassage: list = []

    r1 = random.choice(c.T)
    r2 = random.choice(c.T)
    r3 = random.choice(c.T)
    iterations = 10
    for i in range(iterations):
        for point in c.T:
            r1Closeness: float = ((r1[0] - point[0]) ** 2 + (r1[1] - point[1]) ** 2)**0.5
            r2Closeness: float = ((r2[0] - point[0]) ** 2 + (r2[1] - point[1]) ** 2)**0.5
            r3Closeness: float = ((r3[0] - point[0]) ** 2 + (r3[1] - point[1]) ** 2)**0.5
            # print(point_index,r1Closeness,r2Closeness)
            if min(r1Closeness,r2Closeness,r3Closeness) == r1Closeness:
                r1 = (1 - alpha) * r1 + alpha * point
            elif min(r1Closeness,r2Closeness,r3Closeness) == r2Closeness:
                r2 = (1 - alpha) * r2 + alpha * point
            else:
                r3 = (1 - alpha) * r3 + alpha * point

            if i == 0:
                r1ListBeggining.append((r1[0], r1[1]))
                r2ListBeggining.append((r2[0], r2[1]))
                r3ListBeggining.append((r3[0], r3[1]))
        r1ListEndOfPassage.append((r1[0], r1[1]))
        r2ListEndOfPassage.append((r2[0], r2[1]))
        r3ListEndOfPassage.append((r3[0], r3[1]))

    exercise1_plot(
        [r1ListBeggining, r2ListBeggining, r3ListBeggining],
        [r1ListEndOfPassage, r2ListEndOfPassage, r3ListEndOfPassage])

    axes.set_aspect(1)
    plt.title("seed=" + str(seed)+" alpha="+str(alpha))
    plt.tight_layout()
    plt.legend()
    plt.show()


def exercise1_plot(beggining_list,ending_list):
    transposed_beggining_list:[]=[]
    for list in beggining_list:
        transposed_beggining_list.append(np.asarray(list).T)

    transposed_ending_list:[]=[]
    for list in ending_list:
        transposed_ending_list.append(np.asarray(list).T)

    #r1ListBeggining_NPArray_T = np.asarray(r1ListBeggining).T
    #r2ListBeggining_NPArray_T = np.asarray(r2ListBeggining).T
#
    #r1ListEndOfPassage_NPArray_T = np.asarray(r1ListEndOfPassage).T
    #r2ListEndOfPassage_NPArray_T = np.asarray(r2ListEndOfPassage).T

    for list_index in range(len(transposed_beggining_list)):
        plt.scatter(transposed_beggining_list[list_index][0], transposed_beggining_list[list_index][1], label="r"+str(list_index)+"ListBeggining")

    for list_index in range(len(transposed_ending_list)):
        plt.scatter(transposed_ending_list[list_index][0], transposed_ending_list[list_index][1], label="r"+str(list_index)+"ListEndOfPassage")

    #plt.scatter(r1ListBeggining_NPArray_T[0], r1ListBeggining_NPArray_T[1], label="r1ListBeggining")
    #plt.scatter(r2ListBeggining_NPArray_T[0], r2ListBeggining_NPArray_T[1], label="r2ListBeggining")
#
    #plt.scatter(r1ListEndOfPassage_NPArray_T[0], r1ListEndOfPassage_NPArray_T[1], label="r1ListEndOfPassage")
    #plt.scatter(r2ListEndOfPassage_NPArray_T[0], r2ListEndOfPassage_NPArray_T[1], label="r2ListEndOfPassage")


if __name__ == '__main__':
    seed = np.random.randint(0, 1000)
    #seed = 356
    #seed = 456
    np.random.seed(seed)
    random.seed(seed)
    print("seed=", seed)
    assign3_exercise1(seed=seed)
