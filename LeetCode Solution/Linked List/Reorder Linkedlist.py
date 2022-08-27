head = [1,2,3,4,5]
left_pointer = 0
right_pointer =len(head)-1
res=[]
while(left_pointer<=right_pointer):
    if left_pointer==right_pointer:
        res.append(head[left_pointer])
    else:
        res.append(head[left_pointer])
        res.append(head[right_pointer])
    left_pointer+=1
    right_pointer-=1
print(res)
