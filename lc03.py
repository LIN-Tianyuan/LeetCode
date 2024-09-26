"""
3. Longest Substring Without Repeating Characters
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        max_length = 0
        start = 0

        for end in range(len(s)):
            if s[end] in char_index_map:
                # Update the start position of the window to the next position of the repeating character, but only move it to the right
                start = max(start, char_index_map[s[end]] + 1)
            # Update the latest index of characters
            char_index_map[s[end]] = end
            # Calculates the current window length and updates the maximum length
            max_length = max(max_length, end - start + 1)
        return max_length


