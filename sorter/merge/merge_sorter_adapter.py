import time

from sorter.sorter_port import SorterPort


class MergeSorterAdapter(SorterPort):
    def __init__(self):
        self._duration = 0

    def sort(self, arr: list) -> list:
        """
        Sorts an array using Merge Sort algorithm.
        Guarantees O(n log n) algorithmic complexity.
        :param arr: Input array.
        :return: Sorted array.
        """
        result = arr.copy()
        start = time.time()
        self.__mergeSort(result, 0, len(result) - 1)
        end = time.time()
        self._duration = end - start
        return result

    def getDuration(self) -> float:
        return self._duration

    @staticmethod
    def __merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = arr[l + i]
        for j in range(n2):
            R[j] = arr[m + 1 + j]

        i = j = 0
        k = l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def __mergeSort(self, arr, l, r):
        if l < r:
            m = l + (r - l) // 2
            self.__mergeSort(arr, l, m)
            self.__mergeSort(arr, m + 1, r)
            self.__merge(arr, l, m, r)
