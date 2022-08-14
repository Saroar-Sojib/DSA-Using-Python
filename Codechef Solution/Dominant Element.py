n = int(input())
for i in range(0,n):
    length = int(input())
    nums = [int(x) for x in input().split()]
    temp_dict = {}
    for x in nums:
        if x in temp_dict:
            temp_dict[x]=temp_dict[x]+1
        else:
            temp_dict[x]=1
    print(temp_dict)