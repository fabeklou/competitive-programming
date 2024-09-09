# Problem: Path Sum - https://leetcode.com/problems/path-sum/

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root: return False

        def dfs(node, pathSum):
            if not node.left and not node.right:
                return pathSum + node.val == targetSum
            
            pathSum += node.val
            if node.left and dfs(node.left, pathSum):
                return True
            if node.right and dfs(node.right, pathSum):
                return True

            pathSum -= node.val

        return dfs(root, 0)
