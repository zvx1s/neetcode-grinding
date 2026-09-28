class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newarray = []
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if sorted(str[i]) == sorted(str[i+1]):
                    newarray.append([str[i], str[i+1]]) 
                
        return newarray