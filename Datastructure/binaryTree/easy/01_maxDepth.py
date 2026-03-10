
from typing import Optional

from Datastructure.binaryTree.TreeNode import TreeNode

'''
| Case          | Time | Space    |
| ------------- | ---- | -------- |
| All trees     | O(n) | O(h)     |
| Balanced tree | O(n) | O(log n) |
| Skewed tree   | O(n) | O(n)     |
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1