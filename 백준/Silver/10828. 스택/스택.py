import sys

n = int(input())

stack_list = list()
n_list = [0,0]

for _ in range(n):
    
    str = sys.stdin.readline().strip()
    n_list = str.split()

    if n_list[0] == "push":
        stack_list.append(n_list[1])

    elif n_list[0] == "pop":
        if not stack_list:
            print(-1)
        else :
            print(stack_list.pop())

    elif n_list[0] == "size":
        print(len(stack_list))

    elif n_list[0] == "empty":
        if not stack_list:
            print(1)
        else :
            print(0)

    elif n_list[0] == "top":
        if not stack_list:
            print(-1)
        else :
            print(stack_list[-1])