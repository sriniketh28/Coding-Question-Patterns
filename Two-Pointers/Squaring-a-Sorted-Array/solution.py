def make_squares(arr):
    left, right = 0, len(arr)-1
    lastIndex = len(arr)-1
    squares = [0] * len(arr)
    while(left <= right):
        leftSquare = arr[left]*arr[left]
        rightSquare = arr[right]*arr[right]
        if leftSquare > rightSquare:
            squares[lastIndex] = leftSquare
            left += 1
        if rightSquare >= leftSquare:
            squares[lastIndex] = rightSquare
            right -= 1
        lastIndex -= 1
    return squares

print(make_squares([-2, -1, 0, 2, 3]))
print(make_squares([-3, -1, 0, 1, 2]))

