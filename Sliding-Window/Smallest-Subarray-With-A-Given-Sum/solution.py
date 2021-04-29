import math

def smallest_subarray_with_given_sum(s, arr):
    windowStart = 0
    windowSum = 0
    min_length = math.inf
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        while(windowSum >= s):
            min_length = min(min_length, windowEnd-windowStart+1)
            windowSum -= arr[windowStart]
            windowStart += 1
    if min_length == math.inf:
        return 0
    else:
        return min_length

print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))
print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))
print(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]))

