def maxHeapify(arr, n, pos):
    l = 2 * pos + 1  # left child
    r = 2 * pos + 2  # right child

    largest = pos  # base case current position is largest

    # check if left child or right child is larger than current position
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    # if largest is not current position, swap and maxHeapify
    if largest != pos:
        arr[largest], arr[pos] = arr[pos], arr[largest]
        maxHeapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # build max heap
    for i in range(n // 2 - 1, -1, -1):
        maxHeapify(arr, n, i)

    # swap root with last element and maxHeapify
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        maxHeapify(arr, i, 0)
