# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def conquer(left, right):
            dummy = ListNode(-1)
            prev = dummy
            while left and right:
                if left.val <= right.val:
                    prev.next = left
                    prev = left
                    left = left.next
                else:
                    prev.next = right
                    prev = right
                    right = right.next
            prev.next = left if left else right
            return dummy.next

        def divide(head):
            if not head or not head.next:
                return head

            hare = prev = turtle = head

            while hare and hare.next:
                prev, turtle = turtle, turtle.next
                hare = hare.next.next
            prev.next = None

            head1 = divide(head)
            head2 = divide(turtle)

            return conquer(head1, head2)

        return divide(head)