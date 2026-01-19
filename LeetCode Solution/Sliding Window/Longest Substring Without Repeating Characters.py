s="pwwkew"
lst=[]
maxl=0
for i in s:
    if i in lst:
        print(lst.index(i))
        lst=lst[lst.index(i)+1:]
        print("after: ",lst)
    lst.append(i)
    if len(lst)>maxl:
        maxl=len(lst)
print(maxl)