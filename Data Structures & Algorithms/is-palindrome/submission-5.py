class Solution:
    def isPalindrome(self, s: str) -> bool:
        h = ""
        for i in range(len(s)):
            if s[i].isalnum():
                h += s[i]
        h = h.lower()
        h = h.replace(" ", "")
        if h[::-1] == h:
            return True
        
        return False