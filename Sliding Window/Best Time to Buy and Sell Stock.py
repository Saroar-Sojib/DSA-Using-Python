prices = [1,4,3,2]
left_pointer = 0
right_pointer = 1
res = 0

while(right_pointer<len(prices)):
    if prices[left_pointer]>prices[right_pointer]:
        temp_res = prices[right_pointer]-prices[left_pointer]
        res = max(temp_res,res)
        left_pointer=right_pointer
        right_pointer=right_pointer+1
    else:
        temp_res = prices[right_pointer]-prices[left_pointer]
        res = max(temp_res,res)
        right_pointer+=1

print(res)