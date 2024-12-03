class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            middle = left + ((right - left) >> 1)
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle
            else:
                return middle
        return right