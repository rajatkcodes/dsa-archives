"""
3. Longest Substring Without Repeating Characters  (Medium)
   — https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem:
    Given a string s, find the length of the longest substring that contains no
    duplicate characters. s may be empty and can contain letters, digits,
    symbols, and spaces.

Approach:
    Sliding window with a hash map. `last_seen` records the most recent index of
    each character. A window [left, right] is expanded by moving `right` across
    the string; whenever the current character was already seen at or after
    `left`, the left edge jumps to just past that previous occurrence, which
    guarantees the window never holds a duplicate. The best window length seen
    is tracked in `max_len`. Each character is visited once.

Time:  O(n)
Space: O(min(n, k))  where k is the size of the character set
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1

            last_seen[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len
