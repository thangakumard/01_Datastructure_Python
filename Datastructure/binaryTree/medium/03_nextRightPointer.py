
# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

'''
| Case         | Time | Space |
| ------------ | ---- | ----- |
| All cases    | O(n) | O(w)  |
| Perfect tree | O(n) | O(n)  |
| Skewed tree  | O(n) | O(1)  |

Where w = maximum width of tree
'''

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        dequeNodes = deque([root])

        while dequeNodes:
            size = len(dequeNodes)
            prevNode = None

            for _ in range(size):
                curNode = dequeNodes.popleft()
                if prevNode:
                    prevNode.next = curNode
                prevNode = curNode

                if curNode.left:
                    dequeNodes.append(curNode.left)

                if curNode.right:
                    dequeNodes.append(curNode.right)

        return root
        