import collections
import sys

m, n = map(int,input().split())

n_list = [[0]*m for _ in range(n)]

for i in range(n):

    n_list[i] = list(map(int,sys.stdin.readline().split()))

queue = collections.deque()

for i in range(n):
        for j in range(m):
            if n_list[i][j] == 1 :
                queue.append([i,j])

dx = [-1,0,1,0]
dy = [0,-1,0,1]

while queue:
    x,y = queue.popleft()
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if n_list[nx][ny] == 0:
                queue.append([nx,ny])
                n_list[nx][ny] = n_list[x][y] + 1

answer = 0

for i in range(n):
    for j in range(m):
        if n_list[i][j] == 0:
            print(-1)
            sys.exit()
        answer = max(answer, n_list[i][j])

print(answer-1)

