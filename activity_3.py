from activity_2 import MaxHeap

def heap_sort(arr):
    heap = MaxHeap()

    for value in arr:
        heap.insert(value)

    sorted_arr = []

    while heap.size() > 0:
        sorted_arr.insert(0, heap.extract())

    return sorted_arr


print("\n=== Activity 3: Heap Sort ===")

tests = [
    [4, 10, 3, 5, 1],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [4, 4, 2, 2, 1],
    []
]

for test in tests:
    print("Original:", test)
    print("Sorted  :", heap_sort(test))
    print()