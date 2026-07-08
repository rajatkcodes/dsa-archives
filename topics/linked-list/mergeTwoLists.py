"""
21. Merge Two Sorted Lists  (Easy)  — https://leetcode.com/problems/merge-two-sorted-lists/

Problem:
    Given the heads of two sorted linked lists list1 and list2, merge them into
    one sorted list by splicing together the nodes of the two input lists (no
    new nodes are created). Return the head of the merged list.

Approach:
    Classic two-pointer merge, the same step as merge sort's combine phase.
    Keep a tail pointer into the result; at each step compare the heads of the
    two lists, splice the smaller node onto the tail, and advance that list.
    A dummy head avoids special-casing the first node. When one list runs out,
    the other is already sorted, so attach the remainder in one move. Using
    <= on the comparison keeps the merge stable (ties take from list1 first).

Time:  O(m + n)
Space: O(1)  — nodes are relinked in place, no extra allocation
"""
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # Attach whichever list is left
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
