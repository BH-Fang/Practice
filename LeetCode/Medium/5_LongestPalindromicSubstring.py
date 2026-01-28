class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        maxLen = 0
        longestSub = ''
        def isPal(string):
            l = len(string)
            for i in range(l):
                if string[i] != string[l - i - 1]:
                    return False
            return True
        
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                sub = s[i:j]
                if isPal(sub) and len(sub) > maxLen:
                    longestSub = sub
                    maxLen = len(sub)
        
        return longestSub
        '''
        l = len(s)        
        if not l or l == 1: return s
        maxLen = 0
        idx = -1
        for i in range(l):
            
            def getPalLen(left, right, l):
                while left >= 0 and right < l and s[left] == s[right]:
                    left -= 1
                    right += 1
                return right - left - 1
                
            palLen = max(getPalLen(i, i, l), getPalLen(i, i+1, l))
            if palLen > maxLen:
                idx, maxLen = i, palLen
        if maxLen % 2: return s[idx - maxLen // 2: idx + maxLen // 2 + 1]
        else: return s[idx - maxLen // 2 + 1: idx + maxLen // 2 + 1]
