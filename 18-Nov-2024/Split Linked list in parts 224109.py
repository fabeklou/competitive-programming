# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        nodes = 0
        curr = head
        while curr:
            curr = curr.next
            nodes += 1
        size, rest = nodes // k, nodes % k
        groups = [size for _ in range(k)]
        for i in range(rest):
            groups[i] += 1
        prev = curr = head
        pos = 0
        curr_len = 0
        result = [None] * k
        while curr:
            prev = curr
            curr = curr.next
            curr_len += 1
            if curr_len == groups[pos]:
                prev.next = None
                result[pos] = head
                pos += 1
                head = curr
                curr_len = 0
        return result
