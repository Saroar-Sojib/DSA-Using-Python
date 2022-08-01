class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        ans = 0
        for n in nums:
            if (n-1) not in unique_nums:
                temp_length = 0
                while (n+temp_length) in unique_nums:
                    temp_length+=1
                ans = max(ans,temp_length)
        return ans
                    