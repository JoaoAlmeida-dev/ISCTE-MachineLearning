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
                    # if self.matrix[point_index][point_index_2] == 0:
                    distance = distance_between(points_list[point_index], points_list[point_index_2])
                    self.matrix[point_index_2][point_index] = distance
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
        _points_found: [int] = []
        _center_point_index = self.points_list.index(center_point)
        # print("matrix at", _center_point_index, self.matrix[_center_point_index])
        for column_index in range(len(self.matrix[_center_point_index])):
            curr_dist: float = self.matrix[_center_point_index][column_index]
            curr_point: Point = self.points_list[column_index]
            if curr_dist <= epsilon > 0 and not curr_point.visited:
                _points_found.append(column_index)
        # print("_points_found", _points_found)
        points_list: [Point] = []
        for _point_index in _points_found:
            points_list.append(self.points_list[_point_index])
        return points_list

    def get_dist_between(self,point1:Point,point2:Point):
        if point1 in self.points_list and point2 in self.points_list:
            point1_index=self.points_list.index(point1)
            point2_index=self.points_list.index(point2)

            return self.matrix[point1_index][point2_index]

    def get_closest_pair(self) -> (Point, Point):

        random_initial_point1=random.choice([0,len(self.points_list)-1])
        random_initial_point2=random.choice([0,len(self.points_list)-1])
        while random_initial_point2 == random_initial_point1:
            random_initial_point1=random.choice([0,len(self.points_list)-1])
            random_initial_point2=random.choice([0,len(self.points_list)-1])

        minimum_value = self.matrix[random_initial_point1][random_initial_point2]
        point1_index: int = random_initial_point1
        point2_index: int = random_initial_point2
        for row_index, row in enumerate(self.matrix):
            for collumn_index, collumn in enumerate(row):
                if collumn < minimum_value and collumn>0.0:
                    minimum_value = collumn
                    point1_index = row_index
                    point2_index = collumn_index
        return self.points_list[point1_index], self.points_list[point2_index],

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
    for point_epsilon in points_in_epsilon:
        plt.scatter(point_epsilon.x, point_epsilon.y, alpha=1, c="red")
    print(matrix0.hasPointsNotVisited())
    print(matrix0.points_list)
    points[0].visited = True
    print(matrix0.hasPointsNotVisited())
    print(matrix0.points_list)
    points[9].visited = True
    print(matrix0.hasPointsNotVisited())
    print(matrix0.points_list)
    for point in matrix0.points_list:
        point.visited = True
    print(matrix0.hasPointsNotVisited())
    print(matrix0.points_list)
    closest_point1,closest_point2 =matrix0.get_closest_pair()
    print("closestPair=",closest_point1,closest_point2 , "dist=",matrix0.get_dist_between(closest_point1,closest_point2))
    plt.legend()
    plt.show()
