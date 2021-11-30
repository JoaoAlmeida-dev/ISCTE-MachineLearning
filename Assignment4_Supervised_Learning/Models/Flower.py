import enum

class FlowerEnum(enum.Enum):
    Iris_virginica="Iris-virginica"
    Iris_versicolor = "Iris-versicolor"
    Iris_setosa = "Iris-setosa"
    NotExisting = ""

class Flower:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    flower_class: FlowerEnum

    def __init__(self, sepal_length: float, sepal_width: float, petal_length: float, petal_width: float,
                 flower_class: str = None, ) -> None:
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        if flower_class is not None:
            for fl in FlowerEnum:
                if fl.value == flower_class:
                    self.flower_class = fl
        else:
            self.flower_class = FlowerEnum.NotExisting

    def __str__(self):
        return str(self.sepal_length) + "," + str(self.sepal_width) + "," + str(self.petal_length) + "," + str(
            self.petal_width) + "," + str(self.flower_class)

    def __repr__(self): return self.__str__()

    def __sub__(self, other) -> float:
        return self.petal_width - other.petal_width + \
               self.petal_length - other.petal_length + \
               self.sepal_width - other.sepal_width + \
               self.sepal_length - other.sepal_length

    def __add__(self, other) -> float:
        return self.petal_width + other.petal_width + \
               self.petal_length + other.petal_length + \
               self.sepal_width + other.sepal_width + \
               self.sepal_length + other.sepal_length


def euclidian_distance( flower1: Flower, flower2: Flower) -> float:
    return ((flower2.petal_length - flower1.petal_length) ** 2 +
            (flower2.petal_width - flower1.petal_width) ** 2 +
            (flower2.sepal_length - flower1.sepal_length) ** 2 +
            (flower2.sepal_width - flower1.sepal_width) ** 2
            ) ** 0.5
