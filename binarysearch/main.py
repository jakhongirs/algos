# 01 - Split List (Easy):
# https://binarysearch.com/problems/Split-List

import math

nums = [0, 2, 1]


def solution(nums):
    length = math.floor(len(nums) / 2)

    left = nums[0: length]
    right = nums[length:]

    all = []

    for left_num in left:
        for right_num in right:
            if (left_num < right_num):
                all.append(True)
            else:
                all.append(False)

    if (False not in all):
        return True
    else:
        return False


print(solution(nums))
