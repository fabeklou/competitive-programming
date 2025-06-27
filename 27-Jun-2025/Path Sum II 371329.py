# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path_list = []

        def dfs(node, curr_sum, path=[]):
            nonlocal path_list
            if not node:
                return
            curr_sum += node.val
            path.append(node.val)
            if not node.left and not node.right and curr_sum == targetSum:
                path_list.append(path[:])
            dfs(node.left, curr_sum, path)
            dfs(node.right, curr_sum, path)
            curr_sum -= node.val
            path.pop()
                
        dfs(root, 0)
        return path_list
