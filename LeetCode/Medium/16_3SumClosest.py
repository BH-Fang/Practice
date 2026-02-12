class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            if i and nums[i] == nums[i - 1]: continue
            j = i + 1
            k = len(nums) - 1
            min_sum = nums[i] + nums[i + 1] + nums[i + 2]
            if min_sum > target:
                if abs(min_sum - target) < abs(ans - target):
                    return min_sum
                return ans
            max_sum = nums[i] + nums[-1] + nums[-2]
            if max_sum < target:
                if abs(max_sum - target) < abs(ans - target):
                    ans = max_sum
                    continue
            while k > j:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(ans - target):
                    ans = s
                if s > target: k -= 1
                elif s < target: j += 1
                else: return ans
        return ans