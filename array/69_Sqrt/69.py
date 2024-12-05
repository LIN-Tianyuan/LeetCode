class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            middle = left + ((right - left) >> 1)
            if middle * middle < x:
                left = middle + 1
            elif middle * middle > x:
                right = middle - 1
            else:
                return middle
        return right
