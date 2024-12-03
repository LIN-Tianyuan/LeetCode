class Solution {
    public int[] searchRange(int[] nums, int target) {
        int leftBorder = getLeftBorder(nums, target);
        int rightBorder = getRightBorder(nums, target);
        if (leftBorder == -2 || rightBorder == -2) {
            return new int[]{-1, -1};
        }
        if (rightBorder - leftBorder > 0){
            return new int[]{leftBorder, rightBorder - 1};
        }
        return new int[]{-1, -1};
    }

    public int getLeftBorder(int[] nums, int target) {
        int left = 0;
        int right = nums.length;
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

    public int getRightBorder(int[] nums, int target) {
        int left = 0;
        int right = nums.length;
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
}