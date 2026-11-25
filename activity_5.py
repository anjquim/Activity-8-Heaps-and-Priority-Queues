import heapq
import random

def merge_k_sorted_arrays(arrays):
    heap = []

    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    merged = []

    while heap:
        value, array_idx, element_idx = heapq.heappop(heap)

        merged.append(value)

        next_idx = element_idx + 1

        if next_idx < len(arrays[array_idx]):
            heapq.heappush(
                heap,
                (
                    arrays[array_idx][next_idx],
                    array_idx,
                    next_idx
                )
            )

    return merged


print("\n=== Activity 5: Merge K Sorted Arrays ===")

arrays = [
    [1, 4, 7, 10],
    [2, 5],
    [3, 6, 8, 9, 11]
]

merged = merge_k_sorted_arrays(arrays)

print("Merged:", merged)
