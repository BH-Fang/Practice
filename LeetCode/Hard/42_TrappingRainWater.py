class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        ans = 0
        ls, rs = [], []
        lm = height[0]
        for h in height:
            if h > lm: 
                lm = h
            ls.append(lm)
        
        lm = height[n - 1]
        li =  n
        for i in range(n - 1, -1, -1):
            h = height[i]
            if h > lm: 
                lm = h
            rs.append(lm)
        rs.reverse()
        for i, h in enumerate(height):
            ans += min(ls[i], rs[i]) - h
        
        return ans
        
S = Solution()
print(S.trap([0,1,0,2,1,0,1,3,2,1,2,1]))