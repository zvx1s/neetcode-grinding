class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy = {}
        for i, index in enumerate(nums):
            if index in hashy:
                return True
        return False