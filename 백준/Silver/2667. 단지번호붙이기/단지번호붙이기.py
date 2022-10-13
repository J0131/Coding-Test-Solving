import itertools
import math
import sys
from collections import deque as dq

n = int(input())

n_list = []

for _ in range(n):
    n_list.append(list(map(int,sys.stdin.readline().strip())))

danji = dq()
#print(n_list)

for i in range(n):
    for j in range(n):
        if n_list[i][j] == 1:
            danji.append([i,j])

dx = [1,0,-1,0]
dy = [0,1,0,-1]

haveto = dq()
visited = []
count_list = []

while danji:

    haveto.append(danji.popleft())
    count = 0

    while haveto:
        node = haveto.popleft()
        if node not in visited:
            visited.append(node)
            count += 1
    
            rx, ry = node

            for i in range(4):
                x = rx + dx[i]
                y = ry + dy[i]
    
                if 0<=x<n and 0<=y<n and n_list[x][y] == 1:
                    if [x,y] not in visited and [x,y] not in haveto:
                        haveto.append([x,y])
                        if [x,y] in danji:
                            danji.remove([x,y])
        
    count_list.append(count)

count_list.sort()
print(len(count_list))

for i in count_list:
    print(i)
#print(n_list)