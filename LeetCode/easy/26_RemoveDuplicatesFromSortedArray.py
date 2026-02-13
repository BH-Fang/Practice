class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        lastNum = 101
        for n in nums:
            if lastNum != n:
                nums[i] = n
                lastNum = n
                i += 1
        return i