def longest_common_prefix(input):
    prefix = input[0]

    for word in input[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""

    return prefix


# Test
input_list = ["fly", "flow", "flower", "flour"]
print(longest_common_prefix(input_list))