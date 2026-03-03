from typing import List,Optional
from Datastructure.binaryTree.TreeNode import TreeNode

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {}
        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i
        postOrderIndex = len(postorder)-1

        def build(start: int, end:int):
            nonlocal postOrderIndex
            if start > end:
                return None
            
            rootVal = postorder[postOrderIndex]
            postOrderIndex -=1
            root = TreeNode(rootVal)
            mid = inorderMap[rootVal]

            root.right = build(mid+1, end)
            root.left = build(start, mid-1)
            return root
        
        return build(0, len(inorder)-1)