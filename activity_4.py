import heapq
import random

def kth_largest(nums, k):
    min_heap = []

    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heapreplace(min_heap, num)

    return min_heap[0]


print("=== Activity 4: Kth Largest ===")

nums = [7, 4, 6, 3, 9, 1]
k = 2

answer = kth_largest(nums, k)

print(f"{k}nd largest:", answer)

verification = sorted(nums, reverse=True)[k - 1]
print("Verification:", verification)
