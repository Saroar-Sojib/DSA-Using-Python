# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        ls = []
        while head:
            ls.append(head.val)
            head = head.next 
        if ls==ls[::-1]:
            return True
        else:
            return False