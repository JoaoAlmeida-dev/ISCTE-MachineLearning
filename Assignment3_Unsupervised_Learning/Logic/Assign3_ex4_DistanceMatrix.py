from Assignment3_Unsupervised_Learning.Logic.Assign3_Point import Point
from Assignment3_Unsupervised_Learning.Logic.Helpers import distance_between


class DistanceMatrix:
    matrix: [[]]
    points_list: [Point]
    size: int

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
                index_ = self.matrix[row][0:point_index:]+self.matrix[row][point_index+1:len(self.matrix[row]):]
                for input in index_:
                    matrix_copy[row].append(input)
        matrix_copy = matrix_copy[0:point_index:]+matrix_copy[point_index+1:len(self.matrix):]

        self.matrix = matrix_copy

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
    point_to_remove = Point(1, 2)
    point_to_remove2 = Point(0.1, 3.1)
    points = [point_to_remove, Point(5, 2), point_to_remove2, Point(0, 2.2), Point(0.5, 2.6)]
    matrix0 = DistanceMatrix(len(points), points)
    print(matrix0)
    matrix0.remove_point(point_to_remove2)
    print(matrix0)
