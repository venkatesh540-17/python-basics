def find_pairs(nums, target):
    seen = set()
    output = set()

    for num in nums:
        diff = target - num
        if diff in seen:
            pair = tuple(sorted((num, diff)))
            output.add(pair)
        seen.add(num)

    return list(output)

print(find_pairs([2, 4, 3, 5, 7, -1, 4], 6))