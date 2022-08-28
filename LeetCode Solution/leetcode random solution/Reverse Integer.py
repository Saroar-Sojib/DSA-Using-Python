class Solution:
    def reverse(self, x: int) -> int:
        temp_val = str(x)
        if '-' in temp_val:
            res = temp_val[1:]
            res = res[::-1]
            res = '-'+res
            res = int(res)
            if res>=(-2)**31 and res<=((2)**31)-1:
                return res
            else:
                return 0
            
        else:
            temp_val = temp_val[::-1]
            temp_val = int(temp_val)
            if temp_val>=(-2)**31 and temp_val<=((2)**31)-1:
                return temp_val
            else:
                return 0

a = Solution()
print(a.reverse(-123))