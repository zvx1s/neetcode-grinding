class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s.sort() == t.sort():
            return True
        return False