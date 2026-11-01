import os
from io import TextIOWrapper
from pathlib import Path

from sorter.sorter_factory import SorterFactory
from sorter.sorter_port import SorterPort

INPUT_FOLDER = Path("input")
OUTPUT_FOLDER = Path("output")


def toStr(arr: list[int]) -> str:
    output = ""
    for n in arr:
        output += f"{n} "
    output.removesuffix(" ")
    return output


def toArr(inp: str) -> list[int]:
    result = []
    arr = inp.split(' ')
    for n in arr:
        if n.isnumeric():
            result.append(int(n))
    return result


def main():
    print("Running sorter (abstract class example)")

    sorter: SorterPort = SorterFactory("sorter.config").get()

    if not OUTPUT_FOLDER.exists():
        os.mkdir(OUTPUT_FOLDER)
        print("Created output directory")

    print("Detecting sets to sort")
    sets: list[TextIOWrapper] = []
    setsNames: list[str] = []
    for path in INPUT_FOLDER.glob("*.in"):
        descriptor = open(path, 'r', encoding='utf-8-sig')
        print("Detected set:", path)
        sets.append(descriptor)
        setsNames.append(path.name.removesuffix(".in"))
    print(f"Detected {len(sets)} sets")

    for i in range(0, len(sets)):
        print(f"Reading set {i + 1}/{len(sets)}")
        N: list[int] = toArr(sets[i].read())
        print(f"Read set {i + 1}/{len(sets)}: len={len(N)}")
        print(f"Sorting set {i + 1}/{len(sets)}")
        sortedN: list[int] = sorter.sort(N)
        print(f"Sorted set {i + 1}/{len(sets)} in {sorter.getDuration():.2f}s")
        print(f"Saving sorted set {i + 1}/{len(sets)}")
        outputPath = OUTPUT_FOLDER / (setsNames[i] + ".out")
        with open(outputPath, 'w') as f:
            f.write(toStr(sortedN))
        print(f"Saved sorted set {i + 1}/{len(sets)}: {str(outputPath)}")


main()
