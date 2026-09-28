class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if ord(sorted(s)) == ord(sorted(t)):
            return True