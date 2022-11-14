import sys


n = int(input())

for _ in range(n):

    flag = 0
    st = sys.stdin.readline().strip()

    left_list = []

    for i in st:
        if i == '(':
            left_list.append(i)
        else :
            if not left_list :
                print("NO")
                flag = 1
                break
            else :
                left_list.pop()
    
    if flag == 0:
        if not left_list:
            print("YES")
        
        else :
            print("NO")
    
        
