from algorithms.algorithm import *
import json
import loader
from typing import Dict

class AlgorithmProvider:

    algorithms: Dict[str, Algorithm] = {
        "Bubble Sort": BubbleSortAlgorithm,
        "Insertion Sort": InsertionSortAlgorithm
    }

    def __init__(self, algorithm) -> None:
        self.algorithm = algorithm

    def get_algorithm(self) -> Algorithm:
        return self.algorithms[self.algorithm]

    @staticmethod
    def get_algotihms_list():
        return list(AlgorithmProvider.algorithms.keys())

    @staticmethod
    def register(algorithm_name: str, algorithm: Algorithm):
        AlgorithmProvider.algorithms[algorithm_name] = algorithm

    @staticmethod
    def load_plugins():
        with open("plugins.json") as file:
            data = json.load(file)
            loader.load_plugins(data["algorithms"])

