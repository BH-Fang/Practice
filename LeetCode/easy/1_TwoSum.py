class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            for i1, n1 in enumerate(nums[i + 1:]):
                if n + n1 == target: return [i, i1 + i + 1]
            