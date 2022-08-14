n=3
res=[]
stack=[]
def backtrack(open_bracket,close_bracket):
    if open_bracket==close_bracket==n:
        res.append("".join(stack))
        return res
    if open_bracket<n:
        stack.append("(")
        backtrack(open_bracket+1,close_bracket)
        stack.pop()
    if close_bracket<open_bracket:
        stack.append(")")
        backtrack(open_bracket,close_bracket+1)
        stack.pop()

backtrack(0,0)
print(res)