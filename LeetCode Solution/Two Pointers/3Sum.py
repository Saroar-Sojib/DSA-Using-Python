# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         response = []
#         # [-4, -1, -1, 0, 1, 2]
#         for left in range(len(nums) - 2):
			
#             if left > 0 and nums[left] == nums[left - 1]:
#                 continue
#             mid = left +1
#             right = len(nums) -1
#             while (mid < right):
#                 s = nums[left] + nums[mid] + nums[right]
#                 if s < 0:
#                     mid += 1
#                 elif s > 0:
#                     right -=1
#                 else:
#                     response.append([nums[left], nums[mid], nums[right]])
# 					# Ignore duplicates
#                     while mid < right and nums[mid] == nums[mid+1]:
#                         mid += 1
#                     while mid < right and nums[right] == nums[right-1]:
#                         right -= 1
#                     mid += 1
#                     right -= 1
                    
#         return response

nums = [-1,0,1,2,-1,-4]
nums.sort()
#print(nums)
temp_list=[]
for left in range(0,len(nums)-2):
    mid_value = left+1
    right_value = len(nums)-1
    while mid_value < right_value:
        s = nums[left]+nums[mid_value]+nums[right_value]
        #print(nums[left],nums[mid_value],nums[right_value])
        if s<0:
            mid_value+=1
        elif s>0:
            right_value-=1
        else:
            temp_list.append([nums[left],nums[mid_value],nums[right_value]])
            mid_value+=1
            right_value-=1
temp_list = [list(item) for item in set(tuple(row) for row in temp_list)]
print(temp_list) 


    