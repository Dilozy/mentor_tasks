nums_indexes = {}

def two_sum(nums, target):
    for index, num in enumerate(nums):
        if target - num in nums_indexes:
            return [nums_indexes[target - num], index]
        nums_indexes[num] = index

    return -1

print(two_sum([3, 2, 4], 8))