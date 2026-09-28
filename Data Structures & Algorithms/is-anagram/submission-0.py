class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = s.sort()
        n = t.sort()
        if m == n:
            return True
        return False