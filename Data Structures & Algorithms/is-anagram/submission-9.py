class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firsthash = {}
        mylist = []
        mysecondlist = []
        for i in range(len(s)):
            mylist.append(s[i])
        mylist = sorted(mylist)

        for i in range(len(t)):
            mysecondlist.append(t[i])
        mysecondlist = sorted(mysecondlist)
        
        if mylist == mysecondlist:
            return True
            
        else:
            return False