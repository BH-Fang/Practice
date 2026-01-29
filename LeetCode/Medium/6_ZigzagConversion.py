class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        step = 1
        rows = [''] * numRows
        i = 0
        for ch in s:
            rows[i] += ch
            i += step
            if i == numRows - 1: step = -1
            elif i == 0: step = 1
        return ''.join(rows)
