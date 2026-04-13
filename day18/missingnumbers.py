def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2   # sum of 0 to n
    actual_sum = sum(nums)

    return expected_sum - actual_sum

print(missing_number([3, 0, 1]))
print(missing_number([0,1,2,4,5]))