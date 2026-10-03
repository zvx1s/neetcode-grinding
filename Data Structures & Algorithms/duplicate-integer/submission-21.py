class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy = {}
        for num in nums:
            if num in hashy:
                return True
            hashy[num] = True
        return False