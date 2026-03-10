#https://leetcode.com/problems/path-sum/
'''
Time complexity is O(n) since each node is visited once.
Space complexity is O(h) due to recursion stack, where h is the tree height.
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum

        leftSum = self.hasPathSum(root.left, targetSum - root.val)
        rightSum = self.hasPathSum(root.right, targetSum - root.val)
        return leftSum or rightSum