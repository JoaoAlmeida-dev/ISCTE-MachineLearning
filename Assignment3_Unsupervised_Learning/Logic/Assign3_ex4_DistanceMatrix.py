import random

import matplotlib.pyplot as plt

from Assignment3_Unsupervised_Learning.Logic.Assign3_Point import Point
from Assignment3_Unsupervised_Learning.Logic.Helpers import distance_between


class DistanceMatrix:
    matrix: [[]]
    points_list: [Point]
    size: int

    def hasPointsNotVisited(self) -> bool:
        points_visited_list = [not point.visited for point in self.points_list]
        points_not_visited_bool = any(points_visited_list)
        return points_not_visited_bool

    def __init__(self, size: int, points_list: [Point] = None):
        self.size = size
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]
        if points_list is not None:
            self.points_list = points_list
            for point_index in range(len(points_list)):
                for point_index_2 in range(len(points_list)):
                    if self.matrix[point_index_2][point_index] == 0:
                        distance = distance_between(points_list[point_index], points_list[point_index_2])
                        self.matrix[point_index][point_index_2] = distance
        else:
            self.points_list = []

    def remove_point(self, point: Point):
        point_index = self.points_list.index(point)
        self.points_list.remove(point)

        matrix_copy = [[] for _ in range(self.size)]
        for row in range(len(self.matrix)):
            if row != point_index:
                index_ = self.matrix[row][0:point_index:] + self.matrix[row][point_index + 1:len(self.matrix[row]):]
                for input in index_:
                    matrix_copy[row].append(input)
        matrix_copy = matrix_copy[0:point_index:] + matrix_copy[point_index + 1:len(self.matrix):]

        self.matrix = matrix_copy

    def add_point(self, point: Point):

        # _distances: [float] = [distance_between(point_in_self, point_index) for point_in_self in self.points_list]
        _distances: [float] = []
        _last_row: [float] = []
        for point_in_self in self.points_list:
            _distances.append(distance_between(point_in_self, point))
            _last_row.append(0)
        _last_row.append(distance_between(point, point))

        self.points_list.append(point)
        _counter: int = 0
        for row_index in range(len(self.matrix)):
            self.matrix[row_index].append(_distances[_counter])
            _counter += 1
        self.matrix.append(_last_row)

    def get_points_inside_epsilon(self, center_point: Point, epsilon: float) -> [Point]:
        _distances_found: [float] = []
        _points_found: [int] = []
        _point_index = self.points_list.index(center_point)

        for row_index in range(len(self.matrix)):
            # for collumn_index in range(len(self.matrix[_point_index])):
            _value: float = self.matrix[row_index][_point_index]
            _point_value = self.points_list[row_index]
            if epsilon >= _value > 0 and not _point_value.visited:
                _distances_found.append(_value)
                # _points_found.append((row_index, _point_index))
                #_points_found.append(row_index)
                _point_value.visited=True
                _points_found.append(_point_value)
        return _points_found

    def __str__(self):
        # result = [ str(row)+"\n" for row in self.matrix]
        result = ""
        for row in range(len(self.matrix)):
            result += "["
            for collumn in range(len(self.matrix[row])):
                result += str(round(self.matrix[row][collumn], 2)) + ",\t"
            result += "]\n"
        # return "".join(result)
        return result

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    points = [Point(random.random(), random.random()) for _ in range(10)]
    matrix0 = DistanceMatrix(len(points), points)
    print(matrix0)
    points_in_epsilon = matrix0.get_points_inside_epsilon(center_point=points[5], epsilon=0.5)

    for point in points:
        plt.scatter(point.x, point.y, c="black", alpha=0.5)
    for point_index in points_in_epsilon:
        plt.scatter(matrix0.points_list[point_index].x, matrix0.points_list[point_index].y, alpha=1, c="red")
    print(matrix0.hasPointsNotVisited())
    print(matrix0.points_list)
    points[0].visited=True
    print(matrix0.hasPointsNotVisited())
    print(matrix0.points_list)
    points[9].visited=True
    print(matrix0.hasPointsNotVisited())
    print(matrix0.points_list)
    for point in matrix0.points_list:
        point.visited=True
    print(matrix0.hasPointsNotVisited())
    print(matrix0.points_list)

    plt.legend()
    plt.show()
