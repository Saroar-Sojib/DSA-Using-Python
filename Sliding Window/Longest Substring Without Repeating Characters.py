s="pwwkew"
lst=[]
maxl=0
for i in s:
    if i in lst:
        lst=lst[lst.index(i)+1:]
    lst.append(i)
    if len(lst)>maxl:
        maxl=len(lst)
print(maxl)