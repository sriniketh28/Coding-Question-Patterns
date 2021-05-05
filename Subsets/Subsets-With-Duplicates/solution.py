def find_non_duplicate_subsets(nums):
    subsets = []
    subsets.append([])
    startIndex, endIndex = 0, 0
    for i in range(len(nums)):
        startIndex = 0
        if i > 0 and nums[i] == nums[i-1]:
            startIndex = endIndex + 1
        endIndex = len(subsets) - 1
        for j in range(startIndex, endIndex+1):
            temp = list(subsets[j])
            temp.append(nums[i])
            subsets.append(temp)
    
    return subsets


print(find_non_duplicate_subsets([1, 3, 3]))
print(find_non_duplicate_subsets([1, 5, 3, 3]))
