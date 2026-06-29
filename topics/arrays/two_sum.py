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


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    print("ok")
