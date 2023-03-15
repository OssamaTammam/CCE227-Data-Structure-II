import sys


class MaxHeap:
    def __init__(self):
        self.size = 0
        self.Heap = [sys.maxsize]
        self.sortedHeap = []

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
        if not self.isLeaf(pos):
            if self.Heap[pos] < self.Heap[self.leftChild(pos)] or self.Heap[pos] < self.Heap[self.rightChild(pos)]:
                if self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]:
                    self.swap(self.leftChild(pos), pos)
                    self.maxHeapify(self.leftChild(pos))
                else:
                    self.swap(self.rightChild(pos), pos)
                    self.maxHeapify(self.rightChild(pos))

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
        originalArray = []
        originalArray.extend(self.Heap)
        for i in range(self.size, 0, -1):
            self.swap(1, i)
            self.size -= 1
            self.maxHeapify(1)
        self.sortedHeap = self.Heap
        self.Heap = originalArray


arr = [5, 6, 2, 7, 10, 11, 13, 5]
heap = MaxHeap()
heap.setHeap(arr)
heap.heapSort()
print(heap.Heap)
