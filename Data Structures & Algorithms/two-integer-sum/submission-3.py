class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      hashy = {}
      for i, index in enumerate(nums):
        if target - nums[i] in hashy:
            if nums[i] != target - nums[i]:
                mylist = [i,target-nums[i]]
                print(mylist)
        
