def Solution(input_list,s1,x):
   side =1
   mid = s1
   search_value = input_list[s1]+1
   while True:
      if side%2==1:
         find = None 
         for i in range(mid,-1,-1):
            if input_list[i]==search_value:
               find = i
               break 
         if find!=None:
            search_value=input_list[find]+1
            input_list[mid]=input_list[mid]+x
            mid = find
         else:
            return input_list
            break 
      if side%2==0:
         find = None 
         for i in range(mid+1,len(input_list)):
            if input_list[i]==search_value:
               find = i
               break 
         if find!=None:
            search_value=input_list[find]+1
            input_list[mid]=input_list[mid]+x
            mid = find
         else:
            return input_list
            break
      side+=1 
input_list = [3,3,2,2,4,5]
s=2
x=4
print(Solution(input_list,s,x))


