import random

from matplotlib import pyplot as plt

from Assignment3_Unsupervised_Learning.Logic.Assign3_DistanceMatrix import DistanceMatrix
from Assignment3_Unsupervised_Learning.Logic.Helpers import distance_between
from Assignment3_Unsupervised_Learning.Logic.Assign3_Point import Point


class Cluster:
    _points_list: [Point]
    _initial_point: Point

    def __init__(self, epsilon: float, distance_matrix: DistanceMatrix):
        self._points_list = []
        initial_point = random.choice(distance_matrix.points_list)
        while initial_point.visited:
            initial_point: Point = random.choice(distance_matrix.points_list)
        self._initial_point = initial_point
        self._initial_point.visited = True
        self._points_list.append(self._initial_point)
        initial_point_index = distance_matrix.points_list.index(self._initial_point)


        def aux( distance_matrix, epsilon, initial_point):
            initial_point.visited = True
            self.addPoint(point=initial_point)

            first_layer = distance_matrix.get_points_inside_epsilon(center_point=initial_point, epsilon=epsilon)
            for point in first_layer:
                point.visited = True
                self.addPoint(point=point)
                # distance_matrix.remove_point(point=point)
            for point in first_layer:
                aux(distance_matrix, epsilon, point)
                # distance_matrix.remove_point(point=point2)
        aux(distance_matrix, epsilon, initial_point)

    def getInitial_Point(self) -> Point:
        return self._initial_point

    def addPoint(self, point: Point):
        if point not in self._points_list:
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


if __name__ == '__main__':
    points = [Point(random.random(), random.random()) for _ in range(10)]
    matrix0 = DistanceMatrix(len(points), points)
    print(matrix0)
    center_point = points[5]
    epsilon: float = 0.5
    points_in_epsilon = matrix0.get_points_inside_epsilon(center_point=center_point, epsilon=epsilon)

    circle = plt.Circle(xy=(center_point.x, center_point.y), radius=epsilon, alpha=0.2,
                        color="orange")
    figure, axes = plt.subplots()

    axes.set_aspect(1)
    axes.add_artist(circle)

    for point in points:
        plt.scatter(point.x, point.y, c="black", alpha=0.5)
    for point_in_epsilon in points_in_epsilon:
        plt.scatter(point_in_epsilon.x, point_in_epsilon.y, alpha=0.5, c="red")

    plt.tight_layout()
    plt.legend()
    plt.show()
