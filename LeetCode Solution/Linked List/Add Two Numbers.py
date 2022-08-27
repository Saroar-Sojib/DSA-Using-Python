# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):    
        ls1=[]
        ls2=[]
        while l1:
            ls1.append(l1.val)
            l1=l1.next
        while l2:
            ls2.append(l2.val)
            l2 = l2.next
        ls1_len = len(ls1)
        ls2_len = len(ls2)
        if ls1_len<ls2_len:
            len_diff = ls2_len - ls1_len
            for i in range(0,len_diff):
                ls1.append(0)
        else:
            len_diff = ls1_len - ls2_len 
            for i in range(0,len_diff):
                ls2.append(0)
        res=[]
        reminder = 0
        for i in range(0,len(ls1)):
            summ = ls1[i]+ls2[i]+reminder
            if summ>=10:
                reminder = 1
                res.append(summ%10)
            else:
                reminder = 0
                res.append(summ)
        if reminder ==1:
            res.append(reminder)
        cur = dummy = ListNode(0)
        for e in res:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next 
        
        