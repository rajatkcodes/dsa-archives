"""
125. Valid Palindrome  (Easy)  — https://leetcode.com/problems/valid-palindrome/

Problem:
    A phrase is a palindrome if, after lowercasing all letters and removing every
    non-alphanumeric character, it reads the same forward and backward.
    Given a string s, return True if it is a palindrome, else False.

Two approaches below:

  1. clean + reverse : build a filtered/lowercased string, compare with its
                        reverse. Readable one-liner, but allocates O(n) memory.
  2. two pointers    : walk inward from both ends, skipping non-alphanumeric
                        characters and comparing in place. O(1) extra space and
                        can short-circuit on the first mismatch.

Both run in O(n) time; the difference is space and early-exit behaviour.
"""


class Solution:
    # --- Approach 1: clean + reverse --------------------------------------
    # Time:  O(n)  — one pass to build `cleaned`, one to reverse/compare.
    # Space: O(n)  — `cleaned` plus its reversed copy.
    def isPalindrome_clean(self, s: str) -> bool:
        cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
        return cleaned == cleaned[::-1]

    # --- Approach 2: two pointers (more optimised) ------------------------
    # Time:  O(n)  — each pointer moves at most n steps total.
    # Space: O(1)  — no extra allocation; returns early on first mismatch.
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
