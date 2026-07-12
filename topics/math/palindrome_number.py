"""
9. Palindrome Number  (Easy)  — https://leetcode.com/problems/palindrome-number/

Problem:
    Given an integer x, return True if x reads the same forward and backward,
    else False. Negative numbers are never palindromes (the leading '-' breaks
    the symmetry).

Approach:
    Rebuild the number in reverse by repeatedly peeling off the last digit
    with x % 10 and appending it to `reverse`. Compare the fully reversed
    value against the original at the end.

Time:  O(log x)  — one iteration per digit.
Space: O(1)
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original, reverse = x, 0
        while x > 0:
            x, last_digit = divmod(x, 10)
            reverse = reverse * 10 + last_digit
        return original == reverse
