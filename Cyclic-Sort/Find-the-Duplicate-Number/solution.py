def find_duplicate(nums):
    i = 0
    while i<len(nums):
        j = nums[i]
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for i in range(len(nums)):
        if nums[i] != i+1:
            return nums[i]


print(find_duplicate([1, 4, 4, 3, 2]))
print(find_duplicate([2, 1, 3, 3, 5, 4]))
print(find_duplicate([2, 4, 1, 4, 4]))
