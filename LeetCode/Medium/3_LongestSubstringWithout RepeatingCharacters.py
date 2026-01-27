'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = ''
        M = 0
        i = 0
        l = len(s)
        while i < l:
            ch = s[i]
            if ch not in subString:
                subString += ch 
            else:
                i -= (len(subString) - subString.index(ch))
                M = max(M, len(subString))
                subString = ''
            i += 1
        return max(M, len(subString))
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        di = dict()
        M = 0
        left = 0
        for i, ch in enumerate(s):
            if ch not in di:
                di[ch] = i
            else:
                left = max(left, di[ch] + 1)
                di[ch] = i
            M = max(M, i - left + 1)
        return M