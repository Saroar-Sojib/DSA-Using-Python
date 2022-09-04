class Solution:
    def longestCommonPrefix(self, strs):
        len_str = len(strs[0])
        ans = ""
        for x in strs:
            if len(x)>=len_str:
                ans = x
                len_str=len(x)
        temp_res = ""
        temp_length= 0
        for i in range(0,len(ans)):
            find = True
            temp_res = ans[0:i+1]
            for x in strs:
                if temp_res!=x[0:i+1]:
                    temp_res=temp_res[0:-1]
                    find = False
                    break 
            if find == False:
                break
            else:
                temp_length=i+1
        if temp_length==0:
            return ""
        else:
            return temp_res
ans = Solution()
strs = ["a"]
print(ans.longestCommonPrefix(strs))