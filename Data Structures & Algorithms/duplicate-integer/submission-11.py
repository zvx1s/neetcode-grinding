class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy = {}
        for i, num in enumerate(nums):
            hashy[i] = num
            if num in hashy:
                return True
        return False