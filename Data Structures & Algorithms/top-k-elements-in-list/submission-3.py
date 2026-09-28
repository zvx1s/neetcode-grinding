class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = 0
        mydict = {}
        for i in range(len(nums)):
            if nums[i] in mydict:
                mydict[nums[i]]+=1
            else:
                mydict[i] = 1
        for i in range(len(nums)):
            if mydict[i] > mydict[i+1]:
                temp = mydict[i+1]
                mydict[i+1] = mydict[i]
                mydict[i] = temp
        return [mydict[-1], mydict[-3]]
        