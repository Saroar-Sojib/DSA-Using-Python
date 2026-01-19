from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_index = 0
        total_number = 0
        for i in range(0,len(s)):
            if s[i] >= g[g_index] and g_index <= len(g)-1:
                total_number += 1
                g_index += 1
            if g_index > len(g)-1:
                break 
        return total_number

sln = Solution()
g = [1,2]
s = [1,2,3]
print(sln.findContentChildren(g,s))
