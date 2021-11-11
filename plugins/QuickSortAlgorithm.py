from algorithms.algorithm_provider import AlgorithmProvider

class QuickSortAlgorithm:
    counter = 0

    def __init__(self, data, canvas_ui):
        self.data = data.copy()
        self.canvas_ui = canvas_ui
        self.low = 0
        self.high = len(self.data)-1

    def partition(self, low, high):
        i = (low - 1)
        pivot = self.data[high]
        for j in range(low, high):
            if self.data[j] <= pivot:
                i = i + 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
                self.canvas_ui.draw(i, j, self.data)
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        self.canvas_ui.draw(i+1, high, self.data)
        return i+1

    def quick_sort(self, low, high):
        if len(self.data) == 1:
            return self.data
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)

    def sort(self):
        self.quick_sort(self.low, self.high)

def initialize():
    AlgorithmProvider.register("QuickSort", QuickSortAlgorithm)

