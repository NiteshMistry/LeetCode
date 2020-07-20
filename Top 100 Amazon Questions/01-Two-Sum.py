class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        addition = {}
        for i, num in enumerate(nums):
            if num in addition:
                return [addition[num], i]
            addition[target - num] = i
