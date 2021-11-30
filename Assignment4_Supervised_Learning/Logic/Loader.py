from typing import List

from Assignment4_Supervised_Learning.Models.Flower import Flower


def loadData(path: str):
    flower_list: List[Flower] = []
    file = open(path, "r")
    for line in file:
        split_line = line.split(",")
        flower_list.append(Flower(sepal_length=float(split_line[0]),
                                  sepal_width=float(split_line[1]),
                                  petal_length=float(split_line[2]),
                                  petal_width=float(split_line[3]),
                                  flower_class=split_line[4][:-1:]
                                  )
                           )
    for flower in flower_list:
        print(flower)
    return flower_list