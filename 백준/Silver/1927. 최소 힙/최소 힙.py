import heapq
import sys
from collections import deque

n = int(input())

hq = []

n_list = deque()

for _ in range(n):
    n_list.append(int(sys.stdin.readline().strip()))

while n_list:
    nn = n_list.popleft()

    if nn == 0:
        if hq:
            print(heapq.heappop(hq))
        else :
            print(0)
    
    else :
        heapq.heappush(hq,nn)