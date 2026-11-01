import time

from sorter.sorter_port import SorterPort


class BubbleSorterAdapter(SorterPort):
    def __init__(self):
        self._duration = 0

    def sort(self, arr: list) -> list:
        """
        Sorts an array using Bubble Sort algorithm.
        Guarantees O(n^2) algorithmic complexity.
        :param arr: Input array.
        :return: Sorted array.
        """
        output = arr.copy()
        n = len(output)
        start = time.time()
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if output[j] > output[j + 1]:
                    output[j], output[j + 1] = output[j + 1], output[j]
                    swapped = True
            if not swapped:
                break
        end = time.time()
        self._duration = end - start
        return output

    def getDuration(self) -> float:
        return self._duration
