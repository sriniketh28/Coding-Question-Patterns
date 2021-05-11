def find_subsets(nums):
    subsets = []
    for i in range(2**len(nums)):
        temp = []
        for j in range(len(nums)):
            if i & 1 == 1:
                temp.append(nums[j])
            i >>= 1
        subsets.append(temp)

    return subsets

print(find_subsets([1, 3]))
print(find_subsets([1, 5, 3]))
