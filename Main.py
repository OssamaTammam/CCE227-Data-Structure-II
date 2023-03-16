import random, time, xlsxwriter, pandas
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
    print(
        f"Running time for Quick Sort is {end - start} ms \nArray after sorting is {tempArray}\nIs sorted = {isSorted(tempArray)}")
    print("---------------------------------------------------------------------------")
    copyArray(originalArray, tempArray)

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
        quickSortTime.append(end - start)

        # merge sort running time
        copyArray(originalArray, tempArray)
        start = time.time()
        MergeSort.mergeSort(tempArray)
        end = time.time()
        mergeSortTime.append(end - start)

        # heap sort running time
        copyArray(originalArray, tempArray)
        start = time.time()
        MaxHeap.heapSort(tempArray)
        end = time.time()
        heapSortTime.append(end - start)

        # selection sort running time
        copyArray(originalArray, tempArray)
        start = time.time()
        SelectionSort.selectionSort(tempArray)
        end = time.time()
        selectionSortTime.append(end - start)

        # insertion sort running time
        copyArray(originalArray, tempArray)
        start = time.time()
        InsertionSort.insertionSort(tempArray)
        end = time.time()
        insertionSortTime.append(end - start)

        arraySizes.append(arraySize)
        arraySize += 1000

    print("Done")
