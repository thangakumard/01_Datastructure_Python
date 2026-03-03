from typing import List, Optional

from Datastructure.binaryTree.TreeNode import TreeNode
'''
Time Complexity O(n)
Space Complexity O(n)
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inordermap ={}
        self.preorderIndex = 0
        for i in range(len(inorder)):
            inordermap[inorder[i]] = i
        
        def heler(start:int, end:int):
            if start > end:
                return None
            
            root = TreeNode(preorder[self.preorderIndex])
            self.preorderIndex += 1
            mid = inordermap[root.val]

            root.left = heler(start, mid-1)
            root.right = heler(mid+1, end)
            return root
        
        return heler(0,len(preorder)-1)