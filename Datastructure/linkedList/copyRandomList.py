from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

'''
Time complextiy O(n)
Space complexity O(1)
'''

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old_to_new = {}
        #First pass
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        
        curr = head
        dummy = Node(0)
        copy_curr = dummy

        while curr:
            copy = curr.next
            curr.next = curr.next.next
            copy_curr.next = copy

            curr = curr.next
            copy_curr = copy_curr.next
        
        return dummy.next


'''
Time complextiy O(n)
Space complexity O(n)
'''
def copyRandomList_map(self, head: 'Optional[Node]') -> 'Optional[Node]':
    if not head:
        return None
    
    old_to_new = {}
    #First pass
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    #Second pass
    curr = head
    while curr:
        old_to_new[curr].next = old_to_new.get(curr.next)
        old_to_new[curr].random = old_to_new.get(curr.random)
        curr = curr.next

    return old_to_new[head] 

