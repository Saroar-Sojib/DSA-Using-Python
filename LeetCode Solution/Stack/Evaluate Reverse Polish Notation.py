stack = []
all_symbol = ["+","-","*","/"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
for x in tokens:
    if x in all_symbol:
        if x == "+":
            if len(stack)>=2:
                y = int(stack[len(stack)-2])+int(stack[len(stack)-1])
                print("before: ",stack)
                stack.pop()
                stack.pop()
                stack.append(y)
                print("after: ",stack)
        elif x == "-":
            if len(stack)>=2:
                y = int(stack[len(stack)-2])-int(stack[len(stack)-1])
                print("before: ",stack)
                stack.pop()
                stack.pop()
                stack.append(y)
                print("after: ",stack)
        elif x == "*":
            if len(stack)>=2:
                y = int(stack[len(stack)-2])*int(stack[len(stack)-1])
                print("before: ",stack)
                stack.pop()
                stack.pop()
                stack.append(y)
                print("after: ",stack)
        elif x == "/":
            if len(stack)>=2:
                y = int(int(stack[len(stack)-2])/(int(stack[len(stack)-1])))
                print("before: ",stack)
                stack.pop()
                stack.pop()
                stack.append(y)
                print("after: ",stack)
    else:
        stack.append(x)
       
print(stack[0])
