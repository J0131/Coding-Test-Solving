import sys
from collections import deque

n, m = map(int,(input().split()))

n_list = []
visited = [[0]*m for _ in range(n)]
node_visited = []
check_visited = [[False]*m for _ in range(n)]

for _ in range(n):
    n_list.append(sys.stdin.readline().strip())

nx = [-1,0,1,0]
ny = [0,1,0,-1]

visited[0][0] = 1

q = deque()
q.append([0,0])

while q:
    node = q.popleft()
    x, y = node

    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]

        if 0 <= dx < n and 0 <= dy < m:
            if n_list[dx][dy] != '0':
                if check_visited[dx][dy] == False:
                    q.append([dx,dy])
                    check_visited[dx][dy] = True
                    visited[dx][dy] = visited[x][y] + 1

print(visited[n-1][m-1])
