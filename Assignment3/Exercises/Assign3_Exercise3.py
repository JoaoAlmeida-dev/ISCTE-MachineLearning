import random
import numpy as np

from Assignment3.Logic.Assign3_PointGenerator import generate_Points


def average_point(point_a: np.ndarray, point_b: np.ndarray) -> list:
    avg_x = (point_a[0] + point_b[0]) / 2
    avg_y = (point_a[1] + point_b[1]) / 2
    list = [avg_x, avg_y]

    return list


def distance_between(point_a: np.ndarray, point_b: np.ndarray) -> float:
    return np.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[0] - point_b[0]) ** 2)


def find_closest_two_points(points_lst: list):
    point_a: np.ndarray = random.choice(points_lst)
    point_b: np.ndarray = random.choice(points_lst)
    shortest_distance: float = distance_between(point_a, point_b)

    for point1 in points_lst:
        for point2 in points_lst:
            distance = distance_between(point1, point2)
            if distance < shortest_distance:
                if point1 != point2:
                    shortest_distance = distance
                    point_a = point1
                    point_b = point2
    return point_a, point_b


def assign3_exercise3(a: np.ndarray, b: np.ndarray, c: np.ndarray):
    points_lst:list = c.T.copy().tolist()
    iterations = 100
    for i in range(iterations):
        points_lst_Length = len(points_lst)
        while  points_lst_Length> 2:
            points_lst_Length = len(points_lst)

            point_a, point_b = find_closest_two_points(points_lst)
            point_avg = average_point(point_a, point_b)
            points_lst.remove(point_a)
            points_lst.remove(point_b)
            points_lst.append(point_avg)
            print("points_lst_Length:",points_lst_Length,point_avg)


if __name__ == '__main__':
    np.random.seed(1)
    random.seed(1)
    points1, points2, pointsconcat = generate_Points()
    assign3_exercise3(points1, points2, pointsconcat)
