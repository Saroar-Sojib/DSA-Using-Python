nums = [2,5]
target = 5
def solution(nums,target):
    left_node = 0
    right_node = len(nums)-1
    mid_node = 0
    if len(nums)==0:
        return -1
    while(right_node-left_node>1):
        mid_node = (left_node+right_node)//2
        if target==nums[mid_node]:
            return mid_node
        
        if target<nums[mid_node]:
            right_node=mid_node-1
        else:
            left_node=mid_node
    if target==nums[right_node]:
            return right_node
    if target==nums[left_node]:
        return left_node
    return -1
print(solution(nums,target))


