/*
 * 26. Remove Duplicates from Sorted Array
 */

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // Idea: keep the one that is different from the previous one
        // Detailed judgment: i-1 cannot cross the boundary, and the 0th one must
        int n = 0;
        for(int i = 0; i < nums.size(); i++){
            if(i == 0 || nums[i] != nums[i - 1]){
                nums[n] = nums[i];
                n++;
            }
        }
        return n;
    }
};