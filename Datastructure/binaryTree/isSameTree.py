from typing import Optional

from Datastructure.binaryTree.TreeNode import TreeNode

'''
| Case          | Time | Space    |
| ------------- | ---- | -------- |
| Worst case    | O(n) | O(h)     |
| Balanced tree | O(n) | O(log n) |
| Skewed tree   | O(n) | O(n)     |
| Best case     | O(1) | O(1)     |
'''

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        else:
            return (p.val == q.val) and \
                   self.isSameTree(p.left, q.left) and \
                   self.isSameTree(p.right, q.right)