import SelectionSort
import MergeSort


def hybridMergeSelection(arr, threshold):
    length = len(arr)
    # use selection sort if the array is small enough
    if length <= threshold:
        SelectionSort.selectionSort(arr)
    # use merge sort until array is small enough to use selection sort
    else:
        middle = length // 2
        left = arr[:middle]
        right = arr[middle:]
        hybridMergeSelection(left, threshold)
        hybridMergeSelection(right, threshold)
        MergeSort.merge(arr, left, right)
