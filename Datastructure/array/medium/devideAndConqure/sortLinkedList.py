
#Time complexity: O(n log n)
#Space complexity: O(log n) due to recursion stack
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 1) Split list into two halves
        left, right = self.split(head)

        # 2) Sort each half
        left = self.sortList(left)
        right = self.sortList(right)

        # 3) Merge sorted halves
        return self.merge(left, right)

    def split(self, head: ListNode) -> tuple[ListNode, Optional[ListNode]]:
        """
        Split the linked list into two halves.
        Returns (left_head, right_head).
        """
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # cut the list
        prev.next = None
        return head, slow

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:     # <= makes it stable
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2
        return dummy.next