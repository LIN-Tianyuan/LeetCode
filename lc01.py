"""
1. Two sum
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to hold numbers and their indexes
        num_to_index = {}
        # Iterate over each number in the array
        for index, num in enumerate(nums):
            # Calculate the difference between the target and the current figure
            difference = target - num
            # If the difference already exists in the dictionary, the answer is found
            if difference in num_to_index:
                return [num_to_index[difference], index]
            # Otherwise, store the current number and its index in the dictionary
            num_to_index[num] = index
        return []