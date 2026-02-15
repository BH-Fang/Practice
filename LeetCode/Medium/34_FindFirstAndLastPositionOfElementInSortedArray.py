class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binarySearch(isStart: bool) -> int:
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    if isStart:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return index
        
        start = binarySearch(True)
        if start == -1: return [-1, -1]
        end = binarySearch(False)
        return [start, end]

S = Solution()
print(S.searchRange([5,7,7,8,8,10], 6))