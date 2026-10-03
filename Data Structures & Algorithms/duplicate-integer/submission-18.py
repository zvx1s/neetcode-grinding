class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy = {}
        for i in range(len(nums)):
            if nums[i] in hashy:
                return True
            hashy[i] = nums[i]
        return False