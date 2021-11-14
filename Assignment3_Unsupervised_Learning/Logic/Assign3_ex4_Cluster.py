import random

from Assignment3_Unsupervised_Learning.Logic.Assign3_ex4_DistanceMatrix import DistanceMatrix
from Assignment3_Unsupervised_Learning.Logic.Helpers import distance_between
from Assignment3_Unsupervised_Learning.Logic.Assign3_Point import Point


# https://www.youtube.com/watch?v=_A9Tq6mGtLI

class Cluster:
    _points_list: [Point]
    _initial_point: Point

    def getInitial_Point(self) -> Point:
        return self._initial_point

    def __init__(self, epsilon: float, distance_matrix: DistanceMatrix):
        self._points_list = []
        initial_point = random.choice(distance_matrix.points_list)
        while initial_point.visited:
            initial_point: Point = random.choice(distance_matrix.points_list)
        self._initial_point = initial_point
        self._initial_point.visited= True
        self._points_list.append(self._initial_point)
        initial_point_index = distance_matrix.points_list.index(self._initial_point)


        def aux(distance_matrix_aux, epsilon_aux, initial_point_aux):
            core_points_in_epsilon: [Point] = distance_matrix_aux.get_points_inside_epsilon(
                center_point=initial_point_aux,
                epsilon=epsilon_aux)
            for point in core_points_in_epsilon:
                self.addPoint(point)
                points_in_epsilon_temp: [Point] = distance_matrix_aux.get_points_inside_epsilon(center_point=point,
                                                                                                epsilon=epsilon_aux)
                distance_matrix_aux.remove_point(point)
                for point2 in points_in_epsilon_temp:
                    print(point2)
                    aux(distance_matrix_aux=distance_matrix_aux, epsilon_aux=epsilon_aux, initial_point_aux=point2)

        aux(distance_matrix_aux=distance_matrix, epsilon_aux=epsilon, initial_point_aux=initial_point)

    def addPoint(self, point: Point):
        point.visited = True
        self._points_list.append(point)

    def addPointList(self, points: [Point]):
        for point in points:
            self.addPoint(point)

    def getPoints(self) -> [Point]:
        return self._points_list.copy()

    def getSize(self) -> int:
        return len(self._points_list)

    def __str__(self):
        string_value: str = "Cluster["
        for i in self._points_list:
            string_value += str(i) + ","
        string_value += "]"
        return string_value

    def __repr__(self):
        return self.__str__()

    #    @classmethod
    #    def get_point_inside_epsilon(cls, initial_point: Point, points_lst: [Point], epsilon: float):
    #        original_points: [Point] = points_lst.copy()
    #        points_in_epsilon: [Point] = []
    #
    #        for point_index in points_lst:
    #            if distance_between(point_index, initial_point) < epsilon:
    #                points_in_epsilon.append(point_index)
    #
    #        for found_point in points_in_epsilon:
    #            try:
    #                original_points.remove(found_point)
    #            except:
    #                print("ERROR removing")
    #                continue
    #        return points_in_epsilon
