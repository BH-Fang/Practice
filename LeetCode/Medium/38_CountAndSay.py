class Solution:
    def countAndSay(self, n: int) -> str:
        
        def f(string):
            a = string[0]
            count = 0
            result = ''
            for c in string:
                if c == a:
                    count += 1
                else: 
                    result += str(count) + a
                    a = c
                    count = 1
            return result + str(count) + a
        
        s = '1'
        for _ in range(n - 1):
            s = f(s)
        
        return s
    
S = Solution()
print(S.countAndSay(42))
