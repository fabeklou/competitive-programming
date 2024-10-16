# Problem: Swapping Nodes in a Linked List - https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = right = None
        hare = turtle = head

        for _ in range(k - 1):
            hare = hare.next
        left = hare

        while hare and hare.next:
            hare = hare.next
            turtle = turtle.next
        right = turtle

        # swap the Nodes values
        left.val, right.val = right.val, left.val

        return head
