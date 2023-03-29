import sys


class MaxHeap:
    def __init__(self):
        self.size = 0
        self.Heap = [sys.maxsize]
        self.sortedHeap = []

    def __init__(self, arr):
        self.size = len(arr)
        self.Heap = [sys.maxsize]
        self.Heap.extend(arr)
        self.buildMaxHeap()

    def setHeap(self, arr):
        self.Heap = [sys.maxsize]
        for i in range(len(arr)):
            self.Heap.append(arr[i])
        self.size = len(arr)
        self.buildMaxHeap()

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return pos * 2

    def rightChild(self, pos):
        return (pos * 2) + 1

    def isLeaf(self, pos):
        return self.size // 2 <= pos <= self.size

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos], self.Heap[fpos])

    def maxHeapify(self, pos):
        n = self.size
        r = self.rightChild(pos)
        l = self.leftChild(pos)
        largest = pos
        if l <= n and self.Heap[largest] < self.Heap[l]:
            largest = l
        if r <= n and self.Heap[largest] < self.Heap[r]:
            largest = r
        if largest != pos:
            self.swap(largest, pos)
            self.maxHeapify(largest)

    # if not self.isLeaf(pos):
    #     if self.Heap[pos] < self.Heap[self.leftChild(pos)] or self.Heap[pos] < self.Heap[self.rightChild(pos)]:
    #         if self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]:
    #             self.swap(self.leftChild(pos), pos)
    #             self.maxHeapify(self.leftChild(pos))
    #         else:
    #             self.swap(self.rightChild(pos), pos)
    #             self.maxHeapify(self.rightChild(pos))

    def insert(self, element):
        self.Heap.append(element)
        self.size += 1
        current = self.size
        while self.Heap[current] > self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def buildMaxHeap(self):
        if self.size <= 1:
            return
        else:
            for i in range(self.size // 2, 0, -1):
                self.maxHeapify(i)

    def heapSort(self):
        originalHeap = []
        originalHeap.extend(self.Heap)
        for i in range(self.size, 0, -1):
            self.swap(1, i)
            self.size -= 1
            self.maxHeapify(1)
        self.sortedHeap = self.Heap
        self.setHeap(originalHeap)

    def isMaxHeap(self):
        for i in range(1, self.size // 2):
            if not (self.Heap[i] >= self.Heap[self.rightChild(i)] and self.Heap[i] >= self.Heap[self.leftChild(i)]):
                return False
        return True
