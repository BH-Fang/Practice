class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = 0
        while True:
            if i == len(s): break
            if s[i] == s[i + 1]:
                del s[i]
                i = 0
                continue
            i += 1
        return len(s)

