def selectionSort(arr):
    for i in range(len(arr) - 1):
        min = i;
        for j in range(len(arr)):
            if arr[min] > arr[j]:
                min = j
            arr[min], arr[j] = arr[j], arr[min]