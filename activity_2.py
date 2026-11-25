import heapq
import random

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, -value)

    def peek(self):
        return -self.heap[0] if self.heap else None

    def extract(self):
        return -heapq.heappop(self.heap) if self.heap else None

    def size(self):
        return len(self.heap)


print("\n=== Activity 2: Max Heap ===")
values = [19, 18, 17, 14, 13, 11, 9, 5]

max_heap = MaxHeap()

for v in values:
    max_heap.insert(v)

result = []
while max_heap.size() > 0:
    result.append(max_heap.extract())

print("Extract order:", result)
# Expected: [19, 18, 17, 14, 13, 11, 9, 5]