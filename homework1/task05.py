"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if not nums:
        print("Empty list")
        return 0
    max_sum = nums[0]
    for ind in range(len(nums)):
        sum_to_check = 0
        for element in nums[ind : ind + k]:
            sum_to_check += element
            if sum_to_check > max_sum:
                max_sum = sum_to_check
    return max_sum
