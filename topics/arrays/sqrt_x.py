"""
69. Sqrt(x)  (Easy)  — https://leetcode.com/problems/sqrtx/

Problem:
    Given a non-negative integer x, return the square root of x rounded down
    to the nearest integer. You must not use any built-in exponent function
    or operator (no pow(x, 0.5), no x ** 0.5).

Approach:
    Binary search for the largest integer mid with mid * mid <= x. The answer
    lies in [1, x // 2] for x >= 2 (since sqrt(x) <= x / 2 there), with x < 2
    handled directly. When the loop ends, hi has settled on floor(sqrt(x)).

Time:  O(log x)
Space: O(1)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        lo, hi = 1, x // 2
        while lo <= hi:
            mid = (lo + hi) // 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
