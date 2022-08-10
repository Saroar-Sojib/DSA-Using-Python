if __name__ == '__main__':
    N = int(input())
    res_list = []
    for i in range(0,N):
        name = input().split();
        if name[0] == "insert":
            res_list.insert(int(name[1]),int(name[2]))
        elif name[0] == "print":
            print(res_list)
        elif name[0] == "remove":
            res_list.remove(int(name[1]))
        elif name[0] == "append":
            res_list.append(int(name[1]))
        elif name[0] == "sort": 
            res_list.sort()
        elif name[0] == "pop":
            res_list.pop()
        elif name[0] == "reverse":
            res_list.reverse()

