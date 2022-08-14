matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
def binary_search(nums,temp_target):
    left_node = 0
    right_node = len(nums)-1
    mid_node = 0
    if len(nums)==0:
        return -1
    while(right_node-left_node>1):
        mid_node = (left_node+right_node)//2
        if temp_target==nums[mid_node]:
            return mid_node
        
        if temp_target<nums[mid_node]:
            right_node=mid_node-1
        else:
            left_node=mid_node
    if temp_target==nums[right_node]:
            return right_node
    if temp_target==nums[left_node]:
        return left_node
    return -1

find = False
for x in matrix:
    n=len(x)
    if target<=x[n-1]:
        if binary_search(x,target)!=-1:
            find=True
            break
print(find) 

