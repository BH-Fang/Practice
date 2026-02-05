class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        m = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        ans = []

        def re(digits, current_str, current_index):
            if current_index == len(digits):
                ans.append(current_str)
                return
            for ch in m[digits[current_index]]:
                current_str += ch
                re(digits, current_str, current_index + 1)
                current_str = current_str[:-1]
        
        re(digits, '', 0)
        return ans
    
S = Solution()
print(S.letterCombinations('23'))