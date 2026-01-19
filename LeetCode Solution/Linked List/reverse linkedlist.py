# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode):
        prev_node = None
        curr_node = head 
        while curr_node:
            temp_node = curr_node.next 
            curr_node.next = prev_node
            prev_node = curr_node 
            curr_node = temp_node 
        return prev_node 