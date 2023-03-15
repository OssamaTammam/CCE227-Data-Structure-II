import random
import time
import QuickSort, MaxHeap, MergeSort, InsertionSort, SelectionSort


def generateRandomArray(size):
    randomArray = []
    for i in range(size):
        temp = random.randint(0, 1000)
        randomArray.append(temp)
    return randomArray


def isSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            return False
    return True


def copyArray(original, clone):
    clone.clear()
    clone.extend(original)


if __name__ == '__main__':
    originalArray = generateRandomArray(10000)
    tempArray = []
    print(f"Original array is {originalArray}")
    print("--------------------------------------------------------------------------")

    # # quick sort algorithm
    # copyArray(originalArray, tempArray)
    # start = time.time()
    # QuickSort.quickSort(tempArray)
    # end = time.time()
    # print(
    #     f"Running time for Quick Sort is {end - start} ms \nArray after sorting is {tempArray}\nIs sorted = {isSorted(tempArray)}")
    # print("---------------------------------------------------------------------------")
    # copyArray(originalArray, tempArray)

    # merge sort algorithm
    copyArray(originalArray, tempArray)
    start = time.time()
    MergeSort.mergeSort(tempArray)
    end = time.time()
    print(
        f"Running time for Merge Sort is {end - start} ms \nArray after sorting is {tempArray}\nIs sorted = {isSorted(tempArray)}")
    print("---------------------------------------------------------------------------")
    copyArray(originalArray, tempArray)

    # heap sort algorithm
    copyArray(originalArray, tempArray)
    start = time.time()
    MaxHeap.heapSort(tempArray)
    end = time.time()
    print(
        f"Running time for Heap Sort is {end - start} ms \nArray after sorting is {tempArray}\nIs sorted = {isSorted(tempArray)}")
    print("---------------------------------------------------------------------------")
    copyArray(originalArray, tempArray)

    # selection sort algorithm
    copyArray(originalArray, tempArray)
    start = time.time()
    SelectionSort.selectionSort(tempArray)
    end = time.time()
    print(
        f"Running time for Selection Sort is {end - start} ms \nArray after sorting is {tempArray}\nIs sorted = {isSorted(tempArray)}")
    print("---------------------------------------------------------------------------")
    copyArray(originalArray, tempArray)

    # insertion sort algorithm
    copyArray(originalArray, tempArray)
    start = time.time()
    InsertionSort.insertionSort(tempArray)
    end = time.time()
    print(
        f"Running time for Insertion Sort is {end - start} ms \nArray after sorting is {tempArray}\nIs sorted = {isSorted(tempArray)}")
    print("---------------------------------------------------------------------------")
    copyArray(originalArray, tempArray)

    QuickSort = []
    MergeSort = []
    HeapSort = []
    SelectionSort = []
    InsertionSort = []
