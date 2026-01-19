nums = [4,5,6,7,0,1,2]
target = 0
def binary_search(nums,target):
    left_value = 0
    right_value= len(nums)-1
    while(left_value<=right_value):
        middle_value = (left_value+right_value)//2
        if nums[middle_value]==target:
            return middle_value
        if nums[left_value]<=nums[middle_value]:
            if target>nums[middle_value] or target<nums[left_value]:
                left_value=middle_value+1
            else:
                right_value = middle_value-1
        else:
            if target<nums[middle_value] or target>nums[right_value]:
                right_value = middle_value-1
            else:
                left_value = middle_value+1
    return -1
print(binary_search(nums,target))