nums = [3,4,5,1,2]
left_value = 0
right_value = len(nums)-1
mid = 0
res = nums[0]
while(left_value<=right_value):
    if nums[left_value]<nums[right_value]:
            res = min(res,nums[left_value])
            break
    
    mid = (left_value+right_value)//2
    res = min(res,nums[mid])
    if nums[mid]>=nums[left_value]:
        left_value = mid+1
    else:
        right_value = mid-1
        
print(res)  