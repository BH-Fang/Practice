class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        inverse = False
        rows = []
        for _ in range(numRows):
            rows.append('')
        i = 0
        for ch in s:
            rows[i] += ch
            if not inverse: i += 1
            else: i -= 1
            if i == numRows - 1: inverse = True
            elif i == 0: inverse = False
        return ''.join(rows)
