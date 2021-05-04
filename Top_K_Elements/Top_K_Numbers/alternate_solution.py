from heapq import *

def find_k_largest_numbers(nums, k):
    heapify(nums)
    return nlargest(k, nums)

print(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3))
print(find_k_largest_numbers([5, 12, 11, -1, 12], 3))
