def find_subsets(arr):
    if len(arr) == 0:
        return [[]]
    temp = find_subsets(arr[1:])
    return temp + [[arr[0]] + subset for subset in temp]

print(find_subsets([1, 3]))
print(find_subsets([1,5,3]))
