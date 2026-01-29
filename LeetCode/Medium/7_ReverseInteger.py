class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))[::-1]
        if x >= 0: ans = int(s)
        else: ans = int(s) * -1
        if (2 ** 31) * -1 <= ans <= 2 ** 31 -1: return ans
        else: return 0 
