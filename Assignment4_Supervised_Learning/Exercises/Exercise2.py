from pathlib import Path
from random import random
from typing import List, Tuple

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


def random_split_dataset(dataset: List[Flower]) -> Tuple[List[Flower], List[Flower]]:
    dataset1: List[Flower] = []
    dataset2: List[Flower] = []

    counter: int = 0
    max_len_dataset1 = int(len(dataset) * 0.7)
    max_len_dataset2 = int(len(dataset) * 0.3)
    while len(dataset) > 0:
        random_index: int = int(random() * len(dataset))
        if counter <= max_len_dataset1:
            dataset1.append(dataset.pop(random_index))
        else:
            dataset2.append(dataset.pop(random_index))
        counter += 1
    return dataset1, dataset2


if __name__ == '__main__':
    root_path = Path(__file__).parent.parent
    print(root_path)
    flowers: List[Flower] = loadData(str(root_path) + "/Resources/iris.data")
    training_set, test_set = random_split_dataset(flowers)
    print("training_set", len(training_set))
    print("test_set", len(test_set))
