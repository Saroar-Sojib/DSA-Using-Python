# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2:ListNode):
        temp_node = ListNode()
        tail = temp_node 
        while list1 and list2:
            if list1.val<list2.val:
                tail.next = list1
                list1 = list1.next 
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next 
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return temp_node.next 