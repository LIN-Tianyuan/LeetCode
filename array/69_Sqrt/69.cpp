class Solution {
public:
    int mySqrt(int x) {
        if (x < 2) return x;
        long left = 1, right = x / 2, middle;
        while (left <= right) {
            middle = left + ((right - left) >> 1);
            if (middle * middle < x) {
               left = middle + 1;
            } else if (middle * middle > x) {
                right = middle - 1;
            } else {
                return middle;
            }
        }
        return right;
    }
};