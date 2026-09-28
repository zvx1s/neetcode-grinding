class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      hashy = {}
      mylist = []
      for i, index in enumerate(nums):
        if target - nums[i] in hashy:
            if nums[i] != target - nums[i]:
                mylist = [i,hashy[target - nums[i]]]
                return mylist
        else:
            hashy[nums[i]] = i
        
