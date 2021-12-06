import numpy
import random
from pathlib import Path
from typing import List, Tuple

from matplotlib import pyplot as plt

from Assignment4_Supervised_Learning.Logic.Helpers import random_split_dataset
from Assignment4_Supervised_Learning.Logic.Loader import loadData
from Assignment4_Supervised_Learning.Models.Flower import Flower, euclidian_distance, FlowerEnum


def calculate_euclidian_dataset(example_flower: Flower, dataset: List[Flower]) -> List[Tuple[Flower, float]]:
    result_list: List[Tuple[Flower, float]] = []
    for flower_dataset in dataset:
        distance = euclidian_distance(flower1=flower_dataset, flower2=example_flower)
        result_list.append((flower_dataset, distance))
    return result_list


def sort_dataset(distance_dataset: List[Tuple[Flower, float]]) -> None:
    def sorting_func(e: Tuple[Flower, float]):
        return e[1]

    distance_dataset.sort(reverse=False, key=sorting_func)


def get_k_neighbours(neighbours: List[Tuple[Flower, float]], k: int) -> List[Tuple[Flower, float]]:
    return neighbours[0:k:]


def get_most_common_class_in_neighbours(neighbours: List[Tuple[Flower, float]]) -> FlowerEnum:
    flower_class_dict = {}
    for tuple_flower_distance in neighbours:
        if tuple_flower_distance[0].flower_class in flower_class_dict.keys():
            flower_class_dict[tuple_flower_distance[0].flower_class] += 1
        else:
            flower_class_dict.update({tuple_flower_distance[0].flower_class: 1})
    max_index = list(flower_class_dict.values()).index(max(flower_class_dict.values()))
    keys = list(flower_class_dict.keys())
    return keys[max_index]


def evaluate_speculation(flower: Flower, fl_class: FlowerEnum) -> bool:
    return fl_class == flower.flower_class


def speculate_class(new_flower: Flower, dataset: List[Flower], k_neighbours_int: int):
    distances: List[Tuple[Flower, float]] = calculate_euclidian_dataset(example_flower=new_flower, dataset=dataset)
    sort_dataset(distance_dataset=distances)
    closest_neighbours: List[Tuple[Flower, float]] = get_k_neighbours(neighbours=distances, k=k_neighbours_int)
    speculation: FlowerEnum = get_most_common_class_in_neighbours(neighbours=closest_neighbours)
    return evaluate_speculation(new_flower, speculation)


def guess_on_dataset(test_set: List[Flower], training_set: List[Flower], k: int) -> Tuple[int, int]:
    corect_guesses: int = 0
    wrong_guesses: int = 0
    for flower in test_set:
        speculated_result: bool = speculate_class(new_flower=flower, dataset=training_set, k_neighbours_int=k)
        if speculated_result:
            corect_guesses += 1
        else:
            wrong_guesses += 1
    print("correct=", corect_guesses, "wrong=", wrong_guesses)
    return corect_guesses, wrong_guesses


def experiment(n_experiments: int, k_list: List[int], initial_dataset: List[Flower]) -> List[List[Tuple[int, int]]]:
    results_list: List[List[float]] = [[] for _ in k_list]
    for _k_index, _k in enumerate(k_list):
        for _ in range(n_experiments):
            _training_set, _test_set = random_split_dataset(initial_dataset)
            correct, wrong = guess_on_dataset(training_set=_training_set, test_set=_test_set, k=_k)
            results_list[_k_index].append(correct / (correct + wrong))
    #plt.subplot(1, 2, 1)
    plt.boxplot(results_list, positions=k_list,widths=3)
    #plt.subplot(1, 2, 2)
    #for results_index, results in enumerate(results_list):
    #    plt.plot(results, label="k=" + str(k_list[results_index]))
    plt.xlabel("K values")
    plt.ylabel("% correct")
    plt.title("Exercise2 with "+str(n_experiments) + " experiments")
    plt.tight_layout()
    plt.legend()
    plt.show()
    return results_list


if __name__ == '__main__':
    random.seed(1)
    numpy.random.seed(1)

    root_path = Path(__file__).parent.parent
    print(root_path)
    flowers: List[Flower] = loadData(str(root_path) + "/Resources/iris.data")
    training_set, test_set = random_split_dataset(flowers)
    print("training_set", len(training_set))
    print("test_set", len(test_set))
    new_flower: Flower = Flower(sepal_length=0.1, sepal_width=0.3, petal_length=0.4, petal_width=0.5)
    k = 2
    guess_on_dataset(test_set=test_set, training_set=training_set, k=k)
    experiment(n_experiments=10, k_list=[2,10,20,30,40,50,60,70,80,90,100], initial_dataset=flowers)
