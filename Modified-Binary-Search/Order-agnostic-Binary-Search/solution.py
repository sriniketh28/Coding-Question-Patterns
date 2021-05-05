def order_agnostic_binary_search(arr, x):
    startIndex = 0
    endIndex = len(arr)-1
    isAscending = True if arr[startIndex] < arr[endIndex] else False
    while startIndex <= endIndex:
        midIndex = (startIndex + endIndex)//2
        if arr[midIndex] == x:
                return midIndex
        if isAscending:
            if arr[midIndex] > x:
                endIndex = midIndex - 1
            else:
                startIndex = midIndex + 1
        else:
            if arr[midIndex] < x:
                endIndex = midIndex - 1
            else:
                startIndex = midIndex + 1
    return -1

print(order_agnostic_binary_search([4, 6, 10], 10))
print(order_agnostic_binary_search([1, 2, 3, 4, 5, 6, 7], 5))
print(order_agnostic_binary_search([10, 6, 4], 10))
print(order_agnostic_binary_search([10, 6, 4], 4))

            
