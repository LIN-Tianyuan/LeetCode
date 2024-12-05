class Solution {
public:
    bool isPerfectSquare(int num) {
        if (num < 2) return true;
        long left = 1, right = num / 2, middle;
        while (left <= right) {
            middle = left + ((right - left) >> 1);
            if (middle * middle < num) {
                left = middle + 1;
            } else if (middle * middle > num) {
                right = middle - 1;
            } else {
                return true;
            }
        }
        return false;
    }
};