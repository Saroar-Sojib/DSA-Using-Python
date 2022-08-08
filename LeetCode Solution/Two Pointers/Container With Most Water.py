height = [1,1]
left_value=0
right_value=len(height)-1
res = 0
while(left_value<right_value):
    temp_result = (right_value-left_value)*min(height[left_value],height[right_value])
    res = max(temp_result,res)
    if height[left_value]<height[right_value]:
        left_value+=1
    else:
        right_value-=1
print(res)
