import random, time
import pandas as pd
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
    originalArray = generateRandomArray(100)
    tempArray = []
    print(f"Original array is {originalArray}")
    print("---------------------------------------------------------------------------")

    # quick sort algorithm
    copyArray(originalArray, tempArray)
    start = time.time()
    QuickSort.quickSort(tempArray, 0, len(tempArray) - 1)
    end = time.time()
    runningTime = (end - start) * 1000
    print(
        f"Running time for Quick Sort is {runningTime} ms \nArray after sorting is {tempArray}\nIs sorted = {isSorted(tempArray)}")
    print("---------------------------------------------------------------------------")
    copyArray(originalArray, tempArray)

    # merge sort algorithm
    copyArray(originalArray, tempArray)
    start = time.time()
    MergeSort.mergeSort(tempArray)
    end = time.time()
    runningTime = (end - start) * 1000
    print(
        f"Running time for Merge Sort is {runningTime} ms \nArray after sorting is {tempArray}\nIs sorted = {isSorted(tempArray)}")
    print("---------------------------------------------------------------------------")
    copyArray(originalArray, tempArray)

    # heap sort algorithm
    copyArray(originalArray, tempArray)
    start = time.time()
    MaxHeap.heapSort(tempArray)
    end = time.time()
    runningTime = (end - start) * 1000
    print(
        f"Running time for Heap Sort is {runningTime} ms \nArray after sorting is {tempArray}\nIs sorted = {isSorted(tempArray)}")
    print("---------------------------------------------------------------------------")
    copyArray(originalArray, tempArray)

    # selection sort algorithm
    copyArray(originalArray, tempArray)
    start = time.time()
    SelectionSort.selectionSort(tempArray)
    end = time.time()
    runningTime = (end - start) * 1000
    print(
        f"Running time for Selection Sort is {runningTime} ms \nArray after sorting is {tempArray}\nIs sorted = {isSorted(tempArray)}")
    print("---------------------------------------------------------------------------")
    copyArray(originalArray, tempArray)

    # insertion sort algorithm
    copyArray(originalArray, tempArray)
    start = time.time()
    InsertionSort.insertionSort(tempArray)
    end = time.time()
    runningTime = (end - start) * 1000
    print(
        f"Running time for Insertion Sort is {runningTime} ms \nArray after sorting is {tempArray}\nIs sorted = {isSorted(tempArray)}")
    print("---------------------------------------------------------------------------")
    copyArray(originalArray, tempArray)

    quickSortTime = []
    mergeSortTime = []
    heapSortTime = []
    selectionSortTime = []
    insertionSortTime = []
    arraySizes = []
    arraySize = 1000

    while arraySize <= 100000:
        # quick sort running time
        copyArray(originalArray, tempArray)
        start = time.time()
        QuickSort.quickSort(tempArray, 0, len(tempArray) - 1)
        end = time.time()
        runningTime = (end - start) * 1000
        quickSortTime.append(runningTime)

        # merge sort running time
        copyArray(originalArray, tempArray)
        start = time.time()
        MergeSort.mergeSort(tempArray)
        end = time.time()
        runningTime = (end - start) * 1000
        mergeSortTime.append(runningTime)

        # heap sort running time
        copyArray(originalArray, tempArray)
        start = time.time()
        MaxHeap.heapSort(tempArray)
        end = time.time()
        runningTime = (end - start) * 1000
        heapSortTime.append(runningTime)

        # selection sort running time
        copyArray(originalArray, tempArray)
        start = time.time()
        SelectionSort.selectionSort(tempArray)
        end = time.time()
        runningTime = (end - start) * 1000
        selectionSortTime.append(runningTime)

        # insertion sort running time
        copyArray(originalArray, tempArray)
        start = time.time()
        InsertionSort.insertionSort(tempArray)
        end = time.time()
        runningTime = (end - start) * 1000
        insertionSortTime.append(runningTime)

        arraySizes.append(arraySize)
        arraySize += 1000

    # excelArray = [arraySizes, quickSortTime, mergeSortTime, heapSortTime, selectionSortTime, insertionSortTime]
    # time.sleep(3)
    # df = pd.DataFrame(excelArray).T
    # time.sleep(3)
    # df.to_excel(excel_writer="running_times.xlsx")

    print("Done")
