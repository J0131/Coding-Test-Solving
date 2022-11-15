import sys
from collections import deque

n = int(input())
n_list = []
dq = deque()

for _ in range(n):
    n_list.append(sys.stdin.readline().split())


for i in n_list:
    if len(i) > 1:
        a, b = i
    else :
        a = i[0]

    if a == 'push':
        dq.append(int(b))

    elif a == 'front':
        if dq:
            print(dq[0])
        else :
            print(-1)
    
    elif a == 'back':
        if dq:
            print(dq[-1])
        else :
            print(-1)
    
    elif a == 'pop':
        if dq:
            print(dq.popleft())

        else :
            print(-1)
    
    elif a == 'size':
        print(len(dq))

    elif a == 'empty' :
        if dq:
            print(0)

        else :
            print(1)