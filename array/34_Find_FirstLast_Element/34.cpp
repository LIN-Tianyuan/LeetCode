class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int leftBorder = getLeftBorder(nums, target);
        int rightBorder = getRightBorder(nums, target);
        if (leftBorder == -2 || rightBorder == -2) {
            return {-1, -1};
        }
        if (rightBorder - leftBorder > 0) {
            return {leftBorder, rightBorder - 1};
        }
        return {-1, -1};
    }

private:
    int getRightBorder(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size();
        int rightBorder = -2;
        while (left < right) {
            int middle = left + ((right - left) >> 1);
            if (nums[middle] > target) {
                right = middle;
            } else {
                left = middle + 1;
                rightBorder = left;
            }
        }
        return rightBorder;
    }

    int getLeftBorder(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size();
        int leftBorder = -2;
        while (left < right) {
            int middle = left + ((right - left) >> 1);
            if (nums[middle] < target) {
                left = middle + 1;
            } else {
                right = middle;
                leftBorder = right;
            }
        }
        return leftBorder;
    }
};