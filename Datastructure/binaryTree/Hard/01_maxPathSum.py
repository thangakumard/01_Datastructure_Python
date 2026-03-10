'''
Time complexity O(n)
Space Complexity O(h)
O(h) recursion stack
Where h = tree height
'''
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        self.maxSum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            current_sum = node.val + left + right
            self.maxSum = max(self.maxSum, current_sum)
            return node.val + max(left, right)
        
        dfs(root)
        return self.maxSum

