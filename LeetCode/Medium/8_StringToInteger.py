class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        a = 1
        if s[0] == '-': 
            s = s[1:]
            a = -1
        elif s[0] == '+':
            s = s[1:]
        firstNonNumIndex = len(s)
        for i, ch in enumerate(s):
            if not ch.isdigit(): 
                firstNonNumIndex = i
                break
        ans = int(s[:firstNonNumIndex]) * a if firstNonNumIndex else 0
        if ans > 2 ** 31 - 1: ans = 2 ** 31 - 1
        elif ans < (2 ** 31) * - 1: ans = (2 ** 31) * - 1
        return ans

S = Solution()
print(S.myAtoi("-+12"))
