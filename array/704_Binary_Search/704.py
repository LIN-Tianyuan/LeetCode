class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)  # [left ,right)

        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle
            else:
                return middle
        
        return -1   # Target value not found