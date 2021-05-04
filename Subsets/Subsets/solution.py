def find_subsets(nums):
    subsets = []
    subsets.append([])
    for currentNum in nums:
        for i in range(len(subsets)):
            temp = list(subsets[i])
            temp.append(currentNum)
            subsets.append(temp)
    
    return subsets

print(find_subsets([1, 3]))
print(find_subsets([1, 5, 3]))
