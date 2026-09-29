class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp_list = []
        stri = ""
        new_list = []
        for i in range(len(strs)):
            temp_list = sorted(strs[i])
            for j in range(len(temp_list)):
                stri += temp_list[j]
            new_list.append(stri)
            stri = ""

        counter = 0   
        hashy = {}
        for k, wrd in enumerate(new_list):
            if wrd not in hashy:
                hashy[wrd] = counter
                counter += 1
                
        
        actual_list = [[] for _ in range(counter)]
        for i, word in enumerate(new_list):
            group = hashy[word]
            actual_list[hashy[word]].append(strs[i])

        return actual_list
            






        

















'''Sort each element alphabetically, then use the hashmap to check if it's already been added to it or not, then add the indices of strs to their own list and put that list inthe new list based on whether or not it's already there or not
'''
