class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy = {}
        for i, index in enumerate(len(nums)):
            if nums[i] in hashy:
                return True
        return False