import SelectionSort
import MergeSort


def hybridMergeSelection(arr, threshold):
    length = len(arr)
    if length <= threshold:
        SelectionSort.selectionSort(arr)
    else:
        middle = length // 2
        left = arr[:middle]
        right = arr[middle:]
        hybridMergeSelection(left, threshold)
        hybridMergeSelection(right, threshold)
        MergeSort.merge(arr, left, right)
