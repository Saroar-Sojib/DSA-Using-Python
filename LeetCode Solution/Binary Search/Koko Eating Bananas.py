piles = [30,11,23,4,20]
h = 6

max_value = max(piles)

left_value = 1
right_value = max_value
mid = 0
res = max_value
while(left_value<=right_value):
    mid = (left_value+right_value)//2
    cnt=0
    for x in piles:
        temp_div = x//mid
        if temp_div*mid<x:
            temp_div=temp_div+1
        elif temp_div==0:
            temp_div+=1
        cnt+=temp_div

    if cnt<=h:
        right_value=mid-1 
        res = min(res,mid)
    else:
        left_value = mid+1
print(res)

        