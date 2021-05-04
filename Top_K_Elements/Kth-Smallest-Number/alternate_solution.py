from heapq import *

def find_kth_smallest_number(nums, k):
    heapify(nums)
    for i in range(k):
        if i == k-1:
            return heappop(nums)
        else:
            heappop(nums)

print(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 3))
print(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 4))
print(find_kth_smallest_number([5, 12, 11, -1, 12], 3))

