# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True

        if not root.left or not root.right:
            return False

        dq = deque([(root.left, 'l'), (root.right, 'r')])

        while dq:
            lvl_arr = [(n.val if n else -101, d) for n, d in dq]
            if len(lvl_arr) % 2:
                return False
            for left, right in zip(lvl_arr[:len(dq)//2], lvl_arr[len(dq)//2:][::-1]):
                if left[0] != right[0] or left[1] == right[1]:
                    return False
            for _ in range(len(dq)):
                node, _ = dq.popleft()
                if node:
                    if node.left:
                        dq.append((node.left, 'l'))
                    else:
                        dq.append((None, 'l'))
                if node:
                    if node.right:
                        dq.append((node.right, 'r'))
                    else:
                        dq.append((None, 'r'))

        return True
