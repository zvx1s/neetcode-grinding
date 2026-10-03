class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy = {}
        for i, num in enumerate(nums):
            if nums[i] in hashy:
                return True
            hashy[i] = nums[i]
        return False