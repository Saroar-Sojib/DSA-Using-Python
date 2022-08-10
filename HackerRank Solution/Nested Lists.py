def solution(students):
    temp_dict = {}
    for x in students:
        if x[1] not in temp_dict:
            temp_dict[x[1]]=[x[0]]
        else:
            temp_dict[x[1]].append(x[0])
    
    temp_value = list(temp_dict.keys())
    temp_value.sort()
    res = temp_dict[temp_value[1]]
    res.sort()
    for x in res:
        print(x)

if __name__ == '__main__':
    n = int(input())
    students = []
    for i in range(0,n):
        x=str(input())
        y=float(input())
        temp_list = [x,y]
        students.append(temp_list)
    solution(students)
    
