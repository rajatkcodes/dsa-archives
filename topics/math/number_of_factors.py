"""
Number of Factors  (Easy)  — https://www.geeksforgeeks.org/problems/number-of-factors1435/1

Problem:
    Find the number of factors of a given integer n.

Approach:
    Factors come in pairs (i, n // i) for i in [1, sqrt(n)]. Special-case
    n == 1 (only factor is itself). Otherwise start the count at 2 to account
    for the trivial factors 1 and n, then walk i from 2 up to sqrt(n): each
    divisor found contributes its pair too, unless i is the square root
    itself (i == n // i), in which case it's only counted once.

Time:  O(sqrt(n))
Space: O(1)
"""


class Solution:
    def countFactors(self, n):
        if n == 1:
            return 1

        factors = 2
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                factors += 1
                if i != n // i:
                    factors += 1
        return factors
