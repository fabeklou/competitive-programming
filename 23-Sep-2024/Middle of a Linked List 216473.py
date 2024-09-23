# Problem: Middle of a Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hare = rabbit = head
        while rabbit and rabbit.next:
            rabbit = rabbit.next
            if rabbit:
                rabbit = rabbit.next
            hare = hare.next
        return hare
