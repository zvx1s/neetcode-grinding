class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        h = s.replace(" ", "")
        if h[::-1] == h:
            return True
        
        return False