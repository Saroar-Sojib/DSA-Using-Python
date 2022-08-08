nums = [1,5,0,3,5]
nums.sort()
n= len(nums)
cnt=0
j=0
while j<n:
    sub_eli = nums[j]
    if sub_eli == 0:
        j+=1
        continue
    find =0
    for i in range(0,n):
        if nums[i]==0:
            continue
        elif nums[i]-sub_eli>=0:
            nums[i]=nums[i]-sub_eli
            find += 1
    if find!=0:
        cnt+=1
    j+=1
print(cnt)
