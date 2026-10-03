class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy = {}
        for i, num in enumerate(nums):
            if num in hashy:
                return True
            hashy[i] = index
        return False