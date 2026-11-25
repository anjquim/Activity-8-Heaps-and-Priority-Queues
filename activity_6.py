import heapq
import random

def priority_scheduler(jobs):
    pq = []

    for priority, name in jobs:
        heapq.heappush(pq, (-priority, name))

    release_order = []

    while pq:
        priority, name = heapq.heappop(pq)
        release_order.append(name)

    return release_order


print("\n=== Activity 6: Priority Scheduler ===")

jobs = [
    (3, "Job A"),
    (5, "Job B"),
    (1, "Job C"),
    (4, "Job D")
]

order = priority_scheduler(jobs)

print("Release order:")
for job in order:
    print(job)