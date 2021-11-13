from Assignment3_Unsupervised_Learning.Logic.Point import Point


def distance_between(point_a: Point, point_b: Point) -> float:
    # return np.sqrt((point_a.x - point_b.x) ** 2 + (point_a.y - point_b.y) ** 2)
    return (point_a.x - point_b.x) ** 2 + (point_a.y - point_b.y) ** 2


def create_empty_matrix(rows: int, collums: int):
    return [[[] for i in range(collums)] for i in range(rows)]
