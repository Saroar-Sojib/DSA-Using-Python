"""
    Input: s = "abccccdd"
    Output: 7
    Explanation: One longest palindrome that 
    can be built is "dccaccd", whose length is 7.
    Docstring for LeetCode Solution.Greedy.Longest Palingdrome
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        computed_dict = {}
        for rec in s:
            if rec in computed_dict:
                computed_dict[rec]+= 1
            else:
                computed_dict[rec] = 1
        palingdrom_lenght = 0
        is_one = False 
        for cnt in computed_dict:
            if computed_dict[cnt] % 2 == 0:
                palingdrom_lenght += computed_dict[cnt]
            else:
                palingdrom_lenght += (computed_dict[cnt]-1)
                is_one = True
        if is_one:
            palingdrom_lenght += 1
        return palingdrom_lenght
            
sln = Solution()
print(sln.longestPalindrome("abccccdd"))
        