import sys
from itertools import combinations

n, m = map(int,input().split())

n_list = []
ch_list = []
house_list = []
dist_list = [[0]*n for _ in range(n)]
only_dist = []

for _ in range(n):
    n_list.append(list(map(int,sys.stdin.readline().split())))


for i in range(n):
    for j in range(n):
        if n_list[i][j] == 1:
            house_list.append([i,j])
        elif n_list[i][j] == 2:
            ch_list.append([i,j])

ch_comb = list(combinations(ch_list,m))

for i in ch_comb:
    sum = 0 
    for j in house_list:
        x,y = j
        min_v = n*n
        for k in i:
            x2, y2 = k
            if abs(x-x2) + abs(y-y2) < min_v:
                min_v = abs(x-x2) + abs(y-y2)
        sum += min_v
    only_dist.append(sum)

"""only_dist.sort()
sum = 0
for i in range(m):
    sum += only_dist[i]"""


print(min(only_dist))


