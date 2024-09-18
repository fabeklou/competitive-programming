# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        post = []
        
        def dfs(node):
            if not node:
                return
            for children in node.children:
                dfs(children)
            post.append(node.val)
        
        dfs(root)
        return post
