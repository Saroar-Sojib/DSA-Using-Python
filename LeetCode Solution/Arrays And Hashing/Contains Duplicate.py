class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp_len = len(nums)
        real_len = len(set(nums))
        if temp_len == real_len:
            return False
        else:
            return True