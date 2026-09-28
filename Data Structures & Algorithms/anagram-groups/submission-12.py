class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newarray = []
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    newarray.append([strs[i], strs[j]])
                else:
                    newarray.append([strs[j]])    
                    
        return newarray