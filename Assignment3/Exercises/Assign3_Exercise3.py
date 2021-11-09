import random
import numpy as np
from matplotlib import pyplot as plt

from Assignment3.Logic.Assign3_PointGenerator import generate_Points


def average_point(point_a: np.ndarray, point_b: np.ndarray) -> list:
    avg_x = (point_a[0] + point_b[0]) / 2
    avg_y = (point_a[1] + point_b[1]) / 2
    list = [avg_x, avg_y]

    return list


def distance_between(point_a: np.ndarray, point_b: np.ndarray) -> float:
    return np.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[0] - point_b[0]) ** 2)


def find_closest_two_points(points_lst: list) -> (np.ndarray, np.ndarray):
    point_a: np.ndarray = random.choice(points_lst)
    point_b: np.ndarray = random.choice(points_lst)
    shortest_distance: float = distance_between(point_a, point_b)

    for point1 in points_lst:
        for point2 in points_lst:
            if point1[0] != point2[0] and point1[1] != point2[1]:
                distance = distance_between(point1, point2)
                if distance < shortest_distance:
                    shortest_distance = distance
                    point_a = point1
                    point_b = point2
    return point_a, point_b


def assign3_exercise3():
    a, b, c = generate_Points(plot=True, pointN=200)
    points_lst: list = c.T.copy().tolist()
    initial_len = len(points_lst)
    lens_for_analysis = [(initial_len / 4) * 1 - 1, (initial_len / 4) * 2 - 1, (initial_len / 4) * 3 - 1,
                         (initial_len / 4) * 4 - 1]
    point_for_analysis = []
    points_lst_Length = len(points_lst)
    while points_lst_Length > 2:

        point_a, point_b = find_closest_two_points(points_lst)
        point_avg = average_point(point_a, point_b)
        if points_lst_Length == 3:
            point_to_remove = random.choice([point_a, point_b])
            points_lst.remove(point_to_remove)
        else:
            try:
                points_lst.remove(point_a)
                points_lst.remove(point_b)
            except:
                print("ERROR:points_lst", points_lst)
                print("ERROR:point_a", point_a[0], point_a[1])
                print("ERROR:point_b", point_b[0], point_b[1])
        points_lst.append(point_avg)
        print("points_lst_Length:", points_lst_Length, point_avg)
        points_lst_Length = len(points_lst)
    #        if len(points_lst) in lens_for_analysis:
    #          point_for_analysis.append(points_lst)

    #    for i in range(len(lens_for_analysis)):
    #      curr_label="len"+str(lens_for_analysis[i])
    #      for point in point_for_analysis[i]:
    #        plt.scatter(point[0],point[1],label=curr_label)

    plt.scatter(points_lst[0][0], points_lst[0][1], label="lastPointA", c="black")
    plt.scatter(points_lst[1][0], points_lst[1][1], label="lastPointB", c="black")
    print("end-points_lst", points_lst)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # np.random.seed(1)
    # random.seed(1)
    plt.figure(figsize=(10, 10))
    assign3_exercise3()