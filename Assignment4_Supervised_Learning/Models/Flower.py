class Flower:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    flower_class: str

    def __init__(self, sepal_length: float, sepal_width: float, petal_length: float, petal_width: float, flower_class: str, ) -> None:
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.flower_class = flower_class

    def __str__(self):
        return str(self.sepal_length)+"," + str(self.sepal_width)+"," + str(self.petal_length)+"," + str(self.petal_width)+"," + str(self.flower_class)