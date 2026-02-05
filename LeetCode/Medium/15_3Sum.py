class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]: continue
            if nums[i] > 0: break
            j, k = i + 1, len(nums) - 1
            while j < k:
                t = (nums[j] + nums[k]) * -1
                if t < nums[i]:
                    k -= 1
                elif t > nums[i]:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    while True:
                        j += 1
                        if j > k or nums[j] != nums[j - 1]: break
                    while True:
                        k -= 1
                        if j > k or nums[k] != nums[k + 1]: break
        return ans

S = Solution()
print(S.threeSum([0, 0, 0]))