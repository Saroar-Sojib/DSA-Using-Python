board = [
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]]

ans = True
cnt = 0
square_grid ={}
a=[]
b=[]
c=[]
for i in range(0,len(board)):
    dict_1={}
    dict_2={}
    cnt=0
    for j in range(0,len(board[i])):
        if board[i][j] not in dict_1 and board[i][j]!='.':
            dict_1[board[i][j]]=1
            if j<=2:
                a.append(board[i][j])
            elif j>=3 and j<=5:
                b.append(board(board[i][j]))
            elif j>=6 and j<=8:
                c.append(board[i][j])
            
        elif board[i][j] in dict_1:
            ans = False
            break 
        if board[j][i] not in dict_2 and board[j][i]!='.':
            dict_2[board[j][i]]=1
            
        elif board[j][i] in dict_2:
            ans = False
            break
    if (i+1)%3==0 and i!=0:
        if len(a)!=len(set(a)) or len(b)!=len(set(b)) or len(c)!=len(set(c)):
            ans = False
        else:
            a=[]
            b=[]
            c=[]
    if ans is False:
        break
print(ans)