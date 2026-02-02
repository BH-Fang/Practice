class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        M = 0
        while j > i:
            hi, hj = height[i], height[j]
            mh = min(hi, hj)
            area = (j - i) * mh
            if area > M: M = area
            if mh == hi: i += 1
            else: j -= 1
        return M