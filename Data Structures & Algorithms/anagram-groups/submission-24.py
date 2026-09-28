class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        for i in range(len(strs)):
            strs[i] = sorted(strs[i])
        hashy = {}
        for i, wrd in enumerate(strs):
            if wrd in hashy:
                hashy[wrd] = i
        




'''Sort each element alphabetically, then use the hashmap to check if it's already been added to it or not, then add the indices of strs to their own list and put that list inthe new list based on whether or not it's already there or not
'''
