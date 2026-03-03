from typing import Optional

from Datastructure.binaryTree.TreeNode import TreeNode
'''
| Case       | Time | Space    |
| ---------- | ---- | -------- |
| Worst case | O(n) | O(h)     |
| Balanced   | O(n) | O(log n) |
| Skewed     | O(n) | O(n)     |
| Best case  | O(1) | O(1)     |
'''

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, n1: Optional[TreeNode],n2: Optional[TreeNode]) -> bool:
        if not n1 and not n2:
            return True
        if not n1 or not n2:
            return False
        return n1.val == n2.val and self.isMirror(n1.left, n2.right) and self.isMirror(n1.right, n2.left)