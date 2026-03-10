'''
Time Complexity

O(n)
Each node is visited once.

Space Complexity

Depends on recursion depth.

O(h) where h = tree height

Worst case (skewed tree): O(n)

Balanced tree: O(log n)
'''
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, curr):
            if not node:
                return 0
            curr = (curr * 10) + node.val
            if not node.left and not node.right:
                return curr
            
            return dfs(node.left, curr) + dfs(node.right,curr)
        
        return dfs(root,0)