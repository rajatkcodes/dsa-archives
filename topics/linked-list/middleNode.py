# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
876. Middle of the Linked List  (Easy)  — https://leetcode.com/problems/middle-of-the-linked-list/

Problem:
    Given the head of a singly linked list, return the middle node. If there
    are two middle nodes, return the second one.

Approach:
    Fast/slow pointers. `second` moves two nodes for every one `first` moves,
    so when `second` reaches the end, `first` is sitting on the middle.

Time:  O(n)
Space: O(1)
"""

from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        second = head
        while second and second.next:
            first = first.next
            second = second.next.next
        return first
