
ans = int(input())
a= list()

for i in range(ans):
    a.append(int(input()))

b = sorted(a)
std = a[0]
result = list()
emp_list = list()
flag = 0

for j in range(ans):
    if j == 0:
        for k in range(1,a[j]+1):
            result.append("+")
            emp_list.append(k)
            max = k
        result.append("-")
        emp_list.pop()
        
    elif j > 0:
        if emp_list and emp_list[-1] == a[j]:
            result.append("-")
            emp_list.pop()
            
        elif emp_list and a[j] > emp_list[-1]:
            for z in range(max+1,a[j]+1):
                max = z
                result.append("+")
                emp_list.append(z)
            result.append("-")
            emp_list.pop()
            
            if max == b[-1]:
                while emp_list:
                    emp_list.pop()
                    result.append("-")
                break

        elif not emp_list and a[j] == b[j]:
            result.append("+")
            emp_list.append(a[j])
            max = a[j]
            result.append("-")
            emp_list.pop()

        elif not emp_list and a[j] > b[j]:
            for z in range(max+1,a[j]+1):
                max = z
                result.append("+")
                emp_list.append(z)
            result.append("-")
            emp_list.pop()

        else :
            flag = 1
            break

if flag == 0:
    print('\n'.join(result))
elif flag == 1:
    print("NO")