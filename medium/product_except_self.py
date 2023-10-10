from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prev = 1
        for i in range(len(nums)):
            result.append(prev)
            prev *= nums[i]

        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= prev
            prev *= nums[i]

        return result
