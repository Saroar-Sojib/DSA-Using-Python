class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        ls = []
        while head:
            ls.append(head.val)
            head = head.next 
        ls.reverse()
        ls.pop(n-1)
        ls.reverse()
        cur=dummy=ListNode(0)
        for x in ls:
            cur.next = ListNode(x)
            cur = cur.next 
        return dummy.next