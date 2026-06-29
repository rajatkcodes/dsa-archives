"""
Two Sum  (Easy)  — https://leetcode.com/problems/two-sum

Approach:
    Walk the array once, keeping a dict of value -> index. For each number,
    check if (target - number) was already seen. If yes, we found the pair.
    This trades space for time: O(n) instead of the O(n^2) brute force.

Time:  O(n)
Space: O(n)
"""


def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return []
