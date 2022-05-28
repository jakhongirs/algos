# 268. Missing Number
# https://leetcode.com/problems/missing-number/

nums = [3, 0, 1]


def missingNumber(nums):
    length = len(nums)
    all_possible_nums = []
    result = None

    for num in range(length + 1):
        all_possible_nums.append(num)

    for num in nums:
        if num in all_possible_nums:
            all_possible_nums.remove(num)

    return all_possible_nums[0]


print(missingNumber(nums))
