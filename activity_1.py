import heapq
import random


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def peek(self):
        return self.heap[0] if self.heap else None

    def extract(self):
        return heapq.heappop(self.heap) if self.heap else None

    def size(self):
        return len(self.heap)


print("=== Activity 1: Min Heap ===")
values = [5, 9, 11, 14, 19, 17, 18, 13]

min_heap = MinHeap()

for v in values:
    min_heap.insert(v)

print("Heap:", min_heap.heap)

result = []
while min_heap.size() > 0:
    result.append(min_heap.extract())

print("Extract order:", result)