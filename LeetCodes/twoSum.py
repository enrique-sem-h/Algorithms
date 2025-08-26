# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        history = dict() # store number, index as we go through nums array
        
        for i, num in enumerate(nums):
            remain = target - num
            if remain in history:
                return [history[remain], i]
            history[num] = i

print(Solution().twoSum([2, 1, 3, 4], 2))