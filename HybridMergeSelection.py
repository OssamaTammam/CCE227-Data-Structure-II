import SelectionSort, MergeSort


def hybridMergeSelection(arr, first, last, threshold):
    if length <= threshold:
        SelectionSort.selectionSort(arr, len(arr))
    elif first < last:
        mid = first + (last - first) // 2
        hybridMergeSelection(arr, first, mid, threshold)
        hybridMergeSelection(arr, mid + 1, last, threshold)
        merge(arr, first, mid, last)
