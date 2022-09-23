import sys
import copy
from collections import deque 

n = int(input())
visited = [[False] * n for _ in range(n)]
px = [1,0,-1,0]
py = [0,1,0,-1]
n_list = list()

for _ in range(n):
    n_list.append(list(map(str,sys.stdin.readline().strip())))

def bfs(x, y, col):
    q = deque()
    q.append([x,y])

    while q:
        x, y = q.popleft()
        
        if visited[x][y] == False:
            visited[x][y] = True
            for i in range(4):
                nx = x + px[i]
                ny = y + py[i]

                if 0 <= nx < n and 0 <= ny < n:
                    if n_list[nx][ny] == col:
                        q.append([nx,ny])

count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            col = n_list[i][j]
            bfs(i,j,col)
            count += 1

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if n_list[i][j] == 'G':
            n_list[i][j] = 'R'

count_gr = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            col = n_list[i][j]
            bfs(i,j,col)
            count_gr += 1

print(count, count_gr)
