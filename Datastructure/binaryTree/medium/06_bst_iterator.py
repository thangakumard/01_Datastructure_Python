
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator(object):
    
    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        self._pushleft(root)
    
    def _pushleft(self, node):
        if not node:
            return
        while node:
            self.stack.append(node)
            node = node.left
            
    def next(self):
        """
        :rtype: int
        """
        curr = self.stack.pop()

        if curr.right:
            self._pushleft(curr.right)
        return curr.val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0
        


#  Your BSTIterator object will be instantiated and called as such:
#  obj = BSTIterator(root)
#  param_1 = obj.next()
#  param_2 = obj.hasNext()