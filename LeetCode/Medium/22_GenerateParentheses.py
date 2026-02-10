class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def rc(curr, left, right, n):
            if left == right == n: 
                ans.append(curr)
                return
            if left < n: 
                rc(curr + '(', left + 1, right, n)
            if right < left:
                rc(curr + ')', left, right + 1, n)
        
        rc('', 0, 0, n)
        return ans

