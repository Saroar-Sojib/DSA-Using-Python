class Solution:
    def myAtoi(self, s: str) -> int:
        temp_str = ''
        cnt=0
        for i in range(0,len(s)):
            if s[i] != ' ':
                break 
            cnt+=1
        temp_str=s[cnt:]
        s = temp_str
        find = ''
        cnt = 0
        if len(s)==0:
            return 0 
        if s[0]=='+' or s[0]=='-':
            find = s[0]
            cnt+=1
        temp_str = ''
        for i in range(0,len(s)):
            if i ==0 and cnt==1:
                continue
            elif s[i].isdigit():
                temp_str+=s[i]
            else:
                break 
            
        res = temp_str
        if len(find+res)==1 and (find+res=='+' or res=='-'):
            return 0
        elif res.isdigit():
            res = find+res
            res = int(res)
            if res>=(-2)**31 and res<=((2)**31)-1:
                return res
            else: 
                if res < (-2)**31:
                    return -2147483648
                elif res> ((2)**31)-1:
                    return 2147483647  
        return 0 
        
                   
ans = Solution()
print(ans.myAtoi("   +0 123"))