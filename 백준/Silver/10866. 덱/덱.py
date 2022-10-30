from collections import deque
import sys

n = int(input())

dq = deque()

for _ in range(n):
    com = sys.stdin.readline().strip()
    if ' ' in com:
        a,b = com.split()
    else :
        a = com

    if a == 'push_back':
        dq.append(b)

    elif a == 'push_front':
        dq.appendleft(b)

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

    elif a == 'size':
        print(len(dq))

    elif a == 'empty':
        if dq:
            print(0)
        else :
            print(1)

    elif a == 'pop_front':
        if dq:
            print(dq.popleft())
        else :
            print(-1)

    elif a == 'pop_back':
        if dq:
            print(dq.pop())
        else :
            print(-1)




