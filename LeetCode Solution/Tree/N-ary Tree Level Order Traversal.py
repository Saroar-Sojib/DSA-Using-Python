# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node'):
        if not root:
            return []
        queue = []
        queue.append(root)
        res = []
        while queue:
            level = []
            len_queue = len(queue)
            for i in range(0,len_queue):
                node = queue.pop(0)
                level.append(node.val)
                for j in node.children:
                    queue.append(j)
            res.append(level)
        return res 
        