class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        ans = []
        candidates.sort()
        
        current = []
        def dfs(start_index, current_sum):
            if current_sum == target: 
                ans.append(current.copy())
                return
            if current_sum > target:
                return
            for i in range(start_index, n):
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                if current_sum + candidates[i] > target: return
                current.append(candidates[i])
                dfs(i + 1, current_sum + candidates[i])
                current.pop()
        
        dfs(0, 0)
        return ans

S = Solution()
print(S.combinationSum2([10,1,2,7,6,1,5], 8))