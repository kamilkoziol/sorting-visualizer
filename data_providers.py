from typing import List
import random
from math import sin, radians
import numpy as np


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DataProvider:

    data: List[int] = []

    def get_data(self):
        if not self.data:
            self.data = self.generate_data()
        return self.data

    def generate_data(self):
        pass

    @staticmethod
    def get_data_provider(data_type):
        if data_type == "Random":
            return RandomDataProvider()
        elif data_type == "Sinus":
            return SinusDataProvider()
        elif data_type == "Sorted":
            return SortedDataProvider()
        elif data_type == "Reverse sorted":
            return ReverseSortedDataProvider()


class RandomDataProvider(DataProvider, metaclass=Singleton):
    def generate_data(self):
        return random.sample(range(1, 201), 100)

    def regenerate_data(self):
        self.data = random.sample(range(1, 201), 100)
        return self.data


class SinusDataProvider(DataProvider, metaclass=Singleton):
    def generate_data(self):
        return [int((sin(x) + 1)*100) for x in np.linspace(0.01, 6.28, 100)]


class SortedDataProvider(DataProvider, metaclass=Singleton):
    def generate_data(self):
        return [x*2 for x in range(1, 101)]


class ReverseSortedDataProvider(DataProvider, metaclass=Singleton):
    def generate_data(self):
        return [200-x*2 for x in range(100)]
