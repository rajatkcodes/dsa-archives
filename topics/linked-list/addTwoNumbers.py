"""
2. Add Two Numbers  (Medium)  — https://leetcode.com/problems/add-two-numbers/

Problem:
    Two non-empty linked lists represent two non-negative integers, with the
    digits stored in reverse order (least-significant digit first) and one digit
    per node. Add the two numbers and return the sum as a linked list in the
    same reverse-order form. No leading zeros, except the number 0 itself.

Approach:
    Walk both lists together, one node at a time, mimicking grade-school
    addition. At each step add the two current digits plus the running carry;
    the ones place (total % 10) becomes the new node's value and the tens place
    (total // 10) becomes the carry into the next step. A dummy head node keeps
    the append logic uniform and avoids special-casing the first node. When one
    list is shorter, its missing digits are treated as 0, and any leftover carry
    after both lists are exhausted is emitted as a final node.

Time:  O(max(m, n))
Space: O(max(m, n))  for the result list
"""
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        current = dummy

        while l1 is not None or l2 is not None:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next