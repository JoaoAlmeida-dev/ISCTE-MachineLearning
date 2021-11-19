import time

import matplotlib.pyplot as plt
import numpy as np
import random

from Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator import generate_Points

alpha = 0.0001

def assign3_exercise1(seed:int):
    figure, axes = plt.subplots()

    a, b, c = generate_Points(plot=True, alpha=0.2, pointN=1000)
    r1ListBeggining: list = []
    r2ListBeggining: list = []
    #r3ListBeggining: list = []
    r1ListEndOfPassage: list = []
    r2ListEndOfPassage: list = []
    #r3ListEndOfPassage: list = []

    r1 = random.choice(c.T)
    r2 = random.choice(c.T)
    #r3 = random.choice(c.T)
    iterations = 100
    for i in range(iterations):
        for point in c.T:
            r1Closeness: float = ((r1[0] - point[0]) ** 2 + (r1[1] - point[1]) ** 2)**0.5
            r2Closeness: float = ((r2[0] - point[0]) ** 2 + (r2[1] - point[1]) ** 2)**0.5
            #r3Closeness: float = ((r3[0] - point[0]) ** 2 + (r3[1] - point[1]) ** 2)**0.5
            # print(point_index,r1Closeness,r2Closeness)
            if min(r1Closeness,r2Closeness) == r1Closeness:
            #if min(r1Closeness,r2Closeness,r3Closeness) == r1Closeness:
                r1 = (1 - alpha) * r1 + alpha * point
            elif min(r1Closeness,r2Closeness) == r2Closeness:
            #elif min(r1Closeness,r2Closeness,r3Closeness) == r2Closeness:
                r2 = (1 - alpha) * r2 + alpha * point
            #else:
                #r3 = (1 - alpha) * r3 + alpha * point

            if i == 0:
                r1ListBeggining.append((r1[0], r1[1]))
                r2ListBeggining.append((r2[0], r2[1]))
                #r3ListBeggining.append((r3[0], r3[1]))
        r1ListEndOfPassage.append((r1[0], r1[1]))
        r2ListEndOfPassage.append((r2[0], r2[1]))
        #r3ListEndOfPassage.append((r3[0], r3[1]))

    exercise1_plot(
        [r1ListBeggining, r2ListBeggining ], #r3ListBeggining],
        [r1ListEndOfPassage, r2ListEndOfPassage]#r3ListEndOfPassage])
    )

    axes.set_aspect(1)




def exercise1_plot(beggining_list,ending_list):
    plt.title("seed=" + str(seed)+" alpha="+str(alpha))

    transposed_beggining_list:[]=[]
    for list in beggining_list:
        transposed_beggining_list.append(np.asarray(list).T)

    transposed_ending_list:[]=[]
    for list in ending_list:
        transposed_ending_list.append(np.asarray(list).T)

    for list_index in range(len(transposed_beggining_list)):
        plt.scatter(transposed_beggining_list[list_index][0], transposed_beggining_list[list_index][1], label="r"+str(list_index)+"ListBeggining")

    for list_index in range(len(transposed_ending_list)):
        plt.scatter(transposed_ending_list[list_index][0], transposed_ending_list[list_index][1], label="r"+str(list_index)+"ListEndOfPassage")


if __name__ == '__main__':
    seed = np.random.randint(0, 1000)
    #seed = 356
    seed = 456
    #seed = 144
    np.random.seed(seed)
    random.seed(seed)
    print("seed=", seed)
    start = time.perf_counter()

    assign3_exercise1(seed=seed)

    stop = time.perf_counter()
    print("time=",stop-start)

    plt.tight_layout()
    plt.legend()
    plt.show()
