from Assignment3_Unsupervised_Learning.Logic.Point import Point


@classmethod
def distance_between(point_a: Point, point_b: Point) -> float:
    # return np.sqrt((point_a.x - point_b.x) ** 2 + (point_a.y - point_b.y) ** 2)
    return (point_a.x - point_b.x) ** 2 + (point_a.y - point_b.y) ** 2