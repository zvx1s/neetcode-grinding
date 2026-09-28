class Solution:
    def isPalindrome(self, s: str) -> bool:
        return replace(reversed(s)) == replace(s)