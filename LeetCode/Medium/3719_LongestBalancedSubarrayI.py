class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n - 1):
            s = set()
            odd_count, even_count = 0, 0
            for j in range(i, n):
                num = nums[j]
                if num not in s: 
                    s.add(num)
                    if num % 2: odd_count += 1
                    else: even_count += 1
                if odd_count == even_count and j - i + 1 > ans:
                    ans =  j - i + 1
        return ans

S = Solution()
print(S.longestBalanced([2,5,4,3]))