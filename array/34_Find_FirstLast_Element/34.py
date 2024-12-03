class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getRightBorder(nums: List[int], target:int) -> int:
            left, right = 0, len(nums)
            rightBorder = -2
            while left < right:
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right = middle
                else:
                    left = middle + 1
                    rightBorder = left
            return rightBorder

        def getLeftBorder(nums: List[int], target:int) -> int:
            left, right = 0, len(nums)
            leftBorder = -2
            while left < right:
                middle = left + (right - left) // 2
                if nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle
                    leftBorder = right
            return leftBorder

        leftBorder = getLeftBorder(nums, target)
        rightBorder = getRightBorder(nums, target)
        if leftBorder == -2 or rightBorder == -2:
            return [-1, -1]
        if rightBorder - leftBorder > 0:
            return [leftBorder, rightBorder - 1]
        return [-1, -1]