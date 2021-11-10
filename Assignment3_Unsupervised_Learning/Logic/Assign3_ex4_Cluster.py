import random

import numpy as np


class Cluster:
    _points_list: [[float, float]]

    def __init__(self):
        self._points_list = []

    def addPoint(self, point: [float, float]):
        self._points_list.append(point)

    def addPointList(self, points: [[float, float]]):
        for point in points:
            self.addPoint(point)

    def getPoints(self) -> [[float, float]]:
        return self._points_list.copy()

    @classmethod
    def distance_between(cls, point_a: [float, float], point_b: [float, float]) -> float:
        return np.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2)

    @classmethod
    def get_point_inside_epsilon(cls, initial_point: [float, float], points_lst: [[float, float]], epsilon: float):
        original_points: [[float, float]] = points_lst.copy()
        points_in_epsilon: [[float, float]] = []


        for point in points_lst:
            if Cluster.distance_between(point, initial_point) < epsilon:
                points_in_epsilon.append(point)

        for found_point in points_in_epsilon:
            try:
                original_points.remove(found_point)
            except:
                continue


        return points_in_epsilon

    @classmethod
    def create_cluster(cls, points_lst: [[float, float]], epsilon: float):
        cluster: Cluster = Cluster()
        initial_point: [float, float] = random.choice(points_lst)





