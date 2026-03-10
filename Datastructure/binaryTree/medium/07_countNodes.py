class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        left_height = self._getLeftHeight(root)
        right_height = self._getRightHeight(root)

        if left_height == right_height:
            return pow(2, right_height) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
    
    def _getLeftHeight(self,node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
    
    def _getRightHeight(self,node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height
