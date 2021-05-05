def find_max_in_bitonic_array(arr):
    startIndex = 0
    endIndex = len(arr) - 1
    while startIndex < endIndex:
        midIndex = (startIndex + endIndex)//2
        if arr[midIndex] > arr[midIndex + 1]:
            endIndex = midIndex
        else:
            startIndex = midIndex + 1

    return arr[startIndex]

print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
print(find_max_in_bitonic_array([3, 8, 3, 1]))
print(find_max_in_bitonic_array([1,3,8,12]))
print(find_max_in_bitonic_array([10, 9, 8]))
    
