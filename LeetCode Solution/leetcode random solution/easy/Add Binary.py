class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b)<len(a):
            a,b=b,a
        if len(a)<=len(b):
            temp_len = len(b)-len(a)
            s=""
            for i in range(0,temp_len):
                s+="0"
            a=s+a
        res = ""
        rm=0
        for i in range(len(a)-1,-1,-1):
            summ=int(a[i])+int(b[i])+rm
            rm = summ//2
            res+=str(summ%2)
        if rm!=0:
            res+=str(rm)
        res = res[::-1]
        return res 
ans = Solution()
a="111"
b="1010"
print(ans.addBinary(a,b))