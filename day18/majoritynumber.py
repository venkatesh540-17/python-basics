def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        elif count==candidate:
            count+=1
        else:
            count=-1
    return candidate

print(majority_element([2,2,1,1,2,2,2]))