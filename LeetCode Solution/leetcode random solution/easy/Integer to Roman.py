class Solution:
    def intToRoman(self, num: int) -> str:
        val={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        res = ''
        for y in val:
            n=num//y
            num=num%y
            for i in range(0,n):
                res+=val[y]
        return res
            
            
ans = Solution()
print(ans.intToRoman(1994))