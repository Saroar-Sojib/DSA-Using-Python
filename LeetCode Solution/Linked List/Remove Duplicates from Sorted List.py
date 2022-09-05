class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        temp_list=[]
        while head:
            temp_list.append(head.val)
            head = head.next 
        res = []
        for x in temp_list:
            if x not in res:
                res.append(x)
        cur=dummy=ListNode(0)
        for x in res:
            cur.next = ListNode(x)
            cur = cur.next
        return dummy.next

ans = Solution()
print(ans.deleteDuplicates([1,1,2]))
        