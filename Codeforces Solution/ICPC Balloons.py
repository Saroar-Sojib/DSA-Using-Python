n=int(input())
for i in range(n):
    len_number = int(input())
    string = input()
    print(len_number+len(set(list(string))))