import random
import time
import InsertionSort


def generateRandomArray(size):
    randomArray = []
    for i in range(size):
        temp = random.randint(0, 1000)
        randomArray.append(temp)
    return randomArray


if __name__ == '__main__':
    originalArray = generateRandomArray(1000)
    print(f"Original array is {originalArray}")
    tempArray = originalArray
    start = time.time()
    InsertionSort.insertionSort(tempArray)
    end = time.time()
    print(f"Running time for Insertion Sort is {end - start} ms \nArray after sorting is {tempArray}")
    tempArray = originalArray
