"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyhash = { None: None}

        curr = head

        while curr:
            copy = Node(curr.val)
            copyhash[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = copyhash[curr]
            copy.next = copyhash[curr.next]
            copy.random = copyhash[curr.random]
            curr= curr.next

        return copyhash[head]