
stack = []
s = "()[]{}"
close_parentheses = {')':'(','}':'{',']':'['}
for x in s:
    if x in close_parentheses:
        if stack and stack[-1]==close_parentheses[x]:
            stack.pop()
        else:
            print(False) 
    else:
        stack.append(x)
if len(stack)==0:
    print(True) 
else:
    print(False)  