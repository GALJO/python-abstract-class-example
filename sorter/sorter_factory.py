from sorter.bubble.bubble_sorter_adapter import BubbleSorterAdapter
from sorter.merge.merge_sorter_adapter import MergeSorterAdapter
from sorter.sorter_port import SorterPort
from sorter.sorter_type import SorterType


class SorterFactory:
    def __init__(self, configPath):
        file = open(configPath, 'r')
        config = file.read()
        match config:
            case SorterType.BUBBLE.value:
                self._sorter = BubbleSorterAdapter()
                print("Configured BubbleSorterAdapter")
            case SorterType.MERGE.value:
                self._sorter = MergeSorterAdapter()
                print("Configured MergeSorterAdapter")

    def get(self, ) -> SorterPort:
        return self._sorter
