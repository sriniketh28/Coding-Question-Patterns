def find_missing_number(nums):
    missing_num = 0
    nums_with_duplicates = [i for i in range(len(nums)+1)] + nums
    for num in nums_with_duplicates:
        missing_num ^= num
    return missing_num

print(find_missing_number([4,0,3,1]))
print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
print(find_missing_number([0, 1]))
