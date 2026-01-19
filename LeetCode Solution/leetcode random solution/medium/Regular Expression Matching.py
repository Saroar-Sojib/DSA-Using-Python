import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s=' '+s+' '
        p='\s'+p+'\s'

        if re.search(p,s):
            return True
        else:
            return False
ans = Solution()
s = "aa"
p = "a*"
print(ans.isMatch(s,p))