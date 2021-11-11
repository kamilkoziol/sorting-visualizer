from abc import ABC, abstractmethod
from typing import List


class Algorithm(ABC):

    @abstractmethod
    def sort(self):
        pass


class BubbleSortAlgorithm(Algorithm):
    counter = 0

    def __init__(self, data, canvas_ui):
        self.data = data.copy()
        self.canvas_ui = canvas_ui

    def sort(self):
        n = len(self.data)
        for i in range(0, n-1):
            for j in range(0, n-i-1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.canvas_ui.draw(j, j+1, self.data)
                    self.counter += 1
        print(f'bubble {self.counter}')


class InsertionSortAlgorithm(Algorithm):
    counter = 0
    def __init__(self, data, canvas_ui):
        self.data = data.copy()
        self.canvas_ui = canvas_ui

    def sort(self):
        n = len(self.data)
        for i in range(1, n):
            key = self.data[i]
            j = i - 1
            while j >= 0 and key < self.data[j]:
                self.data[j + 1] = self.data[j]
                j -= 1
                self.counter += 1
                self.canvas_ui.draw(i, j, self.data)
            self.data[j + 1] = key