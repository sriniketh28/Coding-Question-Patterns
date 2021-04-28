def max_sub_array_of_size_k(k, arr):
    windowStart = 0
    windowSum = 0
    max_sum = 0
    for windowEnd in range(len(arr)):
        windowSum+=arr[windowEnd]
        if windowEnd >= k-1:
            max_sum = max(max_sum, windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1

    return max_sum

print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))
            
