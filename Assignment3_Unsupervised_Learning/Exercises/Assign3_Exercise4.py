import random

import matplotlib.pyplot as plt
import numpy as np

from Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator import generate_Points
from Assignment3_Unsupervised_Learning.Logic.Assign3_ex4_Cluster import Cluster


def distance_between(point_a: np.ndarray, point_b: np.ndarray) -> float:
    return np.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2)


def point_get_Epsylon_points(point: np.ndarray, point_list: [np.ndarray], epsilon: float) -> [np.ndarray]:
    _epsilon_points_list: [np.ndarray] = []
    for point_from_list in point_list:
        if distance_between(point_from_list, point) < epsilon:
            _epsilon_points_list.append(point_from_list)
    return _epsilon_points_list


def assign3_exercise4(epsilon:float):
    cluster_list: [Cluster] = []
    a, b, c = generate_Points(plot=True, alpha=1, pointN=1000)
    points_lst: list = c.T.copy().tolist()

    while len(points_lst) > 0:
        cluster = Cluster.create_cluster(points_lst)
        cluster_list.append(cluster)
        cluster_points = cluster.getPoints()

        points_lst.remove(cluster_points)




    plt.legend()
    plt.show()


if __name__ == '__main__':
    seed: int = random.randint(0, 10000)
    # seed = 4670
    # good seed 4756
    # good seed 4670
    np.random.seed(seed)
    random.seed(seed)
    epsilon = random.random()
    assign3_exercise4(epsilon)
