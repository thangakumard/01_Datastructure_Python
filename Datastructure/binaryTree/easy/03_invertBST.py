from typing import Optional
from Datastructure.binaryTree.TreeNode import TreeNode
'''
| Case      | Time | Space    |
| --------- | ---- | -------- |
| All cases | O(n) | O(h)     |
| Balanced  | O(n) | O(log n) |
| Skewed    | O(n) | O(n)     |
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root