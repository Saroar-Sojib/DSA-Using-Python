from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        initial_index = 0
        for i in range(0,len(nums)):
            ans += min(nums[initial_index],nums[initial_index + 1])
            initial_index += 2
            if initial_index >= len(nums)-1:
                break 
        return ans

sln = Solution()
nums = [6,2,6,5,1,2]
print(sln.arrayPairSum(nums))
