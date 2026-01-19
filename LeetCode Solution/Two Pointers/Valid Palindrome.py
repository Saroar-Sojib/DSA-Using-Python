import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        m = s[::-1]
        if m==s:
            return True
        else:
            return False
