from heapq import *

def find_k_largest_numbers(nums, k):
    min_heap = []
    for i in range(k):
        heappush(min_heap, nums[i])

    for i in range(k, len(nums)):
        if min_heap[0] < nums[i]:
            heappop(min_heap)
            heappush(min_heap, nums[i])

    return min_heap

print(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3))
print(find_k_largest_numbers([5, 12, 11, -1, 12], 3))

