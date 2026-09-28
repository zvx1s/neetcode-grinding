class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy = {}
        for i, index in enumerate(nums):
            if nums[i] in hashy:
                return True
            hashy[nums[i]] = True
        return False