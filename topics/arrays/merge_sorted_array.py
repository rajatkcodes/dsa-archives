"""
88. Merge Sorted Array  (Easy)  — https://leetcode.com/problems/merge-sorted-array/

Problem:
    nums1 (length m+n) holds m real values followed by n zeros to ignore.
    nums2 holds n values. Both are sorted non-decreasing. Merge them into a
    single sorted array stored in-place inside nums1.

Approach:
    Take the first m real elements of nums1, concatenate nums2, sort the
    combined list, and write it back into nums1 using slice assignment
    (nums1[:] = ...), which mutates the original list in place as required.

    Simple and clean. Note it re-sorts from scratch rather than exploiting
    that both inputs are already sorted (a back-to-front two-pointer merge
    would be O(m + n) time and O(1) space).

Time:  O((m + n) log(m + n))
Space: O(m + n)
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Do not return anything, modify nums1 in-place instead."""
        nums1[:] = sorted(nums1[:m] + nums2)
