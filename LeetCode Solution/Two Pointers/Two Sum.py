# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         res=[]
#         left_value = 0
#         right_value = len(numbers)-1
#         while left_value<right_value:
#             sum_value = numbers[left_value]+numbers[right_value]
#             if sum_value>target:
#                 right_value-=1
#             elif sum_value<target:
#                 left_value+=1
#             else:
#                 res+=[left_value+1,right_value+1]
#                 break
#         return res
        

numbers = [0,0,3,4]
target = 0
res=[]
left_value = 0
right_value = len(numbers)-1
while left_value<right_value:
    sum_value = numbers[left_value]+numbers[right_value]
    if sum_value>target:
        right_value-=1
    elif sum_value<target:
        left_value+=1
    else:
        res+=[left_value+1,right_value+1]
        break 
print(res)




