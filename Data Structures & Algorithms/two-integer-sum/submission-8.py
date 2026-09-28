class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      hashy = {}
      mylist = []
      for i, num in enumerate(nums):
        if target - num in hashy:
            mylist = [i,hashy[target - num]]
            return mylist
        else:
            hashy[num] = i
        
