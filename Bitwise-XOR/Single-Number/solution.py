def find_single_number(arr):
    num = 0
    for i in arr:
        num ^= i
    return num

print(find_single_number([1, 4, 2, 1, 3, 2, 3]))
print(find_single_number([7, 9, 7]))

# 0 ^ 30 = 30 
# 30 ^ 30 = 0
