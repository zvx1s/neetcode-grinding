class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy = {}
        for i, num in enumerate(nums):
            if nums[i] in hashy.values():
                return True
            hashy[i] = nums[i]
        return False