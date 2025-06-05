# Problem: Intersection of two linked lists - https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptrA = headA
        while ptrA:
            setattr(ptrA, 'x', -1)
            ptrA = ptrA.next
        ptrB = headB
        while ptrB:
            if hasattr(ptrB, 'x'):
                return ptrB
            ptrB = ptrB.next
        return None
