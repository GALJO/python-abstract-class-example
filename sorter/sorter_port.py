from abc import ABC, abstractmethod


class SorterPort(ABC):
    @abstractmethod
    def sort(self, arr: list) -> list:
        """
        Sorts an array.
        :param arr: Input array.
        :return: Sorted array.
        """
        pass

    @abstractmethod
    def getDuration(self) -> float:
        """
        Getter.
        :return: Duration of last sort.
        """
        pass
