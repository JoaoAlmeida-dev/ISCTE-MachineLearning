import random

from Assignment3_Unsupervised_Learning.Logic.Helpers import distance_between
from Assignment3_Unsupervised_Learning.Logic.Assign3_Point import Point


class Cluster:
    _points_list: [Point]

    def __init__(self):
        self._points_list = []

    def addPoint(self, point: Point):
        self._points_list.append(point)

    def addPointList(self, points: [Point]):
        for point in points:
            self.addPoint(point)

    def getPoints(self) -> [Point]:
        return self._points_list.copy()

    @classmethod
    def get_point_inside_epsilon(cls, initial_point: Point, points_lst: [Point], epsilon: float):
        original_points: [Point] = points_lst.copy()
        points_in_epsilon: [Point] = []

        for point in points_lst:
            if distance_between(point, initial_point) < epsilon:
                points_in_epsilon.append(point)

        for found_point in points_in_epsilon:
            try:
                original_points.remove(found_point)
            except:
                print("ERROR removing")
                continue

        return points_in_epsilon

    @classmethod
    def create_cluster(cls, points_lst: [Point], epsilon: float):
        cluster: Cluster = Cluster()
        initial_point: Point = random.choice(points_lst)
