def find_missing_number(nums):
    return (len(nums)*(len(nums)+1))//2 - sum(nums)

print(find_missing_number([4,0,3,1]))
print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
print(find_missing_number([0, 1]))
