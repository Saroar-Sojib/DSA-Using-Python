items1 = [[1,3],[2,2]]
items2 = [[7,1],[2,2],[1,4]]
final_list = items1+items2
temp_dict = {}
temp_list=[]
for x in final_list:
    if x[0] in temp_dict:
        temp_dict[x[0]]=temp_dict[x[0]]+x[1]
    else:
        temp_dict[x[0]]=x[1]
        temp_list.append(x[0])
temp_list.sort()
res = []
for i in temp_list:
    res.append([i,temp_dict[i]])
print(res)


