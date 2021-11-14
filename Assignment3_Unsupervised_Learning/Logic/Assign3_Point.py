from Assignment3_Unsupervised_Learning.Logic.Assign3_PointGenerator import generate_Points


class Point:
    x: float
    y: float
    label: str
    visited: bool

    def __init__(self, x: float, y: float, visited: bool = False, label: str = "", ):
        self.x = x
        self.y = y
        self.visited = visited
        self.label = label

    def __str__(self):
        round_digits = 5
        return self.label + "[" + str(round(self.x, round_digits)) + "," + str(round(self.y, round_digits)) + "]" + str(
            self.visited)

    def __repr__(self):
        return self.__str__()

    @classmethod
    def generate_Points(cls, alpha: float, plot: bool, pointN: int):
        _a, _b, _c = generate_Points(alpha=alpha, plot=plot, pointN=pointN)
        _points_list: [Point] = []
        for point in _a.T:
            _points_list.append(Point(x=point[0], y=point[1], label="a"))
        for point in _b.T:
            _points_list.append(Point(x=point[0], y=point[1], label="b"))
        return _points_list
