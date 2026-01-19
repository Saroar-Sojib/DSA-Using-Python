class Solution:
    def plusOne(self, digits):
        rm = 0
        ans = digits[-1]+1
        rm = ans//10
        digits[-1]=ans%10
        for i in range(len(digits)-2,-1,-1):
            ans = digits[i]+rm
            digits[i]=ans%10
            rm = ans//10
        if rm!=0:
            digits.insert(0,rm)
        return digits

ans = Solution()
digits=[1,2,3]
print(ans.plusOne(digits))