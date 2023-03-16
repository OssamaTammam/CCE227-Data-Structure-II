def maxHeapify(arr, n, pos):
    l = 2 * pos + 1
    r = 2 * pos + 2
    largest = pos
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != pos:
        arr[largest], arr[pos] = arr[pos], arr[largest]
        maxHeapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    # build max heap
    for i in range(n // 2 - 1, -1, -1):
        maxHeapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        maxHeapify(arr, i, 0)
